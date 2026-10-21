import pandas as pd

ruta = r"C:\Users\Admin\Desktop\proyecto_ventas\productos.csv"
df = pd.read_csv(ruta)

# 1. Limpieza básica
df = df.drop_duplicates()
for col in ["name", "category", "brand"]:
    df[col] = df[col].str.strip()

# 2. Chequeos de calidad
print("Precios <= 0:", (df["retail_price"] <= 0).sum())
print("Costo mayor al precio:", (df["cost"] > df["retail_price"]).sum())

# 3. Columnas nuevas
df["margen"] = (df["retail_price"] - df["cost"]).round(2)
df["margen_pct"] = (df["margen"] / df["retail_price"] * 100).round(1)

# 4. Resumen por categoría
resumen = df.groupby("category").agg(
    productos=("name", "count"),
    precio_prom=("retail_price", "mean"),
    margen_pct_prom=("margen_pct", "mean"),
).round(1).sort_values("productos", ascending=False)
print(resumen)

# 5. Guardar el archivo limpio para Power BI
df.to_csv(r"C:\Users\Admin\Desktop\proyecto_ventas\productos_limpio.csv",
          index=False, encoding="utf-8-sig")
print("Archivo limpio guardado")