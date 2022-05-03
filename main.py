# StarWars Chatbot
import pandas as pd 
characters_path = './characters.csv'
planets_path = './planets.csv'
species_path = './species.csv'
starships_path = './starships.csv'
vehicles_path = './vehicles.csv'

df = pd.read_csv(characters_path)
print(df.head())