import smtplib
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/submit/<name>/<number>/<location>/<email>", methods=['GET'])
def sendEmail(name, number, location, email):
    message = "\r\n".join([
        "Subject: User Details",
        "",
        "name : " + name + ", number : " + number + ", location : " + location + ", email : " + email
    ])
    dowWork(message)
    return "success"


def dowWork(message):
    fromEmail = ''
    toEmail = ''
    username = ''
    password = ''
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromEmail, toEmail, message)
    server.quit()


if __name__ == "__main__":
    app.run()
