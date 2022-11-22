import smtplib
import email.message
from lost import senha
from lost import token

#email = input("Email: ")
#print(email)

def enviar_email():  
    corpo_email = f"Token: {token}"

    msg = email.message.Message()
    msg['Subject'] = "Token de acesso"
    msg['From'] = 'fronttier.server@gmail.com'
    msg['To'] = input("Email: ")
    password =  senha
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()