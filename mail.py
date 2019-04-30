import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mail(email):
    login = "whateats@mail.ru"
    password = 'Kira4976476'
    url = 'smtp.mail.ru'
    toaddr = str(email)

    msg = MIMEMultipart()
    msg['Subject'] = 'Что поесть'
    msg['From'] = "whateats@mail.ru"
    body = 'Спасибо за feedback, в ближайшее время ваши пожеланию будут рассмотрены.'
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP_SSL(url, 465)
    server.login(login, password)
    server.sendmail(login, toaddr, msg.as_string())
    server.quit()


def mail_for_me(feedback, email=""):
    login = "whateats@mail.ru"
    password = 'Kira4976476'
    url = 'smtp.mail.ru'
    toaddr = "whateats@mail.ru"

    msg = MIMEMultipart()
    msg['Subject'] = 'Feedback'
    msg['From'] = "whateats@mail.ru"
    body = str(email) + "  " + str(feedback)
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP_SSL(url, 465)
    server.login(login, password)
    server.sendmail(login, toaddr, msg.as_string())
    server.quit()


