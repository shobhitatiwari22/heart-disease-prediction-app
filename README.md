## ❤️ Machine Learning-Driven Heart Disease Risk Predictor


## 📌 Project Overview

This project is a live, machine learning-driven web app that predicts heart disease risk in real time. Using an optimized Random Forest classifier trained on clinical patient data, it analyzes 13 key health biomarkers—like chest pain type and max heart rate—to provide instant, data-backed diagnostic risk assessments through a clean user interface.

## 🎯 ObjectivePredictive Automation
To develop a highly accurate classification pipeline capable of identifying heart disease risks from non-invasive clinical tests.

**Zero-Latency Inference**: To construct a fast, button-free user experience where sliding health parameters instantly recalculates diagnosis metrics.

**Explainable AI**: To understand and map which specific medical conditions (like heart rate or chest pain indices) influence algorithmic decisions the most.

## 🛠️ Technologies UsedProgramming Core

**Python 3.11Web Framework**: Streamlit

**Machine Learning Library** : Scikit-Learn (Model Selection, Training Pipelines, Metrics Evaluation)

**Data Manipulation**: Pandas, NumPyData Visualization: Seaborn, Matplotlib (Correlation Matrices, Distribution Plots)

**Model Preservation**: Pickle (Binary Model Serialization)

## 📊 Dataset Information

The underlying predictive engine is trained on a standardized cardiovascular study dataset comprising 302 patient records mapped across 13 distinct feature columns and 1 binary class target variable

## 🧬 Predictive Features

**age**: Age of the patient in years.

**sex**: Biological sex (1 = Male, 0 = Female).

**cp**: Chest pain type experienced (0 = Typical Angina, 1 = Atypical Angina, 2 = Non-anginal pain, 3 = Asymptomatic).

**trestbps**: Resting blood pressure in mm Hg on admission to the hospital.

**chol**: Serum cholesterol level in mg/dl.

**fbs**: Fasting blood sugar level > 120 mg/dl (1 = True, 0 = False).

**restecg**: Resting electrocardiographic results (0 = Normal, 1 = ST-T wave abnormality, 2 = Showing left ventricular hypertrophy).

**thalach**: Maximum heart rate achieved during exercise stress testing.

**exang**: Exercise-induced angina pectoris (1 = Yes, 0 = No).

**oldpeak**: ST depression induced by exercise relative to rest states.

**slope**: The slope of the peak exercise ST segment.

**ca**: Number of major blood vessels (0–3) colored by fluoroscopy.

**thal**: Thalassemia disorder indicator (1 = Fixed defect, 2 = Normal, 3 = Reversible defect).

## 🎯 Target Label

**target**: Heart disease status (0 = No Disease / Low Risk, 1 = Disease Detected / High Risk).

## 🤖 Machine Learning Model  

During the design phase, models were trained on an 80/20 train-test data split and exhaustively benchmarked:

**Logistic Regression**: Achieved 80.33% test accuracy.

**Random Forest Classifier**: Achieved 83.61% test accuracy.

## 🛡️ Diagnostic Metrics & Feature Importance

**Confusion Matrix**: Evaluated 61 unknown patient samples, registering 51 absolute correct predictions and minimizing dangerous false-negative errors.

**Top Clinical Predictors**: Feature extraction proved that ca (vessels colored by fluoroscopy) and thalach (maximum heart rate) carry the highest mathematical weight when forecasting a patient's risk profile.

## ⚡ Key FeaturesLive Reactive Loop

Eliminates traditional "Submit" forms; changing a slider updates the backend model calculation and changes UI elements instantly.

**Color-Coded Status Frames**: Implements dynamic alert notifications (st.error for high risk, st.success for clean status) based on the classifier's diagnosis.

**Confidence Progress Gauges**: Utilizes animated progress indicator bars (st.progress) to present prediction certainty clearly to end-users.

**Balanced Dual-Column Interface**: Cleanly splits 13 clinical variables across a symmetric two-column responsive layout layout.

📷 **Application Screenshot:**

<a href="https://heart-disease-prediction-app-9nuhun3s2w2ngaqnecnmhx.streamlit.app/" target="_blank">
<img width="1600" height="779" alt="image" src="https://github.com/user-attachments/assets/d76e0728-9566-4984-a976-7e778d101e2f" />
</a>

## Result:

<a href="https://heart-disease-prediction-app-9nuhun3s2w2ngaqnecnmhx.streamlit.app/" target="_blank">
<img width="1600" height="779" alt="image" src="https://github.com/user-attachments/assets/a43b8e03-3d02-4a31-9664-c3752cf6bdbf" />
</a>
