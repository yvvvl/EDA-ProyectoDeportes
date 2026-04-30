# 🏆 EDA Proyecto Deportes

## ¿Qué es el proyecto?

**EDA Proyecto Deportes** es un proyecto de Análisis Exploratorio de Datos (EDA) enfocado en procesar, limpiar y analizar datos de rendimiento deportivo. El objetivo principal es extraer insights valiosos sobre el desempeño de deportistas en diferentes disciplinas, permitiendo identificar patrones, tendencias y deportistas destacados.

Este proyecto demuestra el flujo completo de un análisis de datos: desde la limpieza y normalización de datos problemáticos, hasta la generación de análisis estadísticos y exportación de resultados.

---

## 📊 Dataset Usado

El dataset utilizado es **`deportistas.csv`** ubicado en la carpeta `data/`. Este conjunto de datos contiene información sobre **1,984 deportistas** con los siguientes atributos:

- **nombre**: Nombre del deportista
- **deporte**: Disciplina deportiva (Fútbol, Natación, Tenis, Voleibol, Baloncesto, Ciclismo, Atletismo, Boxeo, Rugby)
- **edad**: Edad del deportista (en años)
- **peso_kg**: Peso corporal en kilogramos
- **altura_cm**: Altura en centímetros
- **frecuencia_cardiaca_bpm**: Frecuencia cardíaca en latidos por minuto
- **horas_entrenamiento_semana**: Horas de entrenamiento semanales
- **rendimiento_score**: Puntuación de rendimiento (escala 0-10)
- **posicion**: Posición o rol en su deporte

---

## 📁 Descripción de Archivos

### `src/limpieza.py`
Este módulo es responsable de **limpiar y preparar los datos** para su análisis. Realiza las siguientes operaciones:

- **Lectura del CSV**: Lee el archivo de datos en formato CSV
- **Parseo de filas problemáticas**: Corrige errores de formato (conversión de comas a puntos en números decimales)
- **Normalización de deportes**: Estandariza los nombres de deportes usando un diccionario de validación (maneja variaciones como "fútbol", "futbol", "natación", "natacio", etc.)
- **Conversión de tipos**: Convierte columnas numéricas a tipos `float64`
- **Eliminación de outliers**: Usa el método IQR (Rango Intercuartílico) para identificar y eliminar valores atípicos en peso y horas de entrenamiento
- **Imputación de valores faltantes**: Rellena datos faltantes con la media de cada columna numérica

**Función principal**: `limpiar_datos(ruta_csv)` - Retorna un DataFrame limpio y listo para analizar

### `src/analisis.py`
Este módulo contiene **funciones de análisis estadístico** para extraer insights de los datos:

- **`resumen_datos(df)`**: Genera un resumen general con:
  - Total de deportistas en el dataset
  - Promedio de rendimiento general
  - Edad promedio de los deportistas

- **`promedio_por_deporte(df)`**: Calcula el rendimiento promedio agrupado por disciplina deportiva y lo ordena de mayor a menor

- **`deportistas_destacados(df)`**: Identifica deportistas con rendimiento score ≥ 7, retornando su nombre, deporte, edad y rendimiento

### `notebooks/analisis.ipynb`
Es el **Jupyter Notebook principal** que orquesta todo el flujo del análisis:

1. **Preparación del entorno**: Importa librerías y configura rutas
2. **Carga de datos**: Lee el CSV y aplica la función `limpiar_datos()`
3. **Exploración inicial**: Muestra estructura, tipos de datos y primeras filas
4. **Análisis estadístico**: Ejecuta las funciones de análisis (resumen, promedio por deporte, deportistas destacados)
5. **Exportación de resultados**: Guarda dos archivos CSV en `outputs/`:
   - `deportistas_limpios.csv` - Datos procesados y listos
   - `analisis_por_deporte.csv` - Resumen de rendimiento por disciplina

---

## 📦 Librerías Usadas

El proyecto utiliza las siguientes librerías de Python:

| Librería | Versión | Uso |
|----------|---------|-----|
| **pandas** | - | Manipulación y análisis de datos |
| **numpy** | - | Operaciones numéricas y cálculos estadísticos |
| **scikit-learn** | - | Imputación de valores faltantes (`SimpleImputer`) |
| **matplotlib** | - | Visualización de datos y gráficos |
| **re** | (built-in) | Procesamiento de texto con expresiones regulares |
| **csv** | (built-in) | Lectura de archivos CSV |

---

## 🚀 Instrucciones de Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/yvvvl/EDA-ProyectoDeportes.git
   cd EDA-ProyectoDeportes
   ```

2. **Instala las dependencias** (si existe un archivo `requirements.txt`):
   ```bash
   pip install -r requirements.txt
   ```

   O instala las librerías manualmente:
   ```bash
   pip install pandas numpy scikit-learn matplotlib
   ```

3. **Ejecuta el Notebook:**
   ```bash
   jupyter notebook notebooks/analisis.ipynb
   ```

---

## 📂 Estructura del Proyecto

```
EDA-ProyectoDeportes/
├── data/
│   └── deportistas.csv          # Dataset original
├── src/
│   ├── limpieza.py              # Funciones de limpieza de datos
│   └── analisis.py              # Funciones de análisis estadístico
├── notebooks/
│   └── analisis.ipynb           # Notebook principal de análisis
├── outputs/                     # Resultados exportados
│   ├── deportistas_limpios.csv
│   └── analisis_por_deporte.csv
├── README.md                    # Este archivo
└── .gitignore
```

---

## 📈 Resultados Principales

- **Total de deportistas**: 1,984
- **Rendimiento promedio**: 5.55/10
- **Edad promedio**: 31.13 años
- **Deportes analizados**: 9 disciplinas diferentes

---

## 👤 Autor

**yvvvl** - GitHub: [@yvvvl](https://github.com/yvvvl)

---

## 📝 Licencia

Este proyecto está disponible bajo licencia abierta. Siéntete libre de utilizarlo y modificarlo según necesites.