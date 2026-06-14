import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

# Train model directly
df = pd.read_csv('data.csv')
X = df[['age', 'monthly_salary', 'job_satisfaction',
        'years_at_company', 'work_life_balance',
        'promotions_last_3years']]
y = df['left']
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Page title
st.title("Employee Attrition Predictor")
st.write("Enter employee details to predict if they are at risk of leaving.")

# Input fields
age = st.number_input("Age", min_value=18, max_value=65, value=30)
salary = st.number_input("Monthly Salary (Rs)", min_value=10000, max_value=200000, value=35000)
satisfaction = st.slider("Job Satisfaction (1=Low, 4=High)", 1, 4, 2)
years = st.number_input("Years at Company", min_value=0, max_value=40, value=3)
balance = st.slider("Work Life Balance (1=Low, 4=High)", 1, 4, 2)
promotions = st.number_input("Promotions in Last 3 Years", min_value=0, max_value=5, value=0)

# Predict button
if st.button("Predict"):
    input_data = pd.DataFrame([[age, salary, satisfaction, years, balance, promotions]],
                              columns=['age', 'monthly_salary', 'job_satisfaction',
                                       'years_at_company', 'work_life_balance',
                                       'promotions_last_3years'])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ HIGH RISK — This employee is likely to leave")
        st.write(f"Probability of leaving: {probability * 100:.0f}%")
    else:
        st.success(f"✅ LOW RISK — This employee is likely to stay")
        st.write(f"Probability of leaving: {probability * 100:.0f}%")