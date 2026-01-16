# Step 1: Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Step 2: Load Dataset
data = pd.read_csv("phishing.csv")

# Step 3: Separate Features and Target
X = data.drop("is_phishing", axis=1)
y = data["is_phishing"]

# Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Create Logistic Regression Model
model = LogisticRegression()

# Step 6: Train the Model
model.fit(X_train, y_train)

# Step 7: Make Predictions
y_pred = model.predict(X_test)

# Step 8: Evaluate Model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 9: Test with New URL Data
new_url = np.array([[100, 0, 1, 1]])  # Example phishing URL
prediction = model.predict(new_url)

if prediction[0] == 1:
    print("⚠️ Phishing Website Detected")
else:
    print("✅ Legitimate Website")
