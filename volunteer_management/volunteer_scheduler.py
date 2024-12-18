import smtplib
from email.mime.text import MIMEText

def send_volunteer_invitation(volunteer_email, event_details):
    msg = MIMEText(f"Dear Volunteer,\n\nWe are excited to invite you to our upcoming event: {event_details}.\n\nThank you for your support!")
    msg['Subject'] = "Volunteer Invitation"
    msg['From'] = "noreply@nonprofit.org"
    msg['To'] = volunteer_email

    with smtplib.SMTP('smtp.mailtrap.io', 2525) as server:
        server.login("YOUR_SMTP_USERNAME", "YOUR_SMTP_PASSWORD")
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
