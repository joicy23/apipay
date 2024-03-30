import requests
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]}})

@app.route('/obter_json/<invoice_id>', methods=['GET'])
def obter_json(invoice_id):
    api_token = "FD3F026A78FEA4E11BC81A51483934B310805E21E4B1F8FFC74DD633E3C70EFA"
    url = f"https://api.iugu.com/v1/invoices/{invoice_id}?api_token={api_token}"

    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        return jsonify(json_data)
    else:
        return "Erro ao obter o JSON", response.status_code

if __name__ == '__main__':
    app.run(debug=True)
