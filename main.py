import requests
import os
import csv
from datetime import datetime

MEXICO_LAT=19.4326
MEXICO_LONGITUDE=-99.1332
API_KEY="8ee697c6e4a325851b0e01ab51bbb998"
FILE_NAME="clima-mexico-hoy.csv"

def get_weather(lat, lon, api):
    # Docs: https://openweathermap.org/current
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"lat": lat, "lon": lon, "appid": api, "units": "metric"}
    response = requests.get(url, params=params)
    return response.json()

def process(json_response):
    normalized_dict = {
        "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ciudad": json_response.get("name", ""),
        "lat": json_response.get("coord", {}).get("lat", ""),
        "lon": json_response.get("coord", {}).get("lon", ""),
        "temp": json_response.get("main", {}).get("temp", ""),
        "feels_like": json_response.get("main", {}).get("feels_like", ""),
        "temp_min": json_response.get("main", {}).get("temp_min", ""),
        "temp_max": json_response.get("main", {}).get("temp_max", ""),
        "pressure": json_response.get("main", {}).get("pressure", ""),
        "humidity": json_response.get("main", {}).get("humidity", ""),
        "weather_main": json_response.get("weather", [{}])[0].get("main", ""),
        "weather_description": json_response.get("weather", [{}])[0].get("description", ""),
        "wind_speed": json_response.get("wind", {}).get("speed", ""),
        "wind_deg": json_response.get("wind", {}).get("deg", ""),
        "clouds": json_response.get("clouds", {}).get("all", ""),
        "rain_1h": json_response.get("rain", {}).get("1h", ""),
        "snow_1h": json_response.get("snow", {}).get("1h", ""),
    }
    return normalized_dict

def write2csv(data_dict, csv_filename):
    file_exists = os.path.isfile(csv_filename)
    with open(csv_filename, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data_dict.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data_dict)

def main():
    print("=====Bienvenido a Mexico-Clima=====")
    mexico_weather = get_weather(lat=MEXICO_LAT, lon=MEXICO_LONGITUDE, api=API_KEY)
    if mexico_weather['cod'] != 404:
        data = process(mexico_weather)
        write2csv(data, FILE_NAME)
        print("Dato guardado:", data)
    else:
        print("Ciudad no disponible o API KEY no válida")

if __name__=='__main__':
    main()
