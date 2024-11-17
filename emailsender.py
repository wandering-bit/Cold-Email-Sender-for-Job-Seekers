import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders as Encoders
from email.mime.text import MIMEText
import time
import threading

class EMAILSENDER:
    def __init__(self):

        self.client = smtplib.SMTP('smtp.gmail.com',587)

        self.client.starttls()
        self.data={}
        self.loader = threading.Thread(target=self.loading,daemon=False)
        self.loader.start()


    def login(self)->bool:
        reply = self.client.login("sranjansharma2001@gmail.com","yqsw babj efpf qist")
        if reply[1].decode('utf-8') == '2.7.0 Accepted':
            print(" Login Success")
            return True
        else:
            print(" Login Failed")
            return False

    def parseconfig(self)->dict:
        import yaml
        with open("config.yaml", 'r') as f:
            configdata = yaml.load(f, Loader=yaml.SafeLoader)
            self.data = configdata
            return self.data
    
    def form_mail(self):
        self.msg = MIMEMultipart()
        self.msg['Subject'] = self.data['subject']
        self.msg['From'] = self.data['email']

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(self.data["attachement"], "rb").read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{self.data["attachname"]}"')

        self.msg.attach(part)

        self.msg.attach(
        MIMEText(
            self.data["body"]
        ))

    def sendMail(self):
        for i in self.data['to']:

            self.load_flag=True
            Messenger.form_mail()
            self.msg['To']=i

            print('messege packet',self.msg['To'])

            print(" Sending mail to: ",i)

            print(self.client.send_message(self.msg))

            self.load_flag= False

            print(" Mail Sent")


    def loading(self):
        while True:
            print(".",end="-")
            time.sleep(1)

Messenger = EMAILSENDER()


Messenger.login()
Messenger.parseconfig()
Messenger.form_mail()
Messenger.sendMail()
