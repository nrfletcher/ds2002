"""
API Calls Homework
Riley Fletcher
2/29/2024
DS2002 SPR2024
"""
import requests
import pandas as pd

country = input("Enter a country name: ")
url = "https://restcountries.com/v3.1/name/" + country

response = requests.get(url)

if response.status_code == 200:
    jsonified = response.json()
    print(f"Capital: {jsonified[0]['capital'][0]}")
    print(f"Population: {jsonified[0]['population']}")
else:
    print(f'{response.json()['message']}: {response.status_code}')