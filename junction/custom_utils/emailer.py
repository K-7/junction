import sendgrid
from junction.settings import SENDGRID_FROM_EMAIL, SENDGRID_EMAIL_USERNAME,SENDGRID_EMAIL_PASSWORD

class EmailEngine():
   
   ### SEND THE EMAIL BODY,SUBJECT,TO_ADDRESS AS list, CC EMAILS as list IN A DICTIONARY
    def send_email(self, content):    
        
        print content
        to_list = content['to_email']
        try:
            FROM_ADDRESS = content['from_email']
        except:
            FROM_ADDRESS = SENDGRID_FROM_EMAIL
        
        sg = sendgrid.SendGridClient(SENDGRID_EMAIL_USERNAME, SENDGRID_EMAIL_PASSWORD, raise_errors=True)
        message = sendgrid.Mail()
        
        message.add_to(to_list)
        message.set_subject(content['subject'])
        message.set_html(content['body'])
#         message.set_text(content.body)
        message.set_from(FROM_ADDRESS)
        try:
            cc_list = content['cc_email']
            message.add_bcc(cc_list)
        except:
            pass
        
        status, msg = sg.send(message)
      
        return status