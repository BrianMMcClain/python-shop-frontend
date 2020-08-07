from flask import Flask, jsonify, render_template
import requests
import os

from item import Item

app = Flask(__name__)
CONFIG_PATH = "/config/config.cfg"

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
    
    return items

def getBackendURI():
    if os.path.exists(CONFIG_PATH):
        app.config.from_pyfile(CONFIG_PATH)
        return app.config["BACKEND_URI"]
    return "http://localhost:8082"