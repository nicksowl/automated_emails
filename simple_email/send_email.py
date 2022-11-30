import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'xxx'
# email_password = os.environ['GMAIL_PASSWORD_1']
email_password = 'xxx'
email_receiver = 'xxx'

subjet = 'Hello dear customer'
body = """
    There is some information for you.
    """
    
msg = EmailMessage()
msg['From'] = email_sender
msg['To'] = email_receiver
msg['Subject'] = subjet
msg.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, msg.as_string())
