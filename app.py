import streamlit as st 
import streamlit.components.v1 as components 
import pickle
from PIL import Image

pickle_in = open("fordeploy.pkl","rb")
model=pickle.load(pickle_in)


def predict_popu(acousticness,danceability,duration_ms,energy,loudness,speechiness,valence):
    """
    Este modelo es para la predicción de proceso
    toma todas las caracteristicas de los audios que usamos para modelarlo y devuelve una predicción
    """
    prediction=model.predict([[acousticness,danceability,duration_ms,energy,loudness,speechiness,valence]])
    print(prediction)
    return prediction

def main():
    st.title("APP Spoti")
     
    html_temp2 = """
		<div style="background-color:royalblue;padding:10px;border-radius:10px">
		<h2 style="color:white;text-align:center;">Canciones Spoti </h2>
        <h1 style="color:white;text-align:center;">Predicción de popularidad</h1>
		</div>
		"""
    components.html(html_temp2)

    image = Image.open('spot.png')
    st.image(image, caption="")
    
    st.success("Todas las caracteristicas deben ir en números")
    acousticness = st.text_input("Acustica","Escribe aqui")
    danceability = st.text_input("Bailable","Escribe aqui")
    duration_ms = st.text_input("Duracion","Escribe aqui")
    energy = st.text_input("Ritmo","Escribe aqui")
    loudness = st.text_input("Ruidoso","Escribe aqui")
    speechiness = st.text_input("Más hablada","Escribe aqui")
    valence = st.text_input("Balance","Escribe aqui")
    result=""

    if st.button("Prediccion"):
        result=predict_popu(acousticness,danceability,duration_ms,energy,loudness,speechiness,valence)
    st.success('La popularidad de la cancion es: {}'.format(result))

if __name__=='__main__':
    main()