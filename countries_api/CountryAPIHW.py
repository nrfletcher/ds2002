"""
API Calls Homework
Riley Fletcher
2/29/2024
DS2002 SPR2024
"""
import requests
import pandas as pd
import json
import os


def is_valid_country(country_name):
    with open('countries.txt', 'r') as file:
        countries = {co.strip().lower() for co in file}

    return country_name in countries


country = input("Enter a country name: ").strip().lower()

while not is_valid_country(country):
    country = input(f"{country} is an invalid country name, try again or type 'exit' to exit: ").strip().lower()
    if country == 'exit':
        exit(0)

url = "https://restcountries.com/v3.1/name/" + country

response = requests.get(url)

if response.status_code == 200:
    jsonified = response.json()
    print(f"Capital: {jsonified[0]['capital'][0]}")
    print(f"Population: {jsonified[0]['population']}")

    country_data = [{'capital': jsonified[0]['capital'][0], 'population': jsonified[0]['population']}]

    df = pd.DataFrame(country_data)

    if os.path.exists('countries.json') and os.path.getsize('countries.json') > 0:
        with open('countries.json', 'r') as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    existing_data.extend(country_data)

    with open('countries.json', 'w') as file:
        json.dump(existing_data, file, indent=4)
else:
    print(f'{response.json()['message']}: {response.status_code}')
