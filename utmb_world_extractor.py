import requests
import json
import csv
from typing import List, Dict, Any

def fetch_utmb_data() -> Dict[str, Any]:
    url = "https://utmblive-api.utmb.world/races/80koso/progressive?type=FINAL_RANKING&page=0&limit=200"
    headers = {
        "X-Tenant": "quitobyutmb_2025"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

def extract_runner_data(data: Dict[str, Any]) -> List[Dict[str, str]]:
    runners = []
    
    if 'runners' in data:
        for runner in data['runners']:
            fullname = runner.get('info', {}).get('fullname', '')
            
            # Split by finding the first uppercase word(s) as lastname
            words = fullname.split()
            lastname_words = []
            firstname_words = []
            
            # Find consecutive uppercase words at the beginning (lastname)
            for word in words:
                if word.isupper():
                    lastname_words.append(word)
                else:
                    # Once we hit a non-uppercase word, everything else is firstname
                    firstname_words = words[len(lastname_words):]
                    break
            
            lastname = ' '.join(lastname_words)
            firstname = ' '.join(firstname_words)
            
            runner_info = {
                'name': lastname,
                'firstname': firstname,
                'time': runner.get('raceTime', '')
            }
            runners.append(runner_info)
    
    return runners

def save_to_csv(runners: List[Dict[str, str]], filename: str = "utmb_results.csv"):
    if not runners:
        print("No data to save")
        return
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'firstname', 'time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for runner in runners:
            writer.writerow(runner)
    
    print(f"Data saved to {filename} with {len(runners)} runners")

def main():
    print("Fetching UTMB race data...")
    data = fetch_utmb_data()
    
    if data:
        print("Extracting runner information...")
        runners = extract_runner_data(data)
        
        print("Saving to CSV...")
        save_to_csv(runners)
    else:
        print("Failed to fetch data")

if __name__ == "__main__":
    main()
