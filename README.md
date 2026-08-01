## Autor

Marisol Veronica Tigasi Ugsha

Universidad Técnica de Cotopaxi

Carrera de Economía

2026

# Relación entre el crecimiento del PIB, la inflación y el desempleo en Ecuador mediante un modelo VAR

## Descripción

Este proyecto analiza la relación dinámica entre el crecimiento del Producto Interno Bruto (PIB), la inflación y la tasa de desempleo en Ecuador durante el período 2007–2024 mediante un modelo de Vectores Autorregresivos (VAR). El análisis se desarrolló en Python utilizando datos oficiales del Banco Mundial.

## Pregunta de investigación

¿Cómo interactúan dinámicamente el crecimiento del Producto Interno Bruto (PIB), la inflación y la tasa de desempleo en Ecuador durante el período 2007–2024 mediante un modelo VAR?

## Objetivo general

Analizar la relación dinámica entre el crecimiento del PIB, la inflación y el desempleo en Ecuador utilizando un modelo VAR.

## Fuente de datos

- Banco Mundial (World Development Indicators)
- País: Ecuador
- Período: 2007–2024
- Frecuencia: Anual

## Variables utilizadas

- Crecimiento anual del PIB (%)
- Inflación anual (%)
- Tasa de desempleo (%)

## Metodología

El proyecto incluye:

- Análisis descriptivo
- Estadística descriptiva
- Matriz de correlación
- Prueba Dickey-Fuller Aumentada (ADF)
- Transformación de variables
- Selección del número óptimo de rezagos
- Estimación del modelo VAR
- Diagnóstico del modelo
- Causalidad de Granger
- Funciones Impulso–Respuesta (IRF)
- Descomposición de la varianza (FEVD)
- Análisis de robustez

## Principales resultados

Los resultados muestran que:

- El desempleo aporta información para explicar el comportamiento futuro del crecimiento del PIB.
- El crecimiento del PIB aporta información para explicar la inflación.
- El modelo VAR(1) fue la mejor especificación según los criterios AIC y BIC.
- El modelo cumple los principales supuestos econométricos.

## Estructura del proyecto

```
proyecto-var-ecuador/
│.agent/ agent.py
├── data/
├── notebooks/
├── outputs/
├── paper/
├── prompts/
├── README.md
├── requirements.txt
└── .gitignore
```

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Statsmodels
- Matplotlib
- Jupyter Notebook

## Enlaces del proyecto

Repositorio GitHub:
https://github.com/marisoltigasi9075-jpg/TIGASI-MARISOL-proyecto-econometria

Dashboard en Vercel:
https://tigasi-marisol-proyecto-econometria.vercel.app
