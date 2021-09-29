import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get("https://forecast.weather.gov/MapClick.php?lat=27.6062&lon=-80.4268#.YVRXoJrMKUk"  # Insert the .gov link of your area
                    "637245000000064&lon=-80.48609789999995#.Xp8xVFNKjOQ")
soup = BeautifulSoup(page.content, "html.parser")
week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')

(items[0].find(class_='period-name').get_text())
(items[0].find(class_='short-desc').get_text())
(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

weather = pd.DataFrame(
    {
        'period': period_names,
        'short description': short_desc,
        'temperature': temperatures
    })

# weather.to_csv("Weather results.csv") # You can uncomment this to make a 'csv' file instead
print(weather)
