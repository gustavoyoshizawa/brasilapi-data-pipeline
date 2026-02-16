#Padronizando os dados

def normalize_cep(data: dict):
    return {
        "cep": data.get("cep"),
        "state": data.get("state"),
        "city": data.get("city"),
        "neighborhood": data.get("neighborhood"),
        "street": data.get("street")
    }