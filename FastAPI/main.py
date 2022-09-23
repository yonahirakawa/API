from typing import Union

from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session
from database import SessionLocal, engine
import crud, model, schema
from pydantic import BaseModel
import pandas as pd
from pandasql import PandaSQL
from sqlalchemy import create_engine
import json

app = FastAPI()

engine = create_engine("mysql+pymysql://root:@localhost:3306/test")
connection = engine.connect()
pdsql = PandaSQL()


@app.get("/")
def read_root():
    return {"Hello": "World"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/localidades")
def localidades():
    return {"API": "localidades"}


@app.get("/estados/{UF}")
def read_item(UF: str):
    query_uf = f"SELECT * FROM testeapi WHERE municipio_microrregiao_mesorregiao_UF_sigla = '{UF}';"
    df_uf = pd.read_sql(query_uf, connection)
    json_uf = df_uf.to_json(orient = 'records')
    result = json.loads(json_uf)
    return result


@app.get("/localidades/estados/{UF_id}/distritos")
def read_item(UF_id: int):
    query_uf_id = f"SELECT * FROM testeapi WHERE municipio_microrregiao_mesorregiao_UF_id = {UF_id};"
    df_uf_id = pd.read_sql(query_uf_id, connection)
    json_uf_id = df_uf_id.to_json(orient = 'records')
    result_id = json.loads(json_uf_id)
    return result_id

