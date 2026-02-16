# BrasilAPI Data Pipeline

Pipeline de ingestão de dados consumindo a API pública da BrasilAPI e persistindo as informações em um banco MySQL executando em container Docker.

O objetivo do projeto é demonstrar habilidades de integração de sistemas, organização de código em camadas, comunicação com serviços externos e persistência de dados, seguindo práticas comuns em ambientes de engenharia de dados e backend.

---

## Arquitetura

- **clients** → comunicação com API externa
- **services** → tratamento e normalização dos dados
- **repositories** → acesso e escrita no banco
- **database** → conexão
- **main** → orquestra o fluxo

## Tecnologias utilizadas

- Python
- requests
- mysql-connector-python
- Docker
- MySQL

## Estrutura do projeto

- app/
- clients/
- database/
- repositories/
- services/
- main.py
- sql/
- docker-compose.yml

## Como executar o projeto

### 1 - Subir o banco de dados

```bash
docker compose up -d

O banco será criado com:
host: localhost
port: 3306
user: root
password: root
database: brasilapi
```

### 2 - Criar a tabela

Conecte usando qualquer cliente SQL e execute:

```bash
USE brasilapi;

CREATE TABLE ceps (
id INT AUTO_INCREMENT PRIMARY KEY,
cep VARCHAR(10),
state VARCHAR(2),
city VARCHAR(255),
neighborhood VARCHAR(255),
street VARCHAR(255)
);
```

### 3 - Instalar dependências

```bash
pip install -r requirements.txt
```

### 4 - Rodar a ingestão

```bash
python app/main.py
```
