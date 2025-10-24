import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

# Configuración de la página
st.set_page_config(page_title="Vehicles Dashboard", layout="wide")
st.header("Demo: Anuncios de venta de coches")

# --- Cargar los datos de forma robusta ---
DATA_PATH = Path(__file__).resolve().parent / "vehicles_us.csv"

try:
    car_data = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    st.error("❌ No se encontró el archivo 'vehicles_us.csv'. Verifica que esté en la raíz del proyecto.")
    st.stop()

# --- Botón: histograma ---
st.subheader("Gráficos")
hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Creación de un histograma para la columna `odometer`")
    fig = px.histogram(car_data, x="odometer", title="Distribución del odómetro")
    st.plotly_chart(fig, use_container_width=True)

# --- Botón: gráfico de dispersión ---
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Gráfico de dispersión: `odometer` vs `price`")
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        opacity=0.6,
        title="Relación entre odómetro y precio"
    )
    st.plotly_chart(fig, use_container_width=True)
