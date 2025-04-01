import os
import requests 
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

def get_weather(city):
    try:
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'q':city,
            'appid':API_KEY,
            'units':'imperial'
        }
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            print(f'Weather in {city}: {data['weather'][0]['description'].capitalize()}')
            print(f'Tempature: {data['main']['temp']}F')
        else:
            print(f'Error: {response.status_code} - {response.json()['message']}')
    except Exception as e:
        print(f'Error: {e}')

get_weather('Culver City')