import requests
import os
import csv
from datetime import datetime


MEXICO_LAT=19.4326
MEXICO_LONGITUDE=-99.1332
API_KEY=8ee697c6e4a325851b0e01ab51bbb998
FILE_NAME="clima-mexico-hoy.csv"


def get_weather(lat,lon,api):
    pass


def write2csv(json_response, csv_filename):
    pass


def process(json):
    normalized_dict={}
    return normalized_dict


def main():
    print("=====Bienvenido a Mexico-Clima=====")
    mexico_weather= get_weather(lat=MEXICO_LAT, lon=MEXICO_LONGITUDE, api=API_KEY)
    if mexico_weather['cod']!=404:
        process(mexico_weather)
        write2csv() #

    else:
        print("Ciudad no disponible o API KEY no válida")



    if __name__=='__main__':
        main()


        
