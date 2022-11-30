import os
from email.message import EmailMessage
import ssl
import smtplib

# Provide email sender credentials and receiver email
email_sender = 'xxx'
email_password = os.environ['xxx']
email_receiver = 'xxx'

subjet = 'Hello dear vine lover,'
body = '''
    There is some vine selection for you.
    '''
    
msg = EmailMessage()
msg['From'] = email_sender
msg['To'] = email_receiver
msg['Subject'] = subjet
msg.set_content(body)

context = ssl.create_default_context()

# Change protocol and port if useing other email service
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, msg.as_string())
    print('Email sent!')
