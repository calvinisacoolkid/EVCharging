import request
import os

api_key = os.getenv("NREL_API_KEY")
# Perform a GET request using Requests

req_url = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json?{}".format(api_key)

response = requests.get(req_url)

print(response)
print("=" * 50)
print(response.content)

