import pandas as pd
import json


input_json = '/Users/victor/Desktop/projects/previsao-precos-imoveis-dl/data/places.json'

df = pd.read_json(input_json)

output_csv = 'places_data.csv'
df.to_csv(output_csv, index=False)

print(f"Arquivo CSV gerado com sucesso: {output_csv}")
