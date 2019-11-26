from time import sleep
import os
import sys
import requests
from tarefas import *
from flask import Flask
from flask import jsonify
from flask import request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://' + os.environ["REDIRECTIP"] + "/database", 27017)
db = client.database
tarefas = db.tarefas

@app.route('/Tarefa', methods=['GET', 'POST'])
def Tarefa():
    if request.method == 'GET':
        response = tarefas.find()
        listinha = []
        for i in response:
            i["_id"] = str(i["_id"])
            listinha.append(i)
        response = {"resposta" : listinha}
        return response

    if request.method == 'POST':
        return str(tarefas.insert(request.form.to_dict()))

@app.route('/Tarefa/<id>', methods=['GET', 'PUT', 'DELETE'])
def Tarefa_id(id):
    if request.method == 'GET':
        response = tarefas.find({"_id":ObjectId(id)})
        response = response[0]
        response["_id"] = str(response["_id"])
        return response

    if request.method == 'PUT':
        return str(tarefas.update({"_id":ObjectId(id)}, {"$set":request.form.to_dict()}))

    if request.method == 'DELETE':
        return str(tarefas.delete_one({"_id":ObjectId(id)}))

@app.route('/')
def healthcheck():
    resp = jsonify(success = True)
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')
