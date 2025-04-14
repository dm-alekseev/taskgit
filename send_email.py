import smtplib
import sys
from email.mime.text import MIMEText
from email.message import EmailMessage
from credentials import *


commit_msg = sys.stdin.read().strip()
print(commit_msg)

msg = EmailMessage()
msg['Subject'] = 'Новый коммит!'
msg['From'] = sender_email
msg['To'] = recipient_email
msg.set_content[''] = 'commit_msg'

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender_email, sender_password)
    server.send_message(msg)
    print('Email sent successfully!')

