Here’s a `README.md` file template that explains your project, the steps involved in the setup, and the process of email extraction and analysis:

---

# Mailguard

Mailguard is a Python-based tool that extracts emails from a specified Gmail account and analyzes them to classify emails as **phishing** or **legitimate** using a pre-trained machine learning model.

## Features
- **Email Extraction**: Connects to a Gmail account using IMAP to fetch emails based on specific search criteria.
- **Email Analysis**: Analyzes extracted emails for phishing content using a machine learning model.
- **Frontend Interface**: A Flask-based web application that allows users to input credentials, extract emails, and view results in a structured table.

---

## Project Structure
```
Mailguard/
├── classified_emails.csv    # Output file containing classified emails
├── credentials.yml          # Stores email credentials (auto-generated)
├── email_analyzer.py        # Script for analyzing emails
├── email_extract.py         # Script for extracting emails from Gmail
├── emails.csv               # Intermediate file containing extracted emails
├── phishing_model.pkl       # Pre-trained model for phishing detection (not uploaded)
├── vectorizer.pkl           # Saved vectorizer for preprocessing text (not uploaded)
├── app.py                   # Flask application for user interaction
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---
## Important : We could not upload our phising_model.pkl due to its large size.
 Here is the link: https://drive.google.com/file/d/1Y_epwWX7fbufkHq9ooOO4dIpAlXcH_Hf/view?usp=sharing



## Requirements
- Python 3.8 or higher
- Gmail account with [App Password](https://support.google.com/accounts/answer/185833?hl=en)
- Required libraries (see `requirements.txt`):
  - Flask
  - Pandas
  - scikit-learn
  - PyYAML
  - IMAPClient
  - joblib

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Mailguard.git
   cd Mailguard
   ```

2. **Install Dependencies**:
   Use the `requirements.txt` file to install all necessary dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. **Place the Pre-trained Model**:
   Download the `phishing_model.pkl` and `vectorizer.pkl` files and place them in the project directory.

4. **Run the Flask Application**:
   ```bash
   python app.py
   ```

5. **Access the Web App**:
   Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Usage Workflow

### Step 1: Email Extraction
- Log in using your Gmail email and app password via the web app.
- The `email_extract.py` script:
  1. Connects to Gmail using the IMAP protocol.
  2. Searches for emails based on predefined criteria (e.g., sender email address).
  3. Extracts the plain text content of each email and saves it in `emails.csv`.

### Step 2: Email Analysis
- After emails are extracted, the `email_analyzer.py` script:
  1. Preprocesses the extracted email content by removing HTML tags, URLs, special characters, and converting to lowercase.
  2. Uses the pre-trained model and vectorizer to predict whether each email is phishing (1) or legitimate (0).
  3. Saves the predictions in `classified_emails.csv`.

### Step 3: Viewing Results
- The results are displayed in a table on the "Results" page of the web app.

---

## Example Workflow

1. **Login**:
   Enter your Gmail email and app password on the home page of the app.

2. **Email Extraction**:
   Emails are fetched from your inbox based on the specified search criteria (e.g., sender address).

3. **Email Analysis**:
   Extracted emails are analyzed, and a phishing classification report is generated.

4. **Results**:
   Visit the "Results" page to view the phishing classifications for each email.

---

## Notes
- **Security**: Ensure your Gmail account has [App Passwords](https://support.google.com/accounts/answer/185833?hl=en) enabled. Avoid using your primary account password.
- **Custom Criteria**: Update `email_extract.py` to change the email search criteria (e.g., different sender, subject).

---

## Example Output
### Classified Emails (`classified_emails.csv`)
| Email Text                                | Prediction |
|-------------------------------------------|------------|
| "Update your account details immediately" | 1          |
| "Welcome to our platform!"                | 0          |

- **1**: Phishing
- **0**: Legitimate

---

## Troubleshooting
1. **Email Extraction Issues**:
   - Ensure your Gmail account has IMAP enabled ([Gmail IMAP Settings](https://support.google.com/mail/answer/7126229?hl=en)).
   - Verify the sender email address specified in `email_extract.py`.

2. **Model/Vectorizer Missing**:
   - Ensure the `phishing_model.pkl` and `vectorizer.pkl` files are present in the project directory.

3. **App Not Running**:
   - Ensure Flask is installed and all dependencies are satisfied (`pip install -r requirements.txt`).

---

## License
This project is licensed under the [MIT License](LICENSE).

---

You can copy this `README.md` template, customize the repository URL, and adjust details to fit your specific project setup. Let me know if you need further clarification!
