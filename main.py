
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



import os

from dotenv import load_dotenv
load_dotenv()
import gspread
from oauth2client.service_account import ServiceAccountCredentials


print("hello")


def send_mail(recipient_emails, recipient_companies, status):
    print(recipient_emails, recipient_companies)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587 
    sender_email = 'your email'
    sender_password = 'your mail password'
    subject = 'Subject'
    with open('email_template.html', 'r') as file:
        email_template = file.read()

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        for index, recipient_email in enumerate(recipient_emails):
            if status[index] != 'Sent':
          
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['Subject'] = subject
                email_body = email_template.format(company_name=recipient_companies[index])
                msg.attach(MIMEText(email_body, 'html'))
                server.sendmail(sender_email, recipient_email, msg.as_string())

    print('Emails sent successfully.')


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']


creds = 'key.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(creds, scope)
client = gspread.authorize(credentials)

#Sheet Title
sheet_title = 'MailSheet'
sheet = client.open(sheet_title).sheet1



recipient_emails= []
recipient_companies =[]
status = []

count =0
for i in sheet.get_all_records():
    print(i)
    sheet.update_cell(count +2,2, "Sent")
    recipient_emails.append(i['Mail ID'])
    recipient_companies.append(i['Company Name'])
    status.append(i['Status'])
    count = count+1



send_mail(recipient_emails, recipient_companies, status)











