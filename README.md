# Base de datos enriquecida con una API
![Image text](https://st3.depositphotos.com/4112313/13687/v/600/depositphotos_136872318-stock-illustration-color-flat-logo-triathlon-vector.jpg)

En este análisis tratamos de enriquecer a traves de una API un dataset, obteniendo un diccionario de atletas y graficos que explicarán si hay relación entre ciertas variables.
El dataset y la API provienen de la página oficial https://triathlon.org




## Table of Contents
1. [Información general](#Informacion-general)
2. [Datos](#Datos)
3. [Tecnologías](#Tecnologías)
4. [Librerías](#Librerías)
## Información general
***
Para el dataset hemos utilizado el World Triathlon Rankings, de la categoría Elite-Men https://triathlon.org/rankings/world_triathlon_rankings/male .
Para la API hemos utilizado 2 diferentes. La primera nos da información relacionada con el id de cada atleta, y en la segunda utilizamos ese id para bajar información de cada uno.
## Datos
***
Ambos dataset contienen datos tanto categóricos como cuantitaivos, por ello haremos un data cleaning y un join de los DF.

Data cleaning:
- Filtrar columnas que vamos a usar
- Renombrar columnas
- Unir dataframes

## Technologias
***
Una lista de las librerías utilizadas en elproyecto:
* [Jupyter Notebook](https://jupyter.org/) : Version 6.1.4
* [Python](https://www.python.org/): Version 3.8.5
* [Visual Studio Code](https://code.visualstudio.com/)
## Librerías
***
Una pequeña introducción a las librerías usadas: 
```
import os
from dotenv import load_dotenv
import json
import requests
import re
load_dotenv()
from pandas import json_normalize
import pandas as pd
import src.funciones_api as funcion
import matplotlib.pyplot as plot
import seaborn as sns
from seaborn import violinplot
import numpy as np
import time
```

