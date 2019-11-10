"""
by ganesh khadanga 
date :-24-04-2019
"""
import smtplib, ssl



print("________welcome to python gmail by ganesh khadanga__________")



print("there may be error due to gmail security . you can goto  :: accounts > security > eneable for less secure applicatons :: to solve the error ")


port = 465  # port For SSL
smtp_server = "smtp.gmail.com"
sender_email = input("enter your email address:"  )

password = input("Type your password and press enter: ")

receiver_email = input("enter receivers email address:")


message = input("enter your message :")

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
        