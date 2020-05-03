import smtplib
from email.mime.text import MIMEText
import json


def sendMail():
    emails = json.loads(open('emails.json').read())

    for email in emails:

        email_user = "Your email address here"  # Your email address
        email_target = email

        msg = MIMEText("Email content here")  # Email content
        msg['From'] = email_user
        msg['To'] = email_target
        msg['Subject'] = "Email subject here"  # Email subject

        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Change accordingly
        server.starttls()
        server.login(email_user, 'Your email login password here')  # Your email login password
        server.sendmail(email_user, email_target, text)
        server.quit()


if __name__ == "__main__":
    sendMail()
