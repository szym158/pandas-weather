from config import Settings
import requests
import datetime
from tools import wind_speed
from tools import stopnie_celsjusza

def fetch_weather():
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={Settings.city}&appid={Settings.api_key}"

    try:
        response = requests.get(URL)
        weather = response.json()

        feels = weather["main"]["feels_like"]

        data = {
            "odczuwalna": stopnie_celsjusza(weather["main"]["feels_like"]),
            "Ciśnienie": weather["main"]["pressure"],
            "Wilgotność": weather["main"]["humidity"],
            "Zwykla temperatura": stopnie_celsjusza(weather["main"]["temp"]),
            "opis pogody": weather["weather"][0]["description"],
            "miejsce":  weather["name"],
            "predkosc wiatru": wind_speed(weather["wind"]["speed"]),
            "data pomiaru" : datetime.datetime.now()
        }
        return(data)


    except:
        print("wystąpił błąd")