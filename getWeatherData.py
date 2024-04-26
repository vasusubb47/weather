import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY: str = os.getenv('API_KEY')
LOCATIONS_PATH: str = "locations.csv"
WEATHER_API_URL: str = "https://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&appid={2}"

class WeatherData:
    
    location: str
    high_temp: float
    low_temp: float
    temp: float
    pressure: int
    humidity: int

    def __init__(self, location: str, res_json: dict):
        self.location = location
        self.high_temp = res_json["main"]["temp_max"]
        self.low_temp = res_json["main"]["temp_min"]
        self.temp = res_json["main"]["temp"]
        self.pressure = res_json["main"]["pressure"]
        self.humidity = res_json["main"]["humidity"]

    def __repr__(self):
        data = {"location": self.location, "high_temp": self.high_temp, "low_temp": self.low_temp, "temp": self.temp, "pressure": self.temp, "humidity": self.humidity}
        return f'{data}'


df = pd.read_csv(LOCATIONS_PATH, index_col=0)

# print(df)
weather_data: list[WeatherData] = []

for _index, row in df.iterrows():
    # print(row)
    # print(f"{row.locations=}, {row.latitude=}, {row.longitude=}")
    req_url = WEATHER_API_URL.format(row.latitude, row.longitude, API_KEY)
    print(f"{req_url=}")
    res = requests.get(req_url)
    # time.sleep(0.2)
    res_json = res.json()

    weather_data.append(WeatherData(row.locations, res_json))

print(f"{weather_data=}")
