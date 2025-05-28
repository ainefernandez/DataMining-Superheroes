"""
Superhero Data Scraper

Author: Ainé Fernández

This script scrapes superhero data from the Superhero API and saves it to a CSV file.
It uses an API token stored in a .env file to authenticate requests.
For each superhero ID (from 1 to 731), it fetches the biography, powerstats, work, appearance, and image.
It skips any superhero entry that contains 'null' in any of the powerstats.
The valid superhero data is compiled into a list of dictionaries, converted into a pandas DataFrame,
and exported as a CSV file to the ../data/superheroes.csv path.
"""

import os
import requests
import pandas as pd
from dotenv import load_dotenv
from tqdm import tqdm  # For progress bar

# Load API access token from .env file
load_dotenv()
token = os.getenv('access_token')

# Validate token
if not token:
    raise ValueError("API token not found. Please set 'access_token' in your .env file.")

# Base URL for the Superhero API
base_url = f'https://superheroapi.com/api/{token}'

# List to store superhero data
superheroes_data = []

# Fetch data for all superheroes with progress bar
for hero_id in tqdm(range(1, 732), desc="Fetching Superheroes"):
    try:
        # Fetch data
        biography = requests.get(f'{base_url}/{hero_id}/biography').json()
        powerstats = requests.get(f'{base_url}/{hero_id}/powerstats').json()
        work = requests.get(f'{base_url}/{hero_id}/work').json()
        appearance = requests.get(f'{base_url}/{hero_id}/appearance').json()
        image = requests.get(f'{base_url}/{hero_id}/image').json()

        # Check if any powerstat is 'null'
        powerstats_values = [
            powerstats.get('intelligence'),
            powerstats.get('strength'),
            powerstats.get('speed'),
            powerstats.get('durability'),
            powerstats.get('power'),
            powerstats.get('combat')
        ]

        if any(stat == 'null' for stat in powerstats_values):
            continue  # Skip this superhero

        # Construct the superhero record
        superhero = {
            'id': hero_id,
            'superhero_name': biography.get('name'),
            'real_name': biography.get('full-name'),
            'publisher': biography.get('publisher'),
            'alignment': biography.get('alignment'),
            'gender': appearance.get('gender'),
            'race': appearance.get('race'),
            'occupation': work.get('occupation'),
            'intelligence': powerstats.get('intelligence'),
            'strength': powerstats.get('strength'),
            'speed': powerstats.get('speed'),
            'durability': powerstats.get('durability'),
            'power': powerstats.get('power'),
            'combat': powerstats.get('combat'),
            'image_url': image.get('url'),
            'api_url': (
                f'https://akabab.github.io/superhero-api/api/id/{hero_id}.json'
            )
        }

        superheroes_data.append(superhero)

    except requests.RequestException as e:
        print(f"Error fetching hero ID {hero_id}: {e}")

# Create a DataFrame from the list of superheroes
superheroes = pd.DataFrame(superheroes_data)

# Save the DataFrame to a CSV file
output_path = '../data/superheroes.csv'
superheroes.to_csv(output_path, index=False)
