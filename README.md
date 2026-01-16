🔐 Phishing Website Detection using Logistic Regression
Project Overview

This project implements a machine learning-based phishing website detection system using Logistic Regression. The system analyzes URLs and predicts whether a website is legitimate or phishing based on features extracted from the URL.

Phishing attacks are one of the most common cyber threats, targeting users’ sensitive information like login credentials, banking information, and personal data. This system helps detect phishing attempts before users interact with malicious websites.

🚀 Features

Real-time URL analysis

Supervised machine learning using Logistic Regression

URL-based feature extraction:

URL length

Presence of HTTPS

Presence of IP address

Number of dots (.) in URL

Suspicious keywords (login, verify, secure, account, bank)

Presence of @ symbol

Interactive web interface (HTML + CSS + JavaScript / or Streamlit)

Accurate predictions on standard phishing datasets

🛠 Tech Stack
Layer	Technology / Library
Backend	Python
Machine Learning	scikit-learn (Logistic Regression)
Frontend	HTML, CSS, JavaScript / Streamlit
Utilities	pandas, numpy, joblib
📂 Project Structure
phishing-detection-logistic-regression/
│
├── server.py                # Flask backend for ML API
├── feature_extraction.py    # URL feature extraction logic
├── train_model.py           # Train Logistic Regression model
├── phishing_lr_model.pkl    # Trained model (optional, not uploaded to GitHub)
├── requirements.txt         # Python dependencies
├── README.md
├── templates/
│   └── index.html           # Frontend HTML
└── static/
    ├── style.css            # CSS for frontend
    └── app.js               # JavaScript frontend logic

📈 How It Works

User enters a URL on the website interface.

Feature extraction module extracts important URL features.

Features are fed into the Logistic Regression model.

The model predicts:

0 → Legitimate Website

1 → Phishing Website

Result is displayed to the user in real-time.

▶️ How to Run Locally
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Train the Logistic Regression model (if model file is not provided)
python train_model.py

3️⃣ Run Flask backend
python server.py

4️⃣ Open browser
http://127.0.0.1:5000

5️⃣ Enter a URL and check phishing detection
📊 Sample URLs for Testing

Legitimate URLs:

https://www.google.com
https://www.amazon.com
https://www.github.com


Phishing-like URLs:

http://secure-login-paypal.com
http://verify-account-bank.com
http://login-facebook-security.net

🎯 Model Details

Algorithm: Logistic Regression

Supervised Learning: Classification

Key Features: URL length, HTTPS, IP address, suspicious keywords, @ symbol

Accuracy: ~88–90% on standard phishing datasets
