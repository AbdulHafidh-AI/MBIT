import streamlit as st 
import pandas as pd
import pickle

st.write("""
    # Sistem pakar dalam menentukan minat bakat mahasiswa informatika
""")

st.image('./assets/images.png')

# use model to predict new data (new survey) from user input (web) and return the result (class) 

st.write("""
    ## Masukkan data diri anda

    -  Apakah kamu suka melihat rumus matematika?
    -  Apakah kamu suka mendesain?
    -  Apakah kamu menyukai hal-hal yang berkaitan dengan Internet of Things (IoT)?
    -  Apakah kamu menyukai hal-hal yang berkaitan dengan pemetaan?
    -  Apakah kamu menyukai hal-hal yang berkaitan dengan perkembangan teknologi?
    -  Apakah kamu menyukai hal-hal yang berkaitan dengan Artificial Inteligence (AI)?
    -  Apakah kamu menyukai hal-hal yang berkaitan dengan survey lapangan?
    -  Apakah kamu menyukai hal-hal yang berkaitan dengan cloud computing/komputasi awan?
    -  Apakah kamu menyukai hal-hal yang berkaitan dengan interview?

""")

# get user input from web
soal2 = st.selectbox("Apakah kamu suka melihat rumus matematika?", ["Setuju", "Tidak Setuju"])
soal3 = st.selectbox("Apakah kamu suka mendesain?", ["Setuju", "Tidak Setuju"])
soal4 = st.selectbox("Apakah kamu menyukai hal-hal yang berkaitan dengan Internet of Things (IoT)?", ["Setuju", "Tidak Setuju"])
soal5 = st.selectbox("Apakah kamu menyukai hal-hal yang berkaitan dengan pemetaan?", ["Setuju", "Tidak Setuju"])
soal6 = st.selectbox("Apakah kamu menyukai hal-hal yang berkaitan dengan perkembangan teknologi?", ["Setuju", "Tidak Setuju"])
soal7 = st.selectbox("Apakah kamu menyukai hal-hal yang berkaitan dengan Artificial Inteligence (AI)?", ["Setuju", "Tidak Setuju"])
soal8 = st.selectbox("Apakah kamu menyukai hal-hal yang berkaitan dengan survey lapangan?", ["Setuju", "Tidak Setuju"])
soal9 = st.selectbox("Apakah kamu menyukai hal-hal yang berkaitan dengan cloud computing/komputasi awan?", ["Setuju", "Tidak Setuju"])
soal10 = st.selectbox("Apakah kamu menyukai hal-hal yang berkaitan dengan interview?", ["Setuju", "Tidak Setuju"])



# create new data from user input and convert value to float
new_data = {
    # If value = "Setuju" then convert to 1.0, else convert to 0.0
    'soal2': 1.0 if soal2 == "Setuju" else 0.0,
    'soal3': 1.0 if soal3 == "Setuju" else 0.0,
    'soal4': 1.0 if soal4 == "Setuju" else 0.0,
    'soal5': 1.0 if soal5 == "Setuju" else 0.0,
    'soal6': 1.0 if soal6 == "Setuju" else 0.0,
    'soal7': 1.0 if soal7 == "Setuju" else 0.0,
    'soal8': 1.0 if soal8 == "Setuju" else 0.0,
    'soal9': 1.0 if soal9 == "Setuju" else 0.0,
    'soal10': 1.0 if soal10 == "Setuju" else 0.0,
}


# create new dataframe from new data
new_df = pd.DataFrame(new_data, index=[0])

# load model
model = pickle.load(open('models/svm_model.pkl', 'rb'))

# predict new data
prediction = model.predict(new_df)

# show the result
st.write("""

    ## Hasil Klasifikasi

""")

st.write("Kamu termasuk dalam kelas: ", prediction[0])





 


