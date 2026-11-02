import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator
from io import BytesIO

st.set_page_config(page_title="Fábulas de Japón", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: #161616;
}
[data-testid="stHeader"] {
    background-color: #161616;
}
section[data-testid="stSidebar"] {
    background-color: #232323;
}
h1, h2, h3 {
    color: #d4a24c !important;
}
p, label, span, li {
    color: #f1e8d8 !important;
}
div.stButton > button {
    background-color: #b31b1b;
    color: white !important;
    border-radius: 20px;
    border: none;
    padding: 6px 20px;
}
div.stButton > button:hover {
    background-color: #d4a24c;
    color: #161616 !important;
}
</style>
""", unsafe_allow_html=True)

fabulas = {
    "El mono y el cangrejo": [
        "Un cangrejo encontró una bola de arroz, y un mono, envidioso, la cambió por una semilla de caqui que él mismo había hallado.",
        "El cangrejo plantó la semilla, que creció hasta convertirse en un árbol cargado de frutos, pero no podía trepar para alcanzarlos.",
        "El mono se ofreció a subir por él, y una vez arriba se comió todos los caquis maduros. Cuando el cangrejo le pidió su parte, le arrojó uno verde y duro que lo hirió de muerte.",
        "Sus hijos, ayudados por una castaña, una avispa y un mortero, prepararon una trampa. La castaña quemó al mono en el fogón, la avispa lo picó cuando fue a buscar agua y el mortero cayó sobre él desde el techo. Así el cangrejo fue vengado.",
    ],
    "Momotaro, el niño del melocotón": [
        "Un anciano y su esposa vivían solos junto a un río. Un día la mujer encontró un melocotón gigante que bajaba por el agua y se lo llevó a casa.",
        "Al abrirlo, dentro había un niño. Lo llamaron Momotaro, que significa niño melocotón, y creció fuerte y valiente.",
        "Cuando supo que unos ogros asolaban la región, Momotaro decidió ir a su isla. En el camino compartió sus pastelitos de mijo con un perro, un mono y un faisán, que se unieron a él.",
        "Juntos vencieron a los ogros y regresaron al pueblo con el tesoro que les habían robado. Desde entonces, todos vivieron en paz.",
    ],
}

idiomas = {"Español": "es", "English": "en", "Japonés": "ja"}


@st.cache_data(show_spinner=False)
def hacer_audio(texto, codigo, lenta):
    if codigo != "es":
        texto = GoogleTranslator(source="auto", target=codigo).translate(texto)
    audio = BytesIO()
    gTTS(text=texto, lang=codigo, slow=lenta).write_to_fp(audio)
    return audio.getvalue(), texto


with st.sidebar:
    st.subheader("Elige tu fábula")
    opcion = st.selectbox("Fábula", list(fabulas.keys()) + ["Escribe tu propio texto"])
    idioma = st.selectbox("Idioma de la voz", list(idiomas.keys()))
    lenta = st.toggle("Voz lenta")

codigo = idiomas[idioma]

st.title("Fábulas de Japón")
st.image("japan.jpg", width=350)

if opcion == "Escribe tu propio texto":
    texto = st.text_area("Escribe el texto que quieres escuchar")
    if st.button("Convertir a audio"):
        if texto.strip() == "":
            st.warning("Escribe algo primero.")
        else:
            try:
                audio, final = hacer_audio(texto, codigo, lenta)
                st.write(final)
                st.audio(audio, format="audio/mp3")
            except Exception:
                st.error("No se pudo generar el audio. Intenta de nuevo.")
else:
    escenas = fabulas[opcion]
    st.subheader(opcion)

    if st.button("▶ Escuchar la fábula completa"):
        try:
            audio, final = hacer_audio(" ".join(escenas), codigo, lenta)
            st.audio(audio, format="audio/mp3")
            st.download_button("Descargar audio", audio, file_name="fabula.mp3", mime="audio/mp3")
        except Exception:
            st.error("No se pudo generar el audio. Intenta de nuevo.")

    st.divider()

    for i, escena in enumerate(escenas):
        with st.container(border=True):
            st.markdown(f"**Escena {i + 1}**")
            st.write(escena)
            if st.button("🔊 Escuchar escena", key=f"escena{i}"):
                try:
                    audio, final = hacer_audio(escena, codigo, lenta)
                    if codigo != "es":
                        st.caption(final)
                    st.audio(audio, format="audio/mp3")
                except Exception:
                    st.error("No se pudo generar el audio. Intenta de nuevo.")
