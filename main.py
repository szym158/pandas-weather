from api import fetch_weather
from excel import append_to_excel
from excel import append_to_csv
import time

data = fetch_weather()


while True:
    data = fetch_weather()

    append_to_excel(data)
    append_to_csv(data)

    time.sleep(50)
    print("Pobrano nowe dane")