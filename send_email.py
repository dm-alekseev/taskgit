import smtplib
from email.message import EmailMessage
from credentials import *


msg = EmailMessage()
msg['Subject'] = 'Новый коммит!'
msg['From'] = sender_email
msg['To'] = 'a@stw.by'
msg.set_content(f'Сделан коммит с текстом:')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login('puhxxx@gmail.com', 'caok opfy tbqa jjod')
    server.send_message(msg)

