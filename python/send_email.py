from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "dom.sebastiao.primeiro@gmail.com"
receiver_email = "dom.sebastiao.primeiro@gmail.com"
subject = "Test Email"
body = "This is a test email sent from Python."

# Create a MIMEText object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the body to the email
message.attach(MIMEText(body, "plain"))

# Attach the file
# attachment_file_path = "output.csv"
# attachment = open(attachment_file_path, "rb")

# # Create a MIMEBase object
# part = MIMEBase("application", "octet-stream")
# part.set_payload(attachment.read())

# # Encode the attachment
# encoders.encode_base64(part)

# # Set the filename in the header
# part.add_header("Content-Disposition", f"attachment; filename= {attachment_file_path}")

# # Attach the file to the email
# message.attach(part)

# # Close the file
# attachment.close()

# SMTP server configuration (for Gmail, you can use smtp.gmail.com)
smtp_server = "smtp.gmail.com"
smtp_port = 465
smtp_username = "dom.sebastiao.primeiro@gmail.com"
smtp_password = "fuckthenewworldorder"

# Create an SMTP connection
with smtplib.SMTP(smtp_server, smtp_port) as server:
    # Start the TLS connection (for secure communication)
    server.starttls()

    # Log in to the SMTP server
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully.")
