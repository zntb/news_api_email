from dotenv import load_dotenv
import os

import requests

load_dotenv()  # Loads variables from .env

API_KEY = os.getenv("NEWS_API_KEY")
print("API_KEY",API_KEY)

url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-06-15&sortBy=publishedAt&apiKey={API_KEY}"

request = requests.get(url)
content = request.text

print(content)