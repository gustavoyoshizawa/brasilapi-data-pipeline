#Inserindo no Banco de Dados

def insert_cep(cursor, cep):
    cursor.execute("""
        INSERT INTO ceps (cep, state, city, neighborhood, street)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        cep["cep"],
        cep["state"],
        cep["city"],
        cep["neighborhood"],
        cep["street"],
    ))