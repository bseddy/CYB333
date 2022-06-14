
# Import the simple mail transfer protocol library module required for email functions and the
# ssl module for transport layer security / secure socket layer functions as gmail requires encryption.
import smtplib
import ssl

# Imports only the EmailMessage Function from the email.message module to define our email structure
# This reduces resources loaded into memory and allows for efficiency (no need for email.message.EmailMessage)
from email.message import EmailMessage

# Define sender and receiver email addresses
sender = 'cyb333donotreply@gmail.com'
receiver = 'cyb333iateam@gmail.com'

# Define the 16 character authentication key required by Google (This would not be needed for organizations with their
# own Exchange/SMTP server.
gmailauth = 'lckqasrkrdkczvxr'

# Define the email subject and body - used triple quotes for body to span multiple lines for text aesthetics.
subject = 'Logon Failure Audit Detected!'
body = """
***AUTOMATED - Do Not Reply!***

Sent to CYB333 Information Assurance Team.

Logon Failure Audit Detected -

Please review, archive, clear, and take appropriate action.
"""

# Defines the variable for the EmailMessage() function which has core functionality in modifying the structure of a
# message. This function allows us to put all the parts of an email together into one variable.
email = EmailMessage()
email['From'] = sender
email['To'] = receiver
email['Subject'] = subject
email.set_content(body)

# Defines variable for a helper function needed for network encryption using python defined default settings.
context = ssl.create_default_context()


# Added exception handling in which a connection attempt to the SMTP server is made, if a connection is not made then
# a message is prompted to check connection.
try:
    # Defines the instance in which connection is made. (host, port, previously defined SSL context)
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
    # Uses the previously defined SMTP connection settings, attempts login using sender address and authentication key.
    smtp.login(sender, gmailauth)
    # Uses the previously defined SMTP connection settings to send the email to the destination address.
    smtp.sendmail(sender, receiver, email.as_string())

except:
    input("""Unable to establish connection to SMTP server!
Check connection!
Press ENTER to exit""")
