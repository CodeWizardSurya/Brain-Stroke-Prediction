# //modules 
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import joblib
from pathlib import Path

def train_model():
    # Load dataset
    data = pd.read_csv('data/stroke_data.csv')
    
    # Preprocessing
    def preprocess_data(df):
        # Handle missing values in bmi
        imputer = SimpleImputer(strategy='mean')
        df['bmi'] = imputer.fit_transform(df[['bmi']])
        
        # Convert categorical variables
        label_encoders = {}
        categorical_cols = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
        
        for col in categorical_cols:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            label_encoders[col] = le
        
        # Separate features and target
        X = df[['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
               'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status']]
        y = df['stroke']
        
        return X, y, label_encoders

    X, y, label_encoders = preprocess_data(data)

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Save model and encoders
    Path("models").mkdir(exist_ok=True)
    joblib.dump(model, 'models/stroke_model.pkl')
    joblib.dump(label_encoders, 'models/label_encoders.pkl')
    
    print("Model trained and saved successfully!")
    print("Features used:", list(X.columns))

if __name__ == '__main__':
    train_model()