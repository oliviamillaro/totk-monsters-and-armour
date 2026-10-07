import json
import requests

url = "https://api.hyrule-compendium.com/v3/compendium/all?game=totk"

print("Sending request to the Hyrule Compendium API...")

response = requests.get(url)

if response.status_code == 200:
    print("Success! Data received from server.")
    
    totk_data = response.json()
    
    output_filename = "totk_compendium_data.json"
    
    with open(output_filename, "w", encoding="utf-8") as file:
        json.dump(totk_data, file, indent=4)
        
    print(f"Done! File saved as '{output_filename}' in your project folder.")

else:
    print(f"Failed to fetch data. Server returned status code: {response.status_code}")