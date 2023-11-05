import pickle
import streamlit as st

#membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#judul web
st.title('Mechine Learning Diabetes Detector')

col1, col2 = st.columns(2)

with col1:
    Pregnancies              = st.text_input('Input nilai Pregnancies')
with col1:
    Glucose                  = st.text_input('Input nilai Glucose')
with col1:
    BloodPressure            = st.text_input('Input nilai BloodPressure')
with col1:
    SkinThickness            = st.text_input('Input nilai SkinThickness')
with col2:
    Insulin                  = st.text_input('Input nilai Insulin')
with col2:
    BMI                      = st.text_input('Input nilai BMI')
with col2:
    DiabetesPedigreeFunction = st.text_input('Input nilai DiabetesPedigreeFunction')
with col2:
    Age                      = st.text_input('Input nilai Age')

# code untuk prediksi
diab_diagnosis = ''

# membuat tombo untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
    if (diab_prediction[0] == 1):
        diabetes_diagnosis = "Pasien terkena diabetes"     
    else:
        diabetes_diagnosis = "Pasien tidak terkena diabetes"
        
    st.success(diabetes_diagnosis)









st.caption('made with ❤️ by Syamsun Noor Fasha (c) 2023')
