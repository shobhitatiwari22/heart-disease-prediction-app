import streamlit as st
import pickle
import pandas as pd
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="Interactive Heart Predictor", page_icon=":heart:", layout="centered")
st.title("Live Heart Disease Risk Predictor")
st.image("https://img.freepik.com/premium-photo/pretty-realistic-heart-illustration-with-isolated-background_742252-4140.jpg?w=2000", width=50)
st.write("Move any slider or change any value below. The risk calculation updates instantly!")

# 2. Load the Saved Model
@st.cache_resource
def load_model():
    with open('heart_disease_model.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

# 3. Create Input Forms arranged in Columns
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age (years)", 20, 90, 54)
    sex = st.selectbox("Sex", options=[1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
    cp = st.selectbox("Chest Pain Type (cp)", options=[0, 1, 2, 3], format_func=lambda x: f"Type {x}")
    trestbps = st.slider("Resting Blood Pressure (trestbps)", 90, 200, 130)
    chol = st.slider("Serum Cholesterol (chol)", 100, 450, 240)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", options=[0, 1], format_func=lambda x: "True" if x == 1 else "False")

with col2:
    restecg = st.selectbox("Resting Electrocardiographic Results (restecg)", options=[0, 1, 2])
    thalach = st.slider("Maximum Heart Rate Achieved (thalach)", 60, 220, 150)
    exang = st.selectbox("Exercise Induced Angina (exang)", options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
    oldpeak = st.slider("ST Depression (oldpeak)", 0.0, 6.0, 1.0, step=0.1)
    slope = st.selectbox("Slope of Peak Exercise ST Segment (slope)", options=[0, 1, 2])
    ca = st.selectbox("Number of Major Vessels Colored (ca)", options=[0, 1, 2, 3, 4])
    thal = st.selectbox("Thalassemia Type (thal)", options=[0, 1, 2, 3])

# 4. Instant Live Processing (No Button Required)
input_df = pd.DataFrame([{
    'age': age, 'sex': sex, 'cp': cp, 'trestbps': trestbps, 'chol': chol,
    'fbs': fbs, 'restecg': restecg, 'thalach': thalach, 'exang': exang,
    'oldpeak': oldpeak, 'slope': slope, 'ca': ca, 'thal': thal
}])

prediction = model.predict(input_df)
probability = model.predict_proba(input_df)[0][1] * 100

st.markdown("---")
st.subheader("📊 Live Assessment Result")

# Dynamic metric gauge summary
if prediction == 1:
    st.error(f"⚠️ **Heart Disease Risk Detected**")
    st.metric(label="Calculated Risk Probability", value=f"{probability:.1f}%")
    st.progress(int(probability))
else:
    st.success(f"✅ **No Heart Disease Risk Detected**")
    st.metric(label="Calculated Healthy Probability", value=f"{100 - probability:.1f}%")
    st.progress(int(100 - probability))
