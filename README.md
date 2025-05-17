# Optimizador de Riego por Tipo de Suelo

Esta es una aplicación sencilla desarrollada en Python con la librería Tkinter, diseñada para ayudar a agricultores y técnicos a obtener **recomendaciones básicas de riego** basadas en el **tipo de suelo** predominante en una parcela.

## ¿Qué hace?

La aplicación permite al usuario seleccionar un tipo de suelo común (como Arenoso, Franco, Arcilloso, etc.) de una lista desplegable. Al seleccionar el suelo, la aplicación muestra automáticamente una descripción general de las características de ese suelo relacionadas con el agua y ofrece recomendaciones básicas sobre la frecuencia y el volumen de riego adecuados para optimizar el uso del agua y favorecer el desarrollo del cultivo.

## Características

* Interfaz gráfica simple e intuitiva.

* Selección de tipos de suelo comunes.

* Recomendaciones de riego adaptadas a las propiedades de retención y movimiento del agua en cada tipo de suelo.

* Pestaña de información con conceptos básicos sobre la relación suelo-agua y el riego.

## Propósito

El objetivo de esta herramienta es proporcionar una guía rápida y accesible para tomar decisiones iniciales sobre la estrategia de riego, reconociendo que el tipo de suelo es un factor fundamental que influye en la eficiencia del riego y la salud del cultivo.

## Cómo usar

1. Ejecuta la aplicación (`optimizador_riego.py` o el archivo ejecutable `.exe`).

2. Ve a la pestaña "Recomendaciones de Riego".

3. Selecciona el tipo de suelo de tu interés en el menú desplegable.

4. Lee las recomendaciones que aparecerán en el área de texto.

5. Consulta la pestaña "Información" para entender los conceptos detrás de las recomendaciones.

*Nota: Las recomendaciones proporcionadas son generales y deben ser ajustadas considerando otros factores agronómicos como el cultivo específico, su etapa de desarrollo, las condiciones climáticas locales y el sistema de riego utilizado.*

## Requisitos

* Python 3.x

* Librería Tkinter (generalmente incluida con la instalación estándar de Python)

## Instalación (desde código fuente)

1. Clona o descarga este repositorio.

2. Abre una terminal en la carpeta del proyecto.

3. Ejecuta el script: `python optimizador_riego.py`

## Generar Ejecutable (.exe para Windows)

Puedes usar PyInstaller para crear un archivo ejecutable:

```bash
pip install pyinstaller
pyinstaller --onefile optimizador_riego.py

EL ejecutable se encontratará en la carpeta dist .

Desarrolado por
Luisfarming
