# API


Consumindo dados da API de localidades do IBGE: [API e documentação](https://servicodados.ibge.gov.br/api/docs/localidades#api-_).

Duas abordagens:

1. Consumir o JSON, passar os dados para um dataframe e tratá-los nesse formato. Após tratamento, popular uma tabela no banco de dados MySQL. A conexão foi estabelecida com o [SQLAlchemy](https://pypi.org/project/SQLAlchemy/).

2. Utilizar os dados da tabela do MySQL e criar uma API com o [FastAPI](https://fastapi.tiangolo.com/).
