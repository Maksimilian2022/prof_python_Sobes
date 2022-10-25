import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mail_work():
    gmail_smtp = "smtp.gmail.com"
    gmail_imap = "imap.gmail.com"

    login = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    header = None


    def send_message(self):
        masage = MIMEMultipart()
        masage['From'] = self.login
        masage['To'] = ', '.join(self.recipients)
        masage['Subject'] = self.subject
        masage.attach(MIMEText(self.message))

        mas = smtplib.SMTP(self.gmail_smtp, 587)
        # identify ourselves to smtp gmail client
        mas.ehlo()
        # secure our email with tls encryption
        mas.starttls()
        # re-identify ourselves as an encrypted connection
        mas.ehlo()

        mas.login(self.login, self.password)
        mas.sendmail(self.login, mas, masage.as_string())

        mas.quit()
        #send end


    #recieve
    def receive(self):
        mail = imaplib.IMAP4_SSL(self.gmail_smtp)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        #end recieve


if __name__ == '__main__':
    new_mail = Mail_work()
