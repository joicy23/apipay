import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]}})

# Rota da API
@app.route('/api/invoices', methods=['POST'])
def create_invoice():
    # URL da API da Iugu
    url = "https://api.iugu.com/v1/invoices?api_token=FD3F026A78FEA4E11BC81A51483934B310805E21E4B1F8FFC74DD633E3C70EFA"

    # Cabeçalhos da requisição
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Host": "api.iugu.com"
    }

    # Obtém o corpo da requisição da solicitação
    raw_data = request.data

    try:
        # Envia a requisição POST com o corpo fornecido
        response = requests.post(url, headers=headers, data=raw_data)

        # Verifica se a resposta foi bem-sucedida (código 200)
        if response.status_code == 200:
            # Converte a resposta para JSON
            result = response.json()
            return jsonify(result), 200
        else:
            return jsonify({"error": "Erro ao fazer a requisição"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
