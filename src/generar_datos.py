import pandas as pd
import numpy as np

np.random.seed(42)

n = 400

fechas = pd.date_range("2025-01-01", periods=30)

productos = ["Collar", "Juguete", "Comida", "Cama", "Correa"]
canales = ["Organico", "Ads", "Social"]

data = {
    "fecha": np.random.choice(fechas, n),
    "producto": np.random.choice(productos, n),
    "precio": np.random.randint(5, 50, n),
    "cantidad": np.random.randint(1, 5, n),
    "canal": np.random.choice(canales, n),
}

df = pd.DataFrame(data)
df["ingresos"] = df["precio"] * df["cantidad"]

df.to_csv("data/ventas.csv", index=False)

print("Dataset generado en data/ventas.csv")
