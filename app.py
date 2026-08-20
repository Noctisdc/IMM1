import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image
import base64

st.markdown("""
    <style>
    .stApp {
        background-color: #FFF8F0;
    }
    section[data-testid="stSidebar"] {
        background-color: #FDECEC;
    }
    h1, h2, h3 {
        color: #B31B1B;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Fabula Japonesa")
image = Image.open('japan.jpg')
st.image(image, width=350)
with st.sidebar:
    st.subheader("Esrcibe y/o selecciona texto para ser escuchado.")
try:
    os.mkdir("temp")
except:
    pass
st.subheader("El mono y el cangrejo.")
st.write('Un cangrejo encontró una bola de arroz, y un mono, envidioso, la cambió por una semilla de caqui que él mismo había hallado. '
         'El cangrejo plantó la semilla, que creció hasta convertirse en un árbol cargado de frutos, pero no podía trepar para alcanzarlos. '
         'El mono se ofreció a subir por él, y una vez arriba se comió todos los caquis maduros; cuando el cangrejo le pidió su parte, '
         'le arrojó uno verde y duro que lo hirió de muerte. '
         'Sus hijos, ayudados por una castaña, una avispa y un mortero, '
         'prepararon una trampa: la castaña quemó al mono en el fogón, '
         'la avispa lo picó cuando fue a buscar agua, '
         'y el mortero cayó sobre él desde el techo. Así el cangrejo fue vengado.')
           
st.markdown(f"Quieres escucharlo?, copia el texto")
text = st.text_area("Ingrese El texto a escuchar.")
tld='com'
option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English"))
if option_lang=="Español" :
    lg='es'
if option_lang=="English" :
    lg='en'
def text_to_speech(text, tld,lg):
    
    tts = gTTS(text,lang=lg) # tts = gTTS(text,'en', tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name =
                print("Deleted ", f)


remove_files(7)
