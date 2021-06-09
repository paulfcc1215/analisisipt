import sys
import os
# libreria para trabajar con archivos
import pandas as pd 
# libreria numérica
import numpy as np 
# para crear gráficos con matplotlib
import matplotlib.pyplot as plt 
import plotly.express as px
from datetime import datetime
#test de addfuller
from statsmodels.tsa.stattools import adfuller
from pmdarima.arima import auto_arima
import warnings

from werkzeug import formparser
warnings.filterwarnings('ignore')
from statsmodels.tsa.arima_model import ARIMA

def get_model(id_i,fd,fh):

    res = {}
    ipt_datos = {}
    prediccion = {}
    ##importar dataset csv
    datos = pd.read_csv("data/ipt_2016_2021_4.csv", delimiter=";")
    datos = datos.set_index('PERIODO')
    datos.sort_index(inplace=True)
    
    industria = list(datos.keys())[int(id_i)]
    
    fechas = list(datos[industria].keys())
    valores = datos[industria].values.tolist()
    length = len(fechas)
    for i in range(length):
        ipt_datos[fechas[int(i)]] = valores[i]
    
    res['ipt_datos'] = ipt_datos
    res['prediccion'] = prediccion
    
    return res
    
    # ##gráfica de dataset
    # datos[industria].plot(figsize=(15,5))
    # plt.title(industria)
    # plt.xlabel('Serie de tiempo (PERIODO)')
    # plt.ylabel('IPT')
    # plt.show()

    # datos_anual = datos.resample(rule='A').sum()
    # datos_anual[industria].plot(figsize=(20,5))

    # ##prueba unitaria a la serie de tiempo para obtener correlación
    # def adfuller_test(dataset):
    #     dftest = adfuller(dataset,autolag='AIC')
    #     print("1. ADF: ", dftest[0])
    #     print("2. P-Value: ", dftest[1])
    #     print("3. Num of Lags: ", dftest[2])
    #     print("4. Num of observations Used for ADF Regresion and Critical Values Calculation: ", dftest[3])
    #     print("5. Critical Values:")
    #     for key, val in dftest[4].items():
    #         print ("\t",key,": ",val)

    # adfuller_test(datos[industria])

    # stepwise_fit = auto_arima(datos[industria],trace=True,suppress_warnings=True)
    # print('*********************************   SUMMARY ENTRENAMIENTO   *********************************')
    # print(stepwise_fit.summary())
    # print('********************************* FIN SUMMARY ENTRENAMIENTO *********************************')

    # #set de datos de entrenamiento y de prueba
    # train = datos.iloc[:-10]
    # test = datos.iloc[-10:] #10 instancias para datos de prueba
    # #entrenamiento del modelo
    # modelo = ARIMA(train[industria],order=(0,2,1))
    # modelo = modelo.fit()
    # print('*********************************   RESUMEN MODELO   *********************************')
    # print(modelo.summary())
    # print('********************************* FIN RESUMEN MODELO *********************************')

    # inicio = len(train)
    # fin = len(train)+len(test)-1

    # pred = modelo.plot_predict(start=1,end=len(datos)+3,plot_insample=True)

    # pred.set_size_inches(15, 5)
    # #pred = modelo.predict(start=inicio,end=fin,typ='levels')
    # #print(pred)
    # plt.title(industria)
    # plt.xlabel('Serie de tiempo (PERIODO)')
    # plt.ylabel('IPT')
    # plt.show()

    return {
        'Feb-2016' : 93.82, 
        'Mar-2016' : 93.82,
        'Abr-2016' : 93.05,
        'May-2016' : 93.45,
        'Jun-2016' : 92.54,
        'Jul-2016' : 92.20
    }








"""
Funcion para obtener las industrias cargadas en la base
"""
def get_industrias():
    datos = pd.read_csv("data/ipt_2016_2021_4.csv", delimiter=";")
    datos = datos.set_index('PERIODO')
    catalogo_industrias = {}
    i = 0
    for clave in datos.keys():
        catalogo_industrias[i]=clave
        i = i + 1
    return catalogo_industrias






"""
T e s t
"""
def test():
    return {
        'Feb-2016' : 93.82, 
        'Mar-2016' : 93.82,
        'Abr-2016' : 93.05,
        'May-2016' : 93.45,
        'Jun-2016' : 92.54,
        'Jul-2016' : 92.20
    }