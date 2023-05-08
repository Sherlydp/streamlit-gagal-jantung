import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('Gagal_Jantung.sav', 'rb'))

st.title('Prediksi Penyakit Gagal Jantung')

col1, col2, col3 = st.columns(3)

with col1:age = st.number_input('Usia')
with col2:anaemia = st.number_input('Mengidap Anemia/tidak')
with col3:creatinine_phosphokinase = st.number_input('Tingkat serum kreatinin dalam daraha')
with col1:diabetes = st.number_input('Diabetes')
with col2:ejection_fraction = st.number_input('Persentase darah yang meninggalkan jantung pada setiap kontraksi ')
with col3:high_blood_pressure = st.number_input('Tekanan darah tinggi')
with col1:platelets = st.number_input('Trombosit')
with col2:serum_creatinine = st.number_input('Tingkat serum kreatinin dalam darah')
with col3:serum_sodium = st.number_input('Tingkat natrium serum dalam darah')
with col1:sex = st.number_input('Jenis kelamin')
with col2:smoking = st.number_input('Perokok/bukan')
with col3:time = st.number_input('Periode tindak lanjut')

predict = ''

if st.button('Prediksi Penyakit Gagal Jantung'):
    predict = model.predict([[age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,sex,smoking,time]])
    
    if (predict[0]==0):
        predict = 'Pasien bukan pengidap penyakit gagal jantung'
    else:
        predict = 'Pasien adalah pengidap penyakit gagal jantung'
        
st.success(predict)
