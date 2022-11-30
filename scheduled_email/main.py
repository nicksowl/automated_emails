from deta import app
from datetime import date
import pandas as pd
from send_email import send_email

# Fixes ssl issue while executing the script
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

SHEET_ID = '1w4LPyjVRGrgYvQm08xrW_HgUo_DU_x0OIMSykp40SV0'
SHEET_NAME = 'Sheet1'
URL = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'

def load_df(url):
    parse_dates = ['due_date', 'reminder_date']
    df = pd.read_csv(url, parse_dates=parse_dates)
    return df

def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (present >= row['reminder_date'].date()) and (row['has_paid'] == 'no'):
            send_email(
                subject=f'Invoice reminder #{row["invoice_no"]}',
                receiver_email=row['email'],
                name=row['name'],
                due_date=row['due_date'].strftime('%d, %b %Y'),
                invoice_no=row['invoice_no'],
                amount=row['amount'],
            )
            email_counter += 1
    return f'Total emails sent: {email_counter}'

# df = load_df(URL)
# result = query_data_and_send_emails(df)
# print(result)

@app.lib.cron()
def cron_job(event):
    df = load_df(URL)
    result = query_data_and_send_emails(df)
    return result  