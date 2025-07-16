import os
from dotenv import load_dotenv
import smtplib, ssl

load_dotenv()

username = os.getenv("MAIL_USER")
password = os.getenv("MAIL_PASS")
receiver = os.getenv("RECEIVER_EMAIL")

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    email_message = f"""\
From: {username}
To: {receiver}
Subject: Daily News

{message.decode() if isinstance(message, bytes) else message}
"""

    print(f"username: {repr(username)}")
    print(f"password: {repr(password)}")

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, email_message.encode("utf-8"))