import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={"title":"Titulo", "content": "Hello World", "price":"abc"})  # HTTP REQUEST
#print(get_response.headers)
#print(get_response.text) # PRINT RAW TEXT RESPONSE
print(get_response.json())  # PRINT JSON
# print(get_response.status_code) #PRINT STATUS CODE
