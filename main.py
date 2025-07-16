from dotenv import load_dotenv
import os
import requests
from send_email import send_email

load_dotenv() 
API_KEY = os.getenv("NEWS_API_KEY")
topic = "tesla"

url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={API_KEY}&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + "\n" + str(article["url"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)