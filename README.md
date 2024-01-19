# Scraping-Python-MongoDB-Instagram

## Overview

Scraping-Python-MongoDB-Instagram is a Python script for scraping Instagram data based on a specific hashtag and storing it in MongoDB. The script uses the `instagrapi` library for Instagram scraping.

## Features

- Fetches Instagram posts related to a specified hashtag.
- Stores post details (caption, comments, image URL) in a MongoDB database.
- Simple and modular structure for easy customization.

## Requirements

- Python 3.11
- MongoDB installed and running
- Required Python packages: `instagrapi`, `pymongo`

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/MedHisoka11/Scraping-Python-MongoDB-Instagram.git
cd Scraping-Python-MongoDB-Instagram

### 2. Install dependencies:

pip install -r requirements.txt

### 3. Set up MongoDB:

Make sure MongoDB is installed and running.
Update MongoDB connection details in the script or use environment variables.

Usage
Update credentials:

Open credentials.py and provide your Instagram username and password.
Run the script:


python main.py
Enter the hashtag when prompted.

Contributing
Feel free to contribute to this project by opening issues or submitting pull requests. Your contributions are valuable and appreciated!
