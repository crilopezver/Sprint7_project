import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Vehicles Dashboard", layout="wide")
st.header("Demo: Anuncios de venta de coches")

# leer los datos
car_data = pd.read_csv("vehicles_us.csv")

# botón: histograma
hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Creación de un histograma para la columna `odometer`")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# botón: gráfico de dispersión
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Gráfico de dispersión: `odometer` vs `price`")
    fig = px.scatter(car_data, x="odometer", y="price", opacity=0.6)
    st.plotly_chart(fig, use_container_width=True)
