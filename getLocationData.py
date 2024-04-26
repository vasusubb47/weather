import requests
import pandas as pd
import time
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY: str = os.getenv('API_KEY')

locations: list[str] = []
latitude: list[float] = []
longtitude: list[float] = []

with open("locations.txt", "r") as location_file:
    locations = [loc.strip() for loc in location_file.readlines()]

for location in locations:
    resopnse = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid={API_KEY}")
    print(f"{location=}")
    res_json = resopnse.json()
    latitude.append(res_json[0]["lat"])
    longtitude.append(res_json[0]["lon"])

data = {"locations": locations, "latitude": latitude, "longitude": longtitude}

df = pd.DataFrame(data)

print(df)

df.to_csv("locations.csv")