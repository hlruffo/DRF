import requests

product_id = input("Indique o id do produto a ser removido \n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} inválido')

if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"

get_response = requests.delete(endpoint)  # HTTP REQUEST

print(get_response.status_code, get_response.status_code == 204)  # PRINT JSON
