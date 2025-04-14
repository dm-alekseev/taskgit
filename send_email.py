import smtplib
import sys
from email.mime.text import MIMEText
from email.message import EmailMessage
from credentials import *

branch_name = sys.stdin.read().strip()
commit_msg = sys.stdin.read().strip()
print(branch_name)
print(commit_msg)

msg = EmailMessage()
msg['Subject'] = 'New commit'
msg['From'] = sender_email
msg['To'] = recipient_email
msg.set_content(f'Branch: {branch_name} , {commit_msg}')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender_email, sender_password)
    server.send_message(msg)
    print('Email sent successfully!')

