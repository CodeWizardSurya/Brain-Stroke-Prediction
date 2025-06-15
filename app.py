from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load model and encoders
try:
    model = joblib.load('models/stroke_model.pkl')
    label_encoders = joblib.load('models/label_encoders.pkl')
except:
    model = None
    label_encoders = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or label_encoders is None:
        return render_template('result.html', prediction="Model not loaded. Please train the model first.")
    
    try:
        # Get form data (now including gender)
        form_data = {
            'gender': request.form['gender'],
            'age': float(request.form['age']),
            'hypertension': int(request.form.get('hypertension', 0)),
            'heart_disease': int(request.form.get('heart_disease', 0)),
            'ever_married': request.form['ever_married'],
            'work_type': request.form['work_type'],
            'Residence_type': request.form['Residence_type'],
            'avg_glucose_level': float(request.form['avg_glucose_level']),
            'bmi': float(request.form['bmi']),
            'smoking_status': request.form['smoking_status']
        }
        
        # Convert to dataframe
        input_data = pd.DataFrame([form_data])
        
        # Encode categorical fields (including gender)
        categorical_fields = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
        for field in categorical_fields:
            le = label_encoders[field]
            input_data[field] = le.transform(input_data[field].astype(str))
        
        # Reorder columns to match training data
        columns_order = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
                        'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status']
        input_data = input_data[columns_order]
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Prepare result
        result = "Affected by Stroke" if prediction[0] == 1 else "Not Affected by Stroke"
        
        return render_template('result.html', prediction=result)
    
    except Exception as e:
        return render_template('result.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    os.makedirs('models', exist_ok=True)
    app.run(debug=True)