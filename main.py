import streamlit as st 
import pandas as pd
import pickle

st.write("""
    # Sistem pakar dalam menentukan minat bakat mahasiswa informatika
""")

st.image('./assets/images.png')

# use model to predict new data (new survey) from user input (web) and return the result (class) 

st.write("""
    ## Silahkan isi form berikut ini untuk mengetahui minat bakat anda di bidang informatika
    - Apakah kamu tertarik dengan matematika?
    - Apakah kamu suka melihat data-data yang sangat banyak?
    - Apakah kamu suka merancang atau mendesain sesuatu?
    - Apakah kamu suka dalam hal menerawang sesuatu?
    - Apakah kamu suka dalam mengolah suatu citra/gambar?
    - Apakah kamu tertarik dengan bidang keilmuan statistika?
    - Apakah kamu suka membajak komputer orang?
    - Apakah kamu suka membikin aplikasi mobile?
    - Apakah kamu tertarik dalam hal membobol situs web seperti bjorka?
    - Apakah kamu tertarik dalam hal membikin game?
    - Apakah kamu pernah membayangkan diri kamu itu sebagai seorang cyber security?
    - Apakah kamu suka menjelajah suatu wilayah dengan tujuan untuk meneliti suatu wilayah?
    - Apakah kamu tertarik dalam hal hacking seperti yang ada dalam film?
    - Apakah kamu tertarik dalam hal bikin web?
    - Apakah kamu suka dalam hal pemetaan?

""")

# get user input from web
soal1 = st.selectbox('Apakah kamu tertarik dengan matematika?', ('Setuju', 'Tidak Setuju'))
soal2 = st.selectbox('Apakah kamu suka melihat data-data yang sangat banyak?', ('Setuju', 'Tidak Setuju'))
soal3 = st.selectbox('Apakah kamu suka merancang atau mendesain sesuatu?', ('Setuju', 'Tidak Setuju'))
soal4 = st.selectbox('Apakah kamu suka dalam hal menerawang sesuatu?', ('Setuju', 'Tidak Setuju'))
soal5 = st.selectbox('Apakah kamu suka dalam mengolah suatu citra/gambar?', ('Setuju', 'Tidak Setuju'))
soal6 = st.selectbox('Apakah kamu tertarik dengan bidang keilmuan statistika?', ('Setuju', 'Tidak Setuju'))
soal7 = st.selectbox('Apakah kamu suka membajak komputer orang?', ('Setuju', 'Tidak Setuju'))
soal8 = st.selectbox('Apakah kamu suka membikin aplikasi mobile?', ('Setuju', 'Tidak Setuju'))
soal9 = st.selectbox('Apakah kamu tertarik dalam hal membobol situs web seperti bjorka?', ('Setuju', 'Tidak Setuju'))
soal10 = st.selectbox('Apakah kamu tertarik dalam hal membikin game?', ('Setuju', 'Tidak Setuju'))
soal11 = st.selectbox('Apakah kamu pernah membayangkan diri kamu itu sebagai seorang cyber security?', ('Setuju', 'Tidak Setuju'))
soal12 = st.selectbox('Apakah kamu suka menjelajah suatu wilayah dengan tujuan untuk meneliti suatu wilayah?', ('Setuju', 'Tidak Setuju'))
soal13 = st.selectbox('Apakah kamu tertarik dalam hal hacking seperti yang ada dalam film?', ('Setuju', 'Tidak Setuju'))
soal14 = st.selectbox('Apakah kamu tertarik dalam hal bikin web?', ('Setuju', 'Tidak Setuju'))
soal15 = st.selectbox('Apakah kamu suka dalam hal pemetaan?', ('Setuju', 'Tidak Setuju'))





# create new data from user input and convert value to float
new_data = {
    # If value = "Setuju" then convert to 1.0, else convert to 0.0
    'soal1': 1.0 if soal1 == 'Setuju' else 0.0,
    'soal2': 1.0 if soal2 == 'Setuju' else 0.0,
    'soal3': 1.0 if soal3 == 'Setuju' else 0.0,
    'soal4': 1.0 if soal4 == 'Setuju' else 0.0,
    'soal5': 1.0 if soal5 == 'Setuju' else 0.0,
    'soal6': 1.0 if soal6 == 'Setuju' else 0.0,
    'soal7': 1.0 if soal7 == 'Setuju' else 0.0,
    'soal8': 1.0 if soal8 == 'Setuju' else 0.0,
    'soal9': 1.0 if soal9 == 'Setuju' else 0.0,
    'soal10': 1.0 if soal10 == 'Setuju' else 0.0,
    'soal11': 1.0 if soal11 == 'Setuju' else 0.0,
    'soal12': 1.0 if soal12 == 'Setuju' else 0.0,
    'soal13': 1.0 if soal13 == 'Setuju' else 0.0,
    'soal14': 1.0 if soal14 == 'Setuju' else 0.0,
    'soal15': 1.0 if soal15 == 'Setuju' else 0.0,
}


# create new dataframe from new data
new_df = pd.DataFrame(new_data, index=[0])

# load model
model = pickle.load(open('models/svm_model.pkl', 'rb'))

# predict new data
prediction = model.predict(new_df)

# show the result
st.write("""

    ## Berikut ini bidang minat yang sesuai dengan anda

""")

st.write("Kamu cocok di bidang minat: ", prediction[0])





 


