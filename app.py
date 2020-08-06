from flask import Flask, jsonify, render_template
import requests
import os

from item import Item

app = Flask(__name__)

@app.route('/')
def index():
    items = getItems()
    return render_template('index.html', items=items)

def getItems():
    backendURI = getBackendURI()
    r = requests.get(backendURI)
    items = []
    for i in r.json():
        items.append(Item(i["id"], i["name"], i["price"], i["count"]))
    
    print(items)
    return items

def getBackendURI():
    backendURI = "http://localhost:8082"
    if os.environ.get('BACKEND_URI') != None:
        backendURI = os.environ.get('BACKEND_URI')
    return backendURI