import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Dashboard E-commerce", layout="wide")

st.title("📊 Dashboard E-commerce")

# Cargar datos
df = pd.read_csv("data/ventas.csv")
df["fecha"] = pd.to_datetime(df["fecha"])

# KPI principal
ingresos_totales = df["ingresos"].sum()

st.metric("💰 Ingresos totales", f"${ingresos_totales:,.0f}")

# Crear columnas
col1, col2 = st.columns(2)

# Ventas por canal
with col1:
    ventas_canal = df.groupby("canal")["ingresos"].sum().reset_index()
    fig_canal = px.bar(
        ventas_canal,
        x="canal",
        y="ingresos",
        title="Ingresos por canal",
        color="canal"
    )
    st.plotly_chart(fig_canal, use_container_width=True)

# Top productos
with col2:
    top_productos = (
        df.groupby("producto")["ingresos"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    fig_prod = px.bar(
        top_productos,
        x="producto",
        y="ingresos",
        title="Top productos",
        color="producto"
    )
    st.plotly_chart(fig_prod, use_container_width=True)

# Tendencia temporal
ventas_dia = df.groupby("fecha")["ingresos"].sum().reset_index()

fig_tiempo = px.line(
    ventas_dia,
    x="fecha",
    y="ingresos",
    title="Tendencia de ventas"
)

st.plotly_chart(fig_tiempo, use_container_width=True)

st.success("✅ App de analítica lista")
