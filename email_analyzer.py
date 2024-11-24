import pandas as pd
import re
import joblib
import os

# Function to preprocess email text
def preprocess_email(text):
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Define paths for input and output files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_CSV_PATH = os.path.join(BASE_DIR, 'emails.csv')  # Extracted emails file
OUTPUT_CSV_PATH = os.path.join(BASE_DIR, 'classified_emails.csv')  # Classified results file

try:
    # Load the phishing model and vectorizer
    MODEL_PATH = os.path.join(BASE_DIR, 'phishing_model.pkl')
    VECTORIZER_PATH = os.path.join(BASE_DIR, 'vectorizer.pkl')
    loaded_model = joblib.load(MODEL_PATH)
    loaded_vectorizer = joblib.load(VECTORIZER_PATH)

    # Load the extracted emails CSV file
    if not os.path.exists(INPUT_CSV_PATH):
        raise FileNotFoundError(f"Input CSV file not found: {INPUT_CSV_PATH}")
    
    emails_to_classify = pd.read_csv(INPUT_CSV_PATH)

    if 'email_text' not in emails_to_classify.columns:
        raise ValueError("Input CSV file does not have the required 'email_text' column.")

    # Preprocess the email text in the input CSV
    emails_to_classify['cleaned_text'] = emails_to_classify['email_text'].apply(preprocess_email)

    # Transform the cleaned emails into features using the saved vectorizer
    email_features = loaded_vectorizer.transform(emails_to_classify['cleaned_text']).toarray()

    # Predict phishing or legitimate emails
    predictions = loaded_model.predict(email_features)

    # Add predictions to the input data
    emails_to_classify['prediction'] = predictions
    emails_to_classify['prediction'] = emails_to_classify['prediction'].map({1: 'Phishing', 0: 'Legitimate'})  # Map labels

    # Save the results to a new CSV file
    emails_to_classify.to_csv(OUTPUT_CSV_PATH, index=False)

    print(f"Predictions saved to: {OUTPUT_CSV_PATH}")
    print("Sample Predictions:\n", emails_to_classify[['email_text', 'prediction']].head())

except FileNotFoundError as e:
    print(f"Error: {e}")

except ValueError as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
