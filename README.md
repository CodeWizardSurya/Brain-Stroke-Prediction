# 🧠 Brain Stroke Prediction Project 🚑

## 📌 Overview

This project is a **Brain Stroke Prediction System** that uses machine learning to predict the likelihood of a stroke based on patient medical data. It includes data preprocessing, model training, console-based interaction, and a user-friendly web interface.

---

## ✨ Features

- 🧠 Predict stroke risk using trained ML models
- 📊 Data preprocessing and label encoding included
- 🖥️ Simple and responsive Flask-based web UI
- 💻 Console-based testing for model validation
- 📁 Clean project structure and modular code

---

## 🚀 Live Demo

👉 Try the app here:  
**[Brain Stroke Prediction Live](https://brain-stroke-prediction-ahro.onrender.com)**

> Note: Due to free hosting, the app may take a few seconds to load.

---

## 🛠️ Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/brain-stroke-prediction.git
cd brain-stroke-prediction
```

2. **(Optional) Create Virtual Environment**

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### 🧠 Train the Model

```bash
python train_model.py
```

### 💻 Run Console Interaction

```bash
python test_model.py
```

> This will allow you to interactively enter patient data in the terminal and see predictions.

### 🌐 Run the Web Application

```bash
python app.py
```

Then open your browser and go to:  
`http://127.0.0.1:5000`

---

## 🌐 Project Structure

```
.
├── app.py                 # Flask app to serve the web interface
├── train_model.py         # Script to train the machine learning model
├── test_model.py          # Console-based user input for model testing
├── requirements.txt       # Required Python libraries
├── data/
│   └── stroke_data.csv    # Dataset used for training
├── models/
│   ├── stroke_model.pkl   # Trained ML model
│   └── label_encoders.pkl # Encoders for categorical variables
├── static/                # CSS and static assets
├── templates/             # HTML templates
└── README.md              # This documentation file
```

---

## 🧰 Technologies Used

* Python 3.x 🐍  
* Flask 🌐  
* scikit-learn 📚  
* pandas, numpy 📈  

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 📬 Contact

If you have any queries or suggestions, feel free to contact:  
📧 **[surya.devgenius@gmail.com](mailto:surya.devgenius@gmail.com)**

---

Thank you for exploring this project! 🚀
