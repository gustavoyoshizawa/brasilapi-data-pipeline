import requests
# Consumindo API
BASE_URL = "https://brasilapi.com.br/api"

def get_cep(cep: str):
    response = requests.get(f"{BASE_URL}/cep/v1/{cep}")
    response.raise_for_status()
    return response.json()