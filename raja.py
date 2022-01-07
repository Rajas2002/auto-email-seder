import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

li = ['ashwinbhagatkar@gmail.com', 'rajasbhagatkar@gmail.com' ]
for gmail in li:
    emails=[gmail]

    # html = Template(Path('C:\Users\RajasB\Documents\index.html').read_text())
    email = EmailMessage()
    email['from'] = 'Rajas Bhagatkar'
    email['to'] = 'rajasbhagatkar@gmail.com'
    email['subject'] = 'this is my code from VS code'

    # email.set_content()

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('rajasbhagatkar01@gmail.com', '9423607702')
        smtp.send_message(email)
        print('done boss')