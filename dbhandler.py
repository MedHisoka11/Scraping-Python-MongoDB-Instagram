import pymongo

def connect():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["instagram"]
    collection = db["posts"]
    return collection