
# Import the simple mail transfer protocol library module required for email functions and the
# ssl module for transport layer security / secure socket layer functions as gmail requires
# encryption for security.
import smtplib
import ssl

# Imports only the EmailMessage Function from the email.message module to define our email structure
from email.message import EmailMessage

# ****DETECT AUTHENTICATION FAILURE SECTION****

# Open the specified authentication log file and assign the alias "authlog". Then look for the keywords "authentication
# failure in the authentication log. If found then continue with code to send email, otherwise quit.
# ***NOTE*** This code will work only in Linux distributions that have the authentication log in the /var/log/
# directory. If using a distro such as RHEL this directory will need to be modified to ensure successful execution!
with open('/var/log/auth.log') as authlog:
    if 'authentication failure' in authlog.read():
        print('AUTHENTICATION FAILURE DETECTED!! BEEP BOOP!')
        print()

# ****SEND EMAIL SECTION****

        # Define sender and received email addresses
        sender = 'cyb333donotreply@gmail.com'
        receiver = 'cyb333iateam@gmail.com'

        # Define the 16 character authentication key required by Google (This would not be needed for organizations
        # with their own Exchange/SMTP server.
        gmailauth = 'lckqasrkrdkczvxr'

        # Define the email subject and body - used triple quotes for body to span multiple lines for text aesthetics.
        subject = 'Logon Failure Detected!'
        body = """
        ***AUTOMATED - DO NOT REPLY!***

        This e-mail has been sent to the CYB333 Information Assurance Team / System Administrators.

        Logon Failure Detected!

        Please review the authentication log, take appropriate action, then truncate.
        """

        # Defines the variable for the EmailMessage() function which has core functionality in modifying
        # the structure of a message. This function allows us to put all the parts of an email together.
        email = EmailMessage()
        email['From'] = sender
        email['To'] = receiver
        email['Subject'] = subject
        email.set_content(body)

        # Defines variable for a helper function needed for network encryption using python defined default settings.
        context = ssl.create_default_context()


        # Added exception handling in which an attempt to connect to the SMTP server is made, if a connection is not made
        # then a message is prompted to check connection.
        try:
            # Defines the instance in which the connection will be made. (host, port, previously defined SSL context)
            smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
            # Uses the previously define SMTP connection settings attempts login using the defined sender address and
            # authentication key
            smtp.login(sender, gmailauth)
            # Uses the previously defined SMTP connection settings to send the email to the destination address
            smtp.sendmail(sender, receiver, email.as_string())
            input('System Adminsitrators notified! Press ENTER to close.')

        # If a connection is not made, inform the user.
        except:
            input("""Unable to establish connection to SMTP server! 
        Check connection!
        Press ENTER to exit""")
    # If an "authentication failure" is not found in auth.log, inform user, then quit.
    else:
        input('No authentication failures at this time. Press ENTER to acknowledge this message.')
        quit()
