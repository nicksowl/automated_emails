import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

EMAIL_SERVER = 'smtp.gmail.com'
PORT = 587 # For starttls

# Load environment variables from .env file
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars_vars = current_dir / '.env'
load_dotenv(envars_vars)

# Read variables
sender_email = os.getenv('EMAIL')
pwd_email = os.getenv('PASSWORD')

def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = formataddr(('Your good friend.', f'{sender_email}'))
    msg['To'] = receiver_email
    msg['BCC'] = sender_email
    
    msg.set_content(
        f'''\
            Hi {name},
            How are you?
            I just wanted to remind you to send me {amount} USD for invoice #{invoice_no} by {due_date}.
            That's it.
            Best regards,
            Your good friend.
        '''
    )
    
    msg.add_alternative(
        f'''\
             <html>
             <body>
                <p>Hi {name},</p>
                <p>How are you?</p>
                <p>I just wanted to remind you to send me <strong>{amount} USD</strong> for invoice <strong>#{invoice_no}</strong> by <strong>{due_date}</strong>.</p>
                <p>That's it.</p>
                <p>Best regards,</p>
                <p>Your good friend.</p>
            </body>
            </html>   
        ''',
            subtype='html',
    )
    
    with smtplib.SMTP(EMAIL_SERVER, PORT) as smtp:
        smtp.starttls()
        smtp.login(sender_email, pwd_email)
        smtp.sendmail(sender_email, receiver_email, msg.as_string())
        
    
if __name__ == '__main__':
    send_email(
        subject='Invoice reminder',
        receiver_email='nickbay767@gmail.com',
        name='John Doe',
        due_date='29, November 2022',
        invoice_no='123456',
        amount='10',
    )
