import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def resumen_datos(df):
    resumen ={
        "Total de deportistas": len(df),
        "Promedio de rendimiento": round(float(df['rendimiento_score'].mean()), 2),
        "Edad Promedio": round(float(df['edad'].mean()), 2),
    }
    return resumen


def promedio_por_deporte(df):
    return (
        df.groupby("deporte")["rendimiento_score"]
        .mean()
        .round(2)
        .reset_index()
        .rename(columns={"rendimiento_score": "rendimiento Promedio"})
        .sort_values("rendimiento Promedio",ascending=False)
    )


def deportistas_destacados(df):
    deportistas_destacados= df[df['rendimiento_score']>=7]
    deportistas_destacados= deportistas_destacados[["nombre","deporte","edad","rendimiento_score"]]
    return deportistas_destacados

    