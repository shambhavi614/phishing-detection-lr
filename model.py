import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
data = pd.read_csv("phishing.csv")

# Split features and target
X = data.drop("is_phishing", axis=1)
y = data["is_phishing"]

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save trained model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ Model trained and saved as model.pkl")
