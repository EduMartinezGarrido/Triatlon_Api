# Base de datos enriquecida con una API
![Image text](https://st3.depositphotos.com/4112313/13687/v/600/depositphotos_136872318-stock-illustration-color-flat-logo-triathlon-vector.jpg)

En este análisis tratamos de enriquecer a traves de una API un dataset, obteniendo un diccionario de atletas y graficos que explicarán si hay relación entre ciertas variables.
El dataset y la API provienen de la página oficial https://triathlon.org




## Table of Contents
1. [Información general](#Informacion-general)
2. [Datos](#Datos)
3. [Tecnologías](#Tecnologías)
4. [Librerías](#Librerías)
5. [Hypotheses](#Hypotheses)
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
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plot
import src.funciones as fun
```

## Hypotheses
**1. ¿LOS TIBURONES ATACAN A LOS SURFISTAS POR ERROR DE IDENTIDAD?**

Vamos a intentar demostrar la teoría de que los tiburones atacan a los surfistas porque los confunden con algún animal.

![Image text](https://www.artsurfcamp.com/blog/wp-content/uploads/2017/04/eg.jpg)

**2. ¿EL ATAQUE ES MAS VIOLENTO SI ERES HOMBRE O MUJER HACIENDO SURF?**

Trataremos de buscar si existe una relación directa entre ser mujer u hombre, y la violencia con la que son atacados.

![Image text](https://margruesa.com/wp-content/uploads/2018/02/surf-hombres-mujeres-premios-9928.jpg)
