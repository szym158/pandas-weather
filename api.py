from config import Settings
import requests
import datetime

def fetch_weather():
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={Settings.city}&appid={Settings.api_key}"

    try:
        response = requests.get(URL)
        weather = response.json()

        feels = weather["main"]["feels_like"]

        data = {
            "odczuwalna": weather["main"]["feels_like"],
            "Ciśnienie": weather["main"]["pressure"],
            "Wilgotność": weather["main"]["humidity"],
            "Zwykla temperatura": weather["main"]["temp"],
            "opis pogody": weather["weather"][0]["description"],
            "miejsce":  weather["name"],
            "predkosc wiatru": weather["wind"]["speed"],
            "data pomiaru" : datetime.datetime.now()
        }
        return(data)


    except:
        print("wystąpił błąd")
