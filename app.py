import json
import requests
import os
from os import path

from flask import Flask, request


app = Flask(__name__)

# This is the code for Container 1:
# 1. Store the data in file
# 2. Calculate the amount of given product


def validate_request(payload):
    if payload and "file" in payload and payload['file'] is not None and payload['file'] != "":
        return True
    return False


def validate_file_data(payload):
    if payload and "file" in payload and payload['file'] is not None and payload['file'] != "" and \
            payload['data'] and payload["data"][:15] == "product, amount":
        return True
    return False


@app.route('/calculate', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    if validate_request(data):
        if path.exists("/Ronil_PV_dir/" + data['file']):
            res = requests.post("http://hello2service:80/calculate_sum", json=data)
            return json.loads(res.text)
        else:
            return json.loads('{"file": "' + data['file'] + '", "error": "File not found."}')
    else:
        return json.loads('{"file": null, "error": "Invalid JSON input."}')


@app.route('/store-file', methods=['POST'])
def store_file_to_persistent():
    data = request.get_json()

    if validate_file_data(data):
        try:
            with open("/Ronil_PV_dir/" + data.get("file"), "w") as f:
            # with open("/home/" + data.get("file"), "w") as f:
                f.write(data.get("data"))
            return json.loads(
                '{"file": "' + data.get("file") + '", "message": "Success."}')
        except:
            return json.loads('{"file": "' + data.get("file") + '", "error": "Error while storing the file to the storage."}')
    else:
        return json.loads('{"file": null, "error": "Invalid JSON input."}')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
