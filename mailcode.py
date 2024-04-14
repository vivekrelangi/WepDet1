"""import smtplib
import ssl

smtp_port = 587
smtp_server = "smtp.gmail.com"

email_from = "wepdet@gmail.com"
email_to = "wepdet@gmail.com"

pswd = "your password"

message = "Mail code"

simple_email_context = ssl.create_default_context()

try:
    print("connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, pswd)
    print("connected to server :)")

    print()
    print(f"Sending email to - {email_to}")
    TIE_server.sendmail(email_from, email_to, message)
    print(f"Email successfully sent to - {email_to}")

except Exception as e:
    print(e)

finally:
    TIE_server.quit()"""

#with attachments
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import ssl

smtp_port = 587
smtp_server = "smtp.gmail.com"

email_from = "wepdet@gmail.com"
email_to_list = ["wepdet@gmail.com"]#we can add any number of receipents in the list

pswd = "your password"

subject = "Weapon Detected"

def send_emails(email_to_list,fn):

    for p in email_to_list:

        body = f"""
        A weapon has been detected in camera 1. 
        Contact police and security 
        Get to a safe place
        """

        msg = MIMEMultipart()
        msg['from'] = email_from
        msg['to'] = p
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        filename = f"/path/{fn}"

        attachment = open(filename, 'rb')

        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition',"attachment; filename= "+filename)
        msg.attach(attachment_package)

        text = msg.as_string()

        print("connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("connected to server :)")

        print()
        print(f"Sending email to - {p}...")
        TIE_server.sendmail(email_from, p, text)
        print(f"Email successfully sent to - {p}")
        print()
    
    TIE_server.quit()

#send_emails(email_to_list)
