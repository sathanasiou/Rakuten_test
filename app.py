import flask
import requests
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/find_company/<mac_address>', methods=['GET'])
def get_company_name(mac_address):
    params_api = {'search': mac_address}
    resp = requests.get(
        'https://api.macaddress.io/v1?apiKey=at_ltSRqlCMjRPtFhkcaqkJAhXwHNUYc&output=json', params=params_api)

    if resp.status_code == 200:
        data = resp.json()
        dict2 = data["vendorDetails"]
        print(dict2['companyName'])
        return jsonify('company:' + dict2['companyName'],resp.status_code)
    else:
        return jsonify('message: error MAC Address does not belong to any Company',resp.status_code)

app.run()
