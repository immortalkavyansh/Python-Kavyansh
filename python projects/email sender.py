import smtplib
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kavimaheshwari609@gmail.com', '#kavyansh@321')
    server.sendmail('kavimahehswari609@gmail.com', to, content)
    server.close()
try:
    var = input("To whom do you want to send the email\n")
    var1 = input("What is the content do you want to send\n")
    content = f"{var}"
    to = f"{var1}"
    sendEmail(to, content)
    print("Email has been sent to", to)

except Exception as error:
    print(error)
    print("Sorry sir because of some problem, email has not send")


