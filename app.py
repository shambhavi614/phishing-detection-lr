from flask import Flask, render_template, request, jsonify
import pickle
from feature_extraction import extract_features

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    url = request.json["url"]
    features = extract_features(url)
    prediction = model.predict([features])[0]

    return jsonify({
        "result": "Phishing Website ⚠️" if prediction == 1 else "Legitimate Website ✅"
    })

if __name__ == "__main__":
    app.run(debug=True)
