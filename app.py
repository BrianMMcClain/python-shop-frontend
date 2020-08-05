from flask import Flask, jsonify, render_template
import requests 

from item import Item

app = Flask(__name__)

@app.route('/')
def index():
    items = getItems()
    return render_template('index.html', items=items)

def getItems():
    backendURI = "http://localhost:8082"
    r = requests.get(backendURI)
    items = []
    for i in r.json():
        items.append(Item(i["id"], i["name"], i["price"], i["count"]))
    
    print(items)
    return items