from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
loaded_data = joblib.load('prediction_model.joblib')
model = loaded_data["model"]
threshold = loaded_data["threshold"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Input data in the same order as training
        features = [
            request.form['Gender'], # drop-down list
            float(request.form['Age']),  # number
            int(request.form['Hypertension']), # no/yes - 0/1
            int(request.form['Heart_disease']), # no/yes - 0/1
            int(request.form['Ever_married']), # no/yes - 0/1
            request.form['Work_type'], # drop-down list
            int(request.form['From_urban_area']), # no/yes - 0/1
            float(request.form['Avg_glucose']),  # number
            float(request.form['BMI']),  # number
            request.form['Smoking_status'] # drop-down list
        ]
        
        # User entered df with the same names of features as training
        df = pd.DataFrame([features], columns=[
            'Gender', 'Age', 'Hypertension', 'Heart disease', 'Ever married',
            'Work type', 'From urban area', 'Avg. glucose (mg/dL)', 'BMI', 'Smoking status'
        ])
        
        # Get the predicted probabilities
        proba = model.predict_proba(df)[:, 1]  # 1 is poss class

        # Use threshold to make the final decision
        prediction = 1 if proba[0] >= threshold else 0
        
        # Return result to web interface
        return render_template('index.html', prediction=prediction)
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
