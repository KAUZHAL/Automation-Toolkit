import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com',25)
server.ehlo()#starts the server
"""server.login('your_mail@gmail.com','your_password')"""#not safe
with open('password.txt','r') as f:#password.txt contains your encrypted password
    password=f.read()
server.login('yourmail@gmail.com',password)
msg=MIMEMultipart()
msg['From']='your_name'
msg['To']='any_email@gmail.com'
msg['Subject']='A TEST'
with open('Mail_content.txt','r') as f:
    message=f.read()
msg.attach(MIMEText(message,'plain'))

#optional image add
"""
filename = 'message.jpg'
attachment =open(filename,'rb') #for reading bytes
p=MIMEBase('application','octet)
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment;filename={filename}')
msg.attach(p)
text=mesg.as_string()
server.sendmail('your_mail@gmail.com','other_mail@gmail.com',text)
"""

