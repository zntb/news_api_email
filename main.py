from dotenv import load_dotenv
import os

import requests

load_dotenv()  # Loads variables from .env

API_KEY = os.getenv("NEWS_API_KEY")
print("API_KEY",API_KEY)

url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-06-15&sortBy=publishedAt&apiKey={API_KEY}"


# Make the request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])