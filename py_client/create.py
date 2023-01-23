import requests

endpoint = "http://127.0.0.1:8000/api/products/"



data = {
    "title" : "Star Wars - The Return of the Jedi",
    "price": 32.99,
}
get_response = requests.post(endpoint, json= data)  # HTTP REQUEST
print(get_response.json())  # PRINT JSON

