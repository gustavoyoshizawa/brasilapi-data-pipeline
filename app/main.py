from clients.brasilapi_client import get_cep
from services.cep_service import normalize_cep
from repositories.cep_repository import insert_cep
from database.connection import get_connection

if __name__ == "__main__":
    conn = get_connection()
    cursor = conn.cursor()

    raw = get_cep("08295005")
    clean = normalize_cep(raw)
    insert_cep(cursor, clean)

    conn.commit()

    cursor.close()
    conn.close()

#testando no terminal
# if __name__ == "__main__":
    # raw = get_cep("08295005")
    # clean = normalize_cep(raw)
    # print(clean)

