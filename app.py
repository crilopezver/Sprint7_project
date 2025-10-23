import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Vehicles Dashboard", layout="wide")
st.header("Demo: Anuncios de venta de coches")

@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

try:
    car_data = load_data()
    st.write("Registros cargados:", len(car_data))
except FileNotFoundError:
    st.warning("Coloca 'vehicles_us.csv' en la carpeta raíz para ver los gráficos.")
    car_data = None

st.subheader("Gráficos")

if st.button("Construir histograma") and car_data is not None:
    st.write("Histograma de `odometer`")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if st.button("Construir gráfico de dispersión") and car_data is not None:
    st.write("Dispersión `odometer` vs `price`")
    fig = px.scatter(car_data, x="odometer", y="price", opacity=0.6)
    st.plotly_chart(fig, use_container_width=True)
