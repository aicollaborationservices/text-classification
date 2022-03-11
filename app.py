import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import yaml

app = Flask(__name__)
cors = CORS(app)


API_V1 = '/api/1.0'

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "status": "it works"
    })

@app.route(API_V1 + '/ping', methods=['GET'])
def ping():
    return "pong"

@app.route(API_V1 + '/definition', methods=['GET'])
def definition():
    with open("./openapi.yml", 'r') as stream:
        try:
            return jsonify(yaml.safe_load(stream))
        except yaml.YAMLError as exception:
            return jsonify(exception)

@app.route(API_V1 + '/info', methods=['GET'])
def info():
    return jsonify({
        'version': API_V1,
        'project': 'aicollaboration',
        'service': 'hello-service',
        'language': 'python',
        'type': 'api',
        'date': str(datetime.datetime.now()),
    })


@app.route(API_V1 + '/predict', methods=['POST', 'OPTIONS'])
@cross_origin(origin='localhost')
def predict():
    data = request.json
    
    return jsonify({ 'data': data })
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)