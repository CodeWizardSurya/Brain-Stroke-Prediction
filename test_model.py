import joblib
import pandas as pd
from pathlib import Path

def load_model_and_encoders():
    """Load the trained model and label encoders"""
    try:
        model = joblib.load('models/stroke_model.pkl')
        label_encoders = joblib.load('models/label_encoders.pkl')
        return model, label_encoders
    except FileNotFoundError:
        print("Error: Model files not found. Please train the model first.")
        exit(1)

def encode_categorical(input_df, label_encoders):
    """Encode categorical variables with handling for unseen labels"""
    for col in label_encoders:
        known_categories = set(label_encoders[col].classes_)
        input_df[col] = input_df[col].apply(
            lambda x: x if x in known_categories else 'Unknown'
        )
        input_df[col] = label_encoders[col].transform(input_df[col].astype(str))
    return input_df

def get_numeric_input(prompt, min_val=None, max_val=None):
    """Get numeric input with validation"""
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")

def get_choice_input(prompt, options):
    """Get choice input with numbered options"""
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = input("Enter choice (number): ")
            if choice.strip() == '0':  # Handle zero input for binary choices
                choice = '1'
            choice = int(choice)
            if 1 <= choice <= len(options):
                return options[choice-1]
            print(f"Please enter a number between 1 and {len(options)}")
        except ValueError:
            print("Please enter a valid number")

def get_user_input(label_encoders):
    """Collect user input for prediction"""
    print("\n" + "="*50)
    print("Stroke Risk Prediction - Enter Patient Details")
    print("="*50 + "\n")
    
    options = {
        'gender': ['Male', 'Female'],
        'ever_married': ['Yes', 'No'],
        'work_type': ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'],
        'Residence_type': ['Urban', 'Rural'],
        'smoking_status': ['never smoked', 'formerly smoked', 'smokes', 'Unknown']
    }
    
    data = {
        'gender': get_choice_input("Gender:", options['gender']),
        'age': get_numeric_input("Age: ", min_val=0, max_val=120),
        'hypertension': get_choice_input("Hypertension:", ['No (0)', 'Yes (1)']).split()[0],
        'heart_disease': get_choice_input("Heart Disease:", ['No (0)', 'Yes (1)']).split()[0],
        'ever_married': get_choice_input("Ever Married:", options['ever_married']),
        'work_type': get_choice_input("Work Type:", options['work_type']),
        'Residence_type': get_choice_input("Residence Type:", options['Residence_type']),
        'avg_glucose_level': get_numeric_input("Average Glucose Level (mg/dL): ", min_val=0),
        'bmi': get_numeric_input("BMI: ", min_val=0),
        'smoking_status': get_choice_input("Smoking Status:", options['smoking_status'])
    }
    
    data['hypertension'] = 1 if data['hypertension'] == 'Yes' else 0
    data['heart_disease'] = 1 if data['heart_disease'] == 'Yes' else 0
    
    input_df = pd.DataFrame([data])
    input_df = encode_categorical(input_df, label_encoders)
    
    return input_df

def predict_stroke_risk(model, input_data):
    """Make prediction using the trained model"""
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]
    
    print("\n" + "="*50)
    print("Prediction Result")
    print("="*50)
    
    if prediction[0] == 1:
        print(f"\n⚠️ This patient is at risk of stroke.")
    else:
        print(f"\n✅ This patient is not at risk of stroke.")

def main():
    model, label_encoders = load_model_and_encoders()
    input_data = get_user_input(label_encoders)
    predict_stroke_risk(model, input_data)

if __name__ == "__main__":
    main()