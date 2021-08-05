from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


message = MIMEMultipart()
message['from'] = 'ftich214@gmail.com'
message['to'] = "cobbs.daqualynn@gmail.com"
message['subject'] = 'New MIME message'
message.attach(MIMEText('Text'))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login()
    smtp.send_message(message)
    print("Message successfully send")