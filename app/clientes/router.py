from os import getenv
from . import main
from flask import request
import pymssql
import json

conn = pymssql.connect("localhost", "sa", "admin", "banco")
cursor = conn.cursor(as_dict=True)

@main.route("/",methods=['GET'])
def index():
    cursor.execute('SELECT * FROM clientes')
    dados = []
    for row in cursor:
        dados.append(row)

    # conn.close()
    return json.dumps(dados)

@main.route("/",methods=['POST'])
def salvar():
    dados = request.get_json()
    print(dados)
    cursor.execute('INSERT INTO clientes VALUES(%s,%s,%s,%s)',
    (dados['data'],dados['nome'],dados['telefone'],dados['email'])
    )
    conn.commit()
    return json.dumps(dados)