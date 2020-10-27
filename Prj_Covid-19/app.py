
from flask import Flask, render_template
from flask import request

import pandas as pd


from scripts.mapworld import render_mapcountWorld


n = "dataSets/countrydata.csv"
data = pd.read_csv(n)
date_list = list(data[data['countryName'] == '中国']['dateId'])
countrylist = list(data[data['dateId'] == 20200412]['countryName'])
countrylist = ['中国']+countrylist


app = Flask(__name__, static_folder="templates")

@app.route("/")
def index():
    return render_template("index.html", cates = countrylist)


@app.route("/worldmap",methods=['POST', 'GET'])
def get_world_map():
    if request.method == 'GET':
        maptype = int(request.args.get('type', ''))
        i = int(request.args.get('index', ''))
        print(maptype)
        print(i)
        return render_mapcountWorld(date_list[int(i)],maptype).dump_options_with_quotes()

        
if __name__ == "__main__":
    app.run()