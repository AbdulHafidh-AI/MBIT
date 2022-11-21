import streamlit as st 
import pandas as pd
import pickle

st.image('./assets/images.png')

st.write("""
    # Sistem Pakar dalam Menentukan Minat Bakat Mahasiswa Informatika
""")



st.write("""

    ## The Creator

    """)

### Menampilkan creator yang membuat web ini
col1, col2, col3 = st.columns(3)

with col1:
   st.write("""
   ### Abdul Hafidh
   """)
   st.image('./assets/Abdul_H.jpeg')

with col2:
    st.write("""
   ### Yoan Rifqi Candra
   """)
    st.image('./assets/Yoan.jpeg')

with col3:
   st.write("""
   ### Haris Daffa
   """)
   st.image("./assets/Haris.jpeg")

### Menampilkan foto creator




# use model to predict new data (new survey) from user input (web) and return the result (class) 

st.write("""
    ## Silahkan isi form berikut ini untuk mengetahui minat bakat anda di bidang informatika
    - Apakah kamu tertarik dengan matematika?
    - Apakah kamu tertarik dengan bidang keilmuan statistika?
    - Apakah kamu suka melihat data-data yang sangat banyak?
    - Apakah kamu suka dalam hal menerawang sesuatu?
    - Apakah kamu suka merancang atau mendesain sesuatu?
    - Apakah kamu suka membikin aplikasi mobile?
    - Apakah kamu tertarik dalam hal membikin game?
    - Apakah kamu tertarik dalam hal bikin web?
    - Apakah kamu tertarik dalam hal hacking seperti yang ada dalam film?
    - Apakah kamu tertarik dalam hal membobol situs web seperti bjorka?
    - Apakah kamu suka dalam hal pemetaan?
    - Apakah kamu suka membajak komputer orang?
    - Apakah kamu pernah membayangkan diri kamu itu sebagai seorang cyber security?
    - Apakah kamu suka dalam mengolah suatu citra/gambar?
    - Apakah kamu suka menjelajah suatu wilayah dengan tujuan untuk meneliti suatu wilayah?
""")

# get user input from web
soal1 = st.selectbox('Apakah kamu tertarik dengan matematika?', ('Tidak Setuju', 'Setuju'))
soal2 = st.selectbox('Apakah kamu tertarik dengan bidang keilmuan statistika?', ('Tidak Setuju', 'Setuju'))
soal3 = st.selectbox('Apakah kamu suka melihat data-data yang sangat banyak?', ('Tidak Setuju', 'Setuju'))
soal4 = st.selectbox('Apakah kamu suka dalam hal menerawang sesuatu?', ('Tidak Setuju', 'Setuju'))
soal5 = st.selectbox('Apakah kamu suka merancang atau mendesain sesuatu?', ('Tidak Setuju', 'Setuju'))
soal6 = st.selectbox('Apakah kamu suka membikin aplikasi mobile?', ('Tidak Setuju', 'Setuju'))
soal7 = st.selectbox('Apakah kamu tertarik dalam hal membikin game?', ('Tidak Setuju', 'Setuju'))
soal8 = st.selectbox('Apakah kamu tertarik dalam hal bikin web?', ('Tidak Setuju', 'Setuju'))
soal9 = st.selectbox('Apakah kamu tertarik dalam hal hacking seperti yang ada dalam film?', ('Tidak Setuju', 'Setuju'))
soal10 = st.selectbox('Apakah kamu tertarik dalam hal membobol situs web seperti bjorka?', ('Tidak Setuju', 'Setuju'))
soal11 = st.selectbox('Apakah kamu suka dalam hal pemetaan?', ('Tidak Setuju', 'Setuju'))
soal12 = st.selectbox('Apakah kamu suka membajak komputer orang?', ('Tidak Setuju', 'Setuju'))
soal13 = st.selectbox('Apakah kamu pernah membayangkan diri kamu itu sebagai seorang cyber security?', ('Tidak Setuju', 'Setuju'))
soal14 = st.selectbox('Apakah kamu suka dalam mengolah suatu citra/gambar?', ('Tidak Setuju', 'Setuju'))
soal15 = st.selectbox('Apakah kamu suka menjelajah suatu wilayah dengan tujuan untuk meneliti suatu wilayah ?', ('Tidak Setuju', 'Setuju'))

# create new data from user input and convert value to float
new_data = {
    # If value = "Setuju" then convert to 0.0, else convert to 1.0
    'soal1': 0.0 if soal1 == 'Setuju' else 1.0,
    'soal2': 0.0 if soal2 == 'Setuju' else 1.0,
    'soal3': 0.0 if soal3 == 'Setuju' else 1.0,
    'soal4': 0.0 if soal4 == 'Setuju' else 1.0,
    'soal5': 0.0 if soal5 == 'Setuju' else 1.0,
    'soal6': 0.0 if soal6 == 'Setuju' else 1.0,
    'soal7': 0.0 if soal7 == 'Setuju' else 1.0,
    'soal8': 0.0 if soal8 == 'Setuju' else 1.0,
    'soal9': 0.0 if soal9 == 'Setuju' else 1.0,
    'soal10': 0.0 if soal10 == 'Setuju' else 1.0,
    'soal11': 0.0 if soal11 == 'Setuju' else 1.0,
    'soal12': 0.0 if soal12 == 'Setuju' else 1.0,
    'soal13': 0.0 if soal13 == 'Setuju' else 1.0,
    'soal14': 0.0 if soal14 == 'Setuju' else 1.0,
    'soal15': 0.0 if soal15 == 'Setuju' else 1.0,
}


# create new dataframe from new data
new_df = pd.DataFrame(new_data, index=[0])

# load model
model = pickle.load(open('models/DT_model.pkl', 'rb'))

# predict new data
prediction = model.predict(new_df)

# show the result
st.write("""

    ## Berikut ini bidang minat yang sesuai dengan anda

""")

st.write("Kamu cocok di bidang minat: ", prediction[0])





 


