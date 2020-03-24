import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask,request

app = Flask(__name__)

@app.route('/',methods=["POST"])
def sending():
    
    mail_content = '''
    <html>
        <head></head>
        <body>
            <p>Hi!<br>How are you?<br>
            Here is the <a href="http://www.python.org">link</a> you wanted.</p>
        </body>
    </html>
    '''
    
    #The mail addresses and password
    sender_address = request.form['sender']
    sender_pass = request.form['password']
    receiver_address = request.form['receiver']

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = request.form['subject']
    
    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'html'))
    
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    return 'Mail Sent'


if __name__ == '__main__':
    app.run()
