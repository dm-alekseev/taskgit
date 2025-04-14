import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage
from credentials import *


msg = EmailMessage()
msg['Subject'] = 'Новый коммит!'
msg['From'] = sender_email
msg['To'] = recipient_email
msg.set_content(f'Сделан коммит с текстом:')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender_email, sender_password)
    server.send_message(msg)

