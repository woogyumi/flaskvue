from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')
data = {
    "fields": ['host', 'cpu', 'mem', 'hdd'],
    "data": [
        {'host':'wgkim', 'cpu':'30', 'mem':'1800', 'hdd':'20'},
        {'host':'bwlee', 'cpu':'40', 'mem':'1500', 'hdd':'30'},
        {'host':'mgkim', 'cpu':'50', 'mem':'2000', 'hdd':'40'},
    ]
}

df = pd.read_csv('sample_data/bike_rental_status.csv')
data2 = {
    "fields": df.columns.tolist(),
    "data": df.to_dict('records')
}

# CORS(app)

@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/rest/get')
def rest_get():
    return jsonify(data)
  

@app.route('/rest/set', methods = ['POST'])
def rest_set():
    req = request.get_json()
    print(req)
    for idx in range(len(data["data"])):
        if(data["data"][idx]['host'] == req["key"]):
            data["data"][idx] = req["row"]
            break
    return jsonify(req)


@app.route('/rest/table', methods=['GET', 'POST'])
def table():
    if request.method == 'POST':
        req = request.get_json()
        print(req)
        #dataframe으로 변환후 머지할 것
        #for idx in range(len(data2["data"])):
        #    if(data2["data"][idx]['host'] == req["key"]):
        #        data2["data"][idx] = req["row"]
        #    break
        return jsonify(req)
    else:
        return jsonify(data2)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8080)