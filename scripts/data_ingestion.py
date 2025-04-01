import os
import time
import schedule
import psycopg2
import requests
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()
API_KEY = os.getenv('API_KEY')

def get_weather(city):
    try:
        base_url =  'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'q':city,
            'appid':API_KEY,
            'units':'imperial'
        }
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            weather_description = data['weather'][0]['description'].capitalize()
            temperature = data['main']['temp']
            print(f'Weather in {city}: {weather_description}')
            print(f'Temperature: {temperature}F')
            return city, weather_description, temperature
        else:
            print(f'Error: {response.status_code} - {response.json()["message"]}')
            return None
    except Exception as e:
        print(f'Error fetching weather data: {e}')
        return None
    
def insert_weather_data(city, description, temperature):
    try:
        conn = psycopg2.connect(
            dbname='weather_data',
            user='nicholasalba',
            password='',
            host='localhost',
            port='5432'
        )
        cur = conn.cursor()

        #inserting data into weather table
        insert_query="""
        INSERT INTO weather (city, description, temperature)
        VALUES (%s, %s, %s);
        """

        cur.execute(insert_query,(city, description,temperature))
        conn.commit()
        print(f'Successfully inserted weather data for {city}')

    except Exception as e:
        print(f'Error" {e}')
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def fetch_and_store_weather():
    city='Culver City'
    weather_data=get_weather(city)
    if weather_data:
        insert_weather_data(*weather_data)

schedule.every(1).hour.do(fetch_and_store_weather)

if __name__ == '__main__':
    print('Starting automated weather data ingestion')
    while True:
        schedule.run_pending()
        time.sleep(60)       
