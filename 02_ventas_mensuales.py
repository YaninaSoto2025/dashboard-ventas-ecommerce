import pandas as pd
from pathlib import Path

# Carpeta donde está este script (funciona con cualquier nombre de carpeta)
carpeta = Path(__file__).parent
df = pd.read_csv(carpeta / "ventas_mensuales.csv")

# 1. Revisión
df["mes"] = pd.to_datetime(df["mes"])
df = df.sort_values("mes")
print(df.shape)
print(df.isna().sum())
print(df.duplicated().sum())

# 2. Columnas nuevas
df["ticket_promedio"] = (df["ingresos"] / df["pedidos"]).round(2)
df["crecimiento_pct"] = (df["ingresos"].pct_change() * 100).round(1)

print(df.head())
print(df.tail())

# 3. Guardar el archivo limpio
df.to_csv(carpeta / "ventas_mensuales_limpio.csv", index=False, encoding="utf-8-sig")
print("Archivo limpio guardado")