import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule 
import time

def send_email():
    sender_email = "pravesh@vama.app"
    sender_password = "Pravesh7079@"
    
    recipients = ["sawan@vama.app","sambhavi@vama.app","amrit@vama.app"]
    
    subject = "Consult Feeedback Sheet Updated"
    body = "This is to inform you that Consult Feedback Sheet is updated.\n Please check the same here:\n https://docs.google.com/spreadsheets/d/1rBGg58YGuwYzwyxc6Mcqn9vQ_qv-erWSQYEQBTW4vcc/edit#gid=1746365222Astrologer\n Thanks & Regards \n Pravesh Roy"

    for recipient in recipients:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
                print(f"Email sent to {recipient}")
        except Exception as e:
            print(f"Failed to send email to {recipient}. Error: {e}")

# Schedule to send email every 1 Hours
schedule.every(1).hours.do(send_email)

# Run the scheduling loop
while True:
    schedule.run_pending()
    time.sleep(1)
