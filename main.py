import requests
import os
import json
import pandas as pd

pd.set_options('display.max_columns', 500)

def get_ev_chargers(_api_key, ret_amount):
    api_key = os.getenv("NREL_API_KEY")

    req_url = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json?api_key={}&status=E&fuel_type=ELEC&ev_network=Tesla&limit=15".format(api_key)
    response = requests.get(req_url)
    response = json.loads(response.content)
    df = pd.DataFrame(list(response['fuel_stations']))
    df = [['station_name', 'date_last_confirmed', 'latitude', 'longitude']]
    return df

ev_chargers = get_ev_chargers(api_key, 1)

