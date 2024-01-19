from credentials import ig_username,ig_password
from instagrapi import Client, exceptions
import requests
import io
from PIL import Image
import os
from dbhandler import connect

# Use a class for a more structured data representation
class Post:
    def __init__(self, post_id, caption, comments, image_data):
        self.post_id = post_id
        self.caption = caption
        self.comments = comments
        self.image_data = image_data
        
    def to_dict(self):
        return {
            'post_id': self.post_id,
            'caption': self.caption,
            'comments': self.comments,
            'image_data': self.image_data
        }

collection = connect()  # connect to mongo db
hash_tag = input('Enter Your Topic (hashtag for IG): ')

cl = Client()
try:
    cl.login(ig_username, ig_password)
except exceptions.ClientError as e:
    print("Error logging in:", e)
    exit()

try:
    posts = cl.hashtag_medias_recent(hash_tag, 20)
except exceptions.ClientError as e:
    print("Error fetching posts:", e)
    posts = []

for post in posts:
        try:
            # Download the image with error handling
            response = requests.get(post.thumbnail_url, stream=True)
            response.raise_for_status()  # Raise an exception for non-200 status codes

            filename = f"image_{post.pk}.jpg"
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

            post_data = Post(
                post_id=post.pk,
                caption=post.caption_text,
                comments=[comment.text for comment in cl.media_comments(post.pk)],
                image_data=None
            )

            # Handle image storage in mongo db
            im = Image.open(filename)
            image_bytes = io.BytesIO()
            im.save(image_bytes, format='JPEG')
            post_data.image_data = image_bytes.getvalue()

            collection.insert_one(post_data.to_dict())  # Insert using a dictionary representation
            os.remove(filename)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading image {post.pk}: {e}")
