import smtplib
import random
import string

# Function to generate a random reset code
def generate_reset_code(length=8):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# Function to send a password reset email
def send_password_reset_email(email, reset_code):
    # Replace these with your email server's details
    smtp_server = 'your_smtp_server.com'
    smtp_port = 587
    smtp_username = 'your_email@example.com'
    smtp_password = 'your_password'

    # Create the email message
    subject = "Password Reset"
    message = f"Hello,\n\nTo reset your password, please use the following code: {reset_code}\n\nBest regards,\nYour App Team"

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        from_email = smtp_username
        to_email = email
        server.sendmail(from_email, to_email, f"Subject: {subject}\n\n{message}")

# Example usage
if __name__ == "__main__":
    email = "user@example.com"
    reset_code = generate_reset_code()

    # Save the reset code to a database or storage
    # You'd typically associate it with the user's email address

    send_password_reset_email(email, reset_code)
    print("Password reset email sent.")
