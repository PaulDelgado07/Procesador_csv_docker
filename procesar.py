import os
from pathlib import Path

import pandas as pd

# Rutas configurables mediante variables de entorno
INPUT_PATH = Path(os.getenv("INPUT_PATH", "/app/datos/ventas.csv"))
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "/app/salida"))


def procesar_ventas():
    if not INPUT_PATH.is_file():
        raise FileNotFoundError(f"No se encontró el archivo: {INPUT_PATH}")

    # Leer el archivo CSV
    df = pd.read_csv(INPUT_PATH)

    # Validar las columnas necesarias
    columnas = {"producto", "cantidad", "precio"}
    if not columnas.issubset(df.columns):
        raise ValueError("El CSV debe contener producto, cantidad y precio")

    # Limpiar los datos
    df = df.dropna(subset=["producto", "cantidad", "precio"]).copy()
    df.loc[:, "cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce")
    df.loc[:, "precio"] = pd.to_numeric(df["precio"], errors="coerce")
    df = df.dropna(subset=["cantidad", "precio"]).copy()

    # Calcular el total por venta
    df.loc[:, "total"] = df["cantidad"] * df["precio"]

    # Calcular estadísticas por producto
    resumen = df.groupby("producto", as_index=False).agg(
        unidades_vendidas=("cantidad", "sum"),
        ingreso_total=("total", "sum")
    )

    # Crear directorio de salida
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Guardar resultados
    df.to_csv(OUTPUT_DIR / "ventas_limpias.csv", index=False)
    resumen.to_csv(OUTPUT_DIR / "resumen.csv", index=False)

    print("Procesamiento completado correctamente.")
    print(f"Registros procesados: {len(df)}")
    print(f"Ingreso total: ${df['total'].sum():.2f}")
    print(f"Archivos generados en: {OUTPUT_DIR}")


if __name__ == "__main__":
    procesar_ventas()
