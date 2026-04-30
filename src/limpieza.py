import re
import csv
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

def eliminar_outliers_iqr(df, columna):
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    return df[(df[columna] >= limite_inferior) & (df[columna] <= limite_superior)]
    
def limpiar_datos(ruta_csv):
    # 1. leer el archivo
    filas = []
    with open(ruta_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for fila in reader:
            filas.append(fila)

    # 2. parsear filas problemáticas
    filas_limpias = []
    encabezado = filas[0]

    for fila in filas[1:]:
        if len(fila) == 1:  # fila problemática
            texto = fila[0]
            texto = re.sub(r'"(\d+),(\d+)"', r'\1.\2', texto)
            fila = texto.split(',')
        filas_limpias.append(fila)

    #Diccionario de deportes
    DEPORTES_VALIDOS={
        'fútbol' : 'Fútbol',
        'futbol' : 'Fútbol',
        'natacion' : 'Natación',
        'natacio' : 'Natación',
        'natació' : 'Natación',
        'natación' : 'Natación',
        'tenis' : 'Tenis',
        'tennis' : 'Tenis',
        'voleibol' : 'Voleibol',
        'volleyball' : 'Voleibol',
        'baloncesto' : 'Baloncesto',
        'basketball' : 'Baloncesto',
        'ciclismo' : 'Ciclismo',
        'atletismo': 'Atletismo',
        'boxeo': 'Boxeo',
        'ciclismo': 'Ciclismo',
        'rugby': 'Rugby',
    }


    df = pd.DataFrame(filas_limpias, columns=encabezado)
    df = df.replace(r'^\s*$', np.nan, regex=True)
    
    df['edad'] = pd.to_numeric(df['edad'], errors='coerce')
    df['peso_kg'] = pd.to_numeric(df['peso_kg'], errors='coerce')
    df['altura_cm'] = pd.to_numeric(df['altura_cm'], errors='coerce')
    df['frecuencia_cardiaca_bpm'] = pd.to_numeric(df['frecuencia_cardiaca_bpm'], errors='coerce')
    df['horas_entrenamiento_semana'] = pd.to_numeric(df['horas_entrenamiento_semana'], errors='coerce')
    df['rendimiento_score'] = pd.to_numeric(df['rendimiento_score'], errors='coerce')
    df['deporte'] = df['deporte'].str.strip().str.lower()
    df['deporte'] = df['deporte'].map(DEPORTES_VALIDOS) 
    
    df = eliminar_outliers_iqr(df, 'peso_kg')
    df = eliminar_outliers_iqr(df, 'horas_entrenamiento_semana')

    #Imputación de valores faltantes
    df= df.fillna(df.mean(numeric_only=True))

    return df 