import json
import requests

url = "https://api.hyrule-compendium.com/v3/regions/all?game=totk"

print("Sending request for Regions data...")

response = requests.get(url)

if response.status_code == 200:
    print("Success! Region data received.")
    
    regions_data = response.json()
    
    output_filename = "totk_regions_data.json"
    
    with open(output_filename, "w", encoding="utf-8") as file:
        json.dump(regions_data, file, indent=4)
        
    print(f"Done! File saved as '{output_filename}' in your folder.")

else:
    print(f"Failed to fetch data. Server returned status code: {response.status_code}")