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
import plotly.express as px
import time


os.system('say -v Samantha calling first Api')

import requests

api_key = os.getenv("Api_key")
url = "https://api.triathlon.org/v1/search/athletes?filters=athlete_gender,male|elite,true"

querystring = {"per_page":"100"}

headers = {"apikey": api_key}

response = requests.request("GET", url, headers=headers, params=querystring).json()


os.system('say -v Samantha successful response')
time.sleep(2)

dic_athlete_id = json_normalize(response.get("data"))
dic_athlete_id

lista_id = list(dic_athlete_id["athlete_id"])

os.system('say -v Samantha creating url')
time.sleep(2)

url_lista = funcion.web_atleta(lista_id)

os.system('say -v Samantha successful url')
time.sleep(2)

#Listas de las columnas a usar

lista_name = []
lista_stats = []
lista_weight = []
lista_height = []
lista_sponsors = []
lista_twitter = []
lista_place_of_birth = []
lista_languages_spoken = []


os.system('say -v Samantha calling second Api')

#Llamamos a la api para que baje la información de cada atleta

for i in url_lista:
    url = i

    headers = {"apikey": api_key}

    response = requests.request("GET", url, headers=headers).json()
    lista_stats.append(response.get("data")["stats"])
    lista_name.append(response.get("data")["athlete_title"])
    lista_weight.append(response.get("data")["weight"])
    lista_height.append(response.get("data")["height"])
    lista_sponsors.append(response.get("data")["sponsors"])
    lista_twitter.append(response.get("data")["twitter"])
    lista_place_of_birth.append(response.get("data")["place_of_birth"])
    lista_languages_spoken.append(response.get("data")["languages_spoken"])

os.system('say -v Samantha successful response')
time.sleep(1.5)

os.system('say -v Samantha creating dataframes')
time.sleep(1.5)

#Convertir listas en dataframes

df_stats = pd.DataFrame(lista_stats)
df_name = pd.DataFrame(lista_name)
df_weight = pd.DataFrame(lista_weight)
df_height = pd.DataFrame(lista_height)
df_sponsors = pd.DataFrame(lista_sponsors)
df_twitter = pd.DataFrame(lista_twitter)
df_place_of_birth = pd.DataFrame(lista_place_of_birth)
df_languages_spoken = pd.DataFrame(lista_languages_spoken)

#Renombrar columnas

df_name.columns = ["Name"]
df_sponsors.columns = ["Sponsors"]
df_height.columns = ["Height"]
df_weight.columns = ["Weight"]
df_languages_spoken.columns = ["Languages"]
df_place_of_birth.columns = ["Place_of_birth"]
df_twitter.columns = ["Twitter"]

os.system('say -v Samantha joining dataframes')
time.sleep(1.5)

#Unir todos los dataframes

df_outer = df_name.join(df_height, how= "outer")
df_outer = df_outer.join(df_weight, how= "outer")
df_outer = df_outer.join(df_languages_spoken, how= "outer")
df_outer = df_outer.join(df_sponsors, how= "outer")
df_outer = df_outer.join(df_twitter, how= "outer")
df_outer = df_outer.join(df_stats, how= "outer")


#Eliminamos unidades de media y renombramos algunos valores

df_outer["Height"] = df_outer["Height"].str.rstrip("cm")
df_outer["Height"] = df_outer["Height"].str.rstrip(" cm")
df_outer["Weight"] = df_outer["Weight"].str.rstrip("kg")
df_outer["Weight"] = df_outer["Weight"].replace({'None of your bu': None, '70 kg “in season “ ;-)': 70,'None of your business ': None})
df_outer["race_podium_percentage"] = df_outer["race_podium_percentage"].astype(int)

#Chequeo valores nulos

df_outer.isnull().sum()

#df_outer["Height"] = df_outer["Height"].fillna("Unknown")
#df_outer["Weight"] = df_outer["Weight"].fillna("Unknown")
#df_outer["Languages"] = df_outer["Languages"].fillna("Unknown")
#df_outer["Sponsors"] = df_outer["Sponsors"].fillna("Unknown")
#df_outer["Twitter"] = df_outer["Twitter"].fillna("Unknown")

df = pd.read_excel('data/WorldRankingsEliteMen.xlsx')

df = df[['Rank','name','YOB', 'Country', 'Total Points']]

df_total = df.join(df_outer, how = "outer")
df_total = df_total[['Rank', 'name', 'YOB', 'Country', 'Total Points',
       'Height', 'Weight', 'Languages', 'Sponsors', 'Twitter', 'race_starts',
       'race_finishes', 'finish_percentage', 'race_wins', 'race_podiums',
       'race_podium_percentage']]
df_total = df_total[df_total.Height != "Unknown"]
df_total = df_total[df_total.Weight != "Unknown"]
df_total["race_wins_percentage"] = ((df_total["race_wins"] / df_total["race_starts"])* 100).round()
df_total["Agebucket"] = pd.cut(df_total.YOB, bins=[1982,1985,1988,1991, 1994, 1997,2000])
df_total[["Height", "Weight"]] = df_total[["Height", "Weight"]].apply(pd.to_numeric)

df_total

os.system('say -v Samantha exporting dataframe as triathlon_merge')

df_total.to_csv("data/triatlon_merge.csv")