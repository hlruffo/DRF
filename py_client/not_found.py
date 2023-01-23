import requests

endpoint = "http://127.0.0.1:8000/api/products/1000000000000000"

get_response = requests.get(endpoint)  # HTTP REQUEST

print(get_response.json())  # PRINT JSON

