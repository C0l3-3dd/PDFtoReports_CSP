# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance

 
def senMail(mensaje):
    msg = MIMEMultipart()
    message = mensaje

    # setup the parameters of the message
    password = "50P0RT3T3C"
    msg['From'] = "correo.pruebas.bat@gmail.com"
    msg['To'] = "edd.god19@gmail.com"
    msg['Subject'] = "Consorcio San Pablo - Generador de Excel"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)


    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    #print ("successfully sent email to %s:" % (msg['To']))