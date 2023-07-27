#Adelaida Suarez
#https://www.linkedin.com/in/adelaidasuarezp/

#importar las librerias
import requests
from pprint import pprint

#obtener la API Key de Openweathermap
API_Key = 'dc585707836c14981cca467350cda4f6'

#pedir al usuario la ciudad de la que quiere conocer el tiempo
city = input("Ingresa una ciudad: ")

# acceso a la web
base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}"

try:
    response = requests.get(base_url)
    response.raise_for_status()
    weather_data = response.json()

    if weather_data['cod'] == 200:
        print(f"Datos meteorológicos para {city}:")
        print(f"Clima: {weather_data['weather'][0]['description']}")
        print(f"Temperatura: {weather_data['main']['temp']} K")
        print(f"Humedad: {weather_data['main']['humidity']}%")
        print(f"Velocidad del viento: {weather_data['wind']['speed']} m/s")
    else:
        print(f"Error: {weather_data['message']}")
except requests.exceptions.RequestException as e:
    print("Error de conexión:", e)
except Exception as ex:
    print("Error:", ex)