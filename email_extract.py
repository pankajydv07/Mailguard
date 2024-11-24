# import imaplib
# import email
# import yaml
# import csv
# import os

# # Define the path to save the output CSV
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# CSV_FILE_PATH = os.path.join(BASE_DIR, 'emails.csv')

# # Load credentials from the YAML file
# CREDENTIALS_FILE = os.path.join(BASE_DIR, "credentials.yml")
# with open(CREDENTIALS_FILE) as f:
#     content = f.read()

# # Extract username and password
# my_credentials = yaml.load(content, Loader=yaml.FullLoader)
# user, password = my_credentials["user"], my_credentials["password"]

# # URL for IMAP connection
# imap_url = 'imap.gmail.com'

# try:
#     # Connect to Gmail using SSL
#     my_mail = imaplib.IMAP4_SSL(imap_url)

#     # Log in using credentials
#     my_mail.login(user, password)

#     # Select the Inbox folder
#     my_mail.select('Inbox')

#     # Define Key and Value for email search
#     key = 'FROM'  # Search emails from a specific sender
#     value = 'cr-cs@srmap.edu.in'  # Replace this with the desired sender's email
#     _, data = my_mail.search(None, key, value)  # Search for emails

#     mail_id_list = data[0].split()  # Get the list of email IDs

#     # List to store the extracted text from email bodies
#     email_texts = []

#     # Iterate through messages and extract the body
#     for num in mail_id_list:
#         typ, data = my_mail.fetch(num, '(RFC822)')  # Fetch the full email content
#         for response_part in data:
#             if isinstance(response_part, tuple):
#                 my_msg = email.message_from_bytes(response_part[1])
#                 for part in my_msg.walk():
#                     if part.get_content_type() == 'text/plain':  # Extract plain text content
#                         email_texts.append(part.get_payload(decode=True).decode())  # Decode and append

#     # Save the extracted email bodies into a CSV file with a placeholder label
#     with open(CSV_FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(["email_text", "label"])  # Header
#         for text in email_texts:
#             writer.writerow([text, "unknown"])  # Write each email body as a row with placeholder label

#     print(f"Emails saved to {CSV_FILE_PATH}.")

# except imaplib.IMAP4.error as e:
#     print(f"IMAP connection error: {e}")

# except Exception as e:
#     print(f"An error occurred: {e}")



import imaplib
import email
import yaml
import csv
import os

# Define the path to save the output CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_PATH = os.path.join(BASE_DIR, 'emails.csv')

# Load credentials from the YAML file
CREDENTIALS_FILE = os.path.join(BASE_DIR, "credentials.yml")
try:
    with open(CREDENTIALS_FILE) as f:
        content = f.read()
    # Extract username and password
    my_credentials = yaml.load(content, Loader=yaml.FullLoader)
    user, password = my_credentials["user"], my_credentials["password"]
except Exception as e:
    print(f"Error reading credentials: {e}")
    exit()

# URL for IMAP connection
imap_url = 'imap.gmail.com'

try:
    # Connect to Gmail using SSL
    my_mail = imaplib.IMAP4_SSL(imap_url)

    # Log in using credentials
    my_mail.login(user, password)

    # Select the Inbox folder
    my_mail.select('Inbox')

    # Define Key and Value for email search
    key = 'FROM'  # Search emails from a specific sender
    value = 'cr-cs@srmap.edu.in'  # Replace this with the desired sender's email
    _, data = my_mail.search(None, key, value)  # Search for emails

    mail_id_list = data[0].split()  # Get the list of email IDs

    if not mail_id_list:
        print("No emails found from the specified sender.")
        exit()

    # List to store the extracted text from email bodies
    email_texts = []

    # Iterate through messages and extract the body
    for num in mail_id_list:
        typ, data = my_mail.fetch(num, '(RFC822)')  # Fetch the full email content
        for response_part in data:
            if isinstance(response_part, tuple):
                my_msg = email.message_from_bytes(response_part[1])
                for part in my_msg.walk():
                    if part.get_content_type() == 'text/plain':  # Extract plain text content
                        email_texts.append(part.get_payload(decode=True).decode())  # Decode and append

    # Check if any emails were extracted
    if not email_texts:
        print("No email text found.")
        exit()

    # Save the extracted email bodies into a CSV file with a placeholder label
    with open(CSV_FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["email_text", "label"])  # Header
        for text in email_texts:
            writer.writerow([text, "unknown"])  # Write each email body as a row with placeholder label

    print(f"Emails saved to {CSV_FILE_PATH}.")

except imaplib.IMAP4.error as e:
    print(f"IMAP connection error: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
