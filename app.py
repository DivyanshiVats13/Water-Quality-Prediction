cd Downloads/Div's project
git init
git remote add origin https://github.com/DivyanshiVats13/Water-Quality-Prediction.git
git branch -M main
git add .
git commit -m "Initial project upload"
git push -u origin main

from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model & scaler
model = pickle.load(open("water_xgb_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read all 20 feature values from form input
        features = [
            float(request.form.get(key)) for key in request.form.keys()
        ]

        # Convert to numpy array
        final_features = np.array(features).reshape(1, -1)

        # Scale input
        final_scaled = scaler.transform(final_features)

        # Predict
        prediction = model.predict(final_scaled)[0]

        result = "Safe to Drink 💧" if prediction == 1 else "Not Safe ❌"

        return render_template("index.html", result=result)

    except Exception as e:
        return render_template("index.html", result="Error: Invalid input")

if __name__ == "__main__":
    # Local development server
    app.run(debug=True, host="127.0.0.1", port=5000)
