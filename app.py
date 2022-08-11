from flask import Flask,render_template
import requests
import time
import pymongo

client = pymongo.MongoClient("mongodb://Pinkesh:Pinke$h911@cluster01-shard-00-00.ao46i.mongodb.net:27017,cluster01-shard-00-01.ao46i.mongodb.net:27017,cluster01-shard-00-02.ao46i.mongodb.net:27017/?ssl=true&replicaSet=atlas-gc9g1d-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client["cryptodb"]
coll = db["crypto"]


app = Flask(__name__)

def addData():
    key = "https://api.binance.com/api/v3/ticker/price?symbol="
    currencies = ["LTCUSDT","ETHUSDT","BNBUSDT","NEOUSDT","MCOUSDT","BCCUSDT"]

    data = {}
    for i in currencies:
        url = key + i
        r = requests.get(url)
        d = r.json()
        
        data[d['symbol']] = d['price']
    
    print(data)
    coll.insert_one(data)

@app.route("/")
def index():
    #addData()
    data = list(coll.find({}).sort("_id",pymongo.DESCENDING).limit(1))[0]
    data.pop("_id")
    print(data)

    return render_template("index.html",data=dict(data))

@app.route("/google-charts/pie-chart")
def google_pie_chart():
    #addData()
    data = list(coll.find({}).sort("_id",pymongo.DESCENDING).limit(1))[0]
    data.pop("_id")
    print(data)
    return render_template("index.html",data=dict(data))


@app.route("/google-charts/pie-chart3d")
def google_pie_chart3d():
    #addData()
    data = list(coll.find({}).sort("_id",pymongo.DESCENDING).limit(1))[0]
    data.pop("_id")
    print(data)
    return render_template("piechartthreed.html",data=dict(data))


@app.route("/google-charts/column-chart")
def google_column_chart():
    #addData()
    data = list(coll.find({}).sort("_id",pymongo.DESCENDING).limit(1))[0]
    data.pop("_id")
    print(data)
    return render_template("columnchart.html",data=dict(data))

@app.route("/google-charts/donut-chart")
def google_donut_chart():
    #addData()
    data = list(coll.find({}).sort("_id",pymongo.DESCENDING).limit(1))[0]
    data.pop("_id")
    print(data)
    return render_template("donutchart.html",data=dict(data))


if __name__ == "__main__":
    app.run(debug=True)