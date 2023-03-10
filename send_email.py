from email.message import EmailMessage
import ssl
import smtplib
from password import password

email_sender = 'ronaldomano7123@gmail.com'
email_password = password()
email_receiver = 'karthikmk229@gmail.com'

subject = "Dont forget top subscribe"
body = """
when you watch video, please hit subscribe
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em[' subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
