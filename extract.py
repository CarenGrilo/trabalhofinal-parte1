import requests

BASE_URL = 'https://brasilapi.com.br/api'

def extract_cities():
    r = requests.get(BASE_URL+'/cptec/v1/cidade')
    return r.json()

def forecast_weather(city_id):
    r = requests.get(BASE_URL+f"/cptec/v1/clima/previsao/{city_id}")
    return r.json()

def forecast_waves(city_id):
    r = requests.get(BASE_URL+f"/cptec/v1/ondas/{city_id}")
    return r.json()