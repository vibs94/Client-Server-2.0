from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
# from flask.ext.jsonpify import jsonify
app = Flask(__name__)
api = Api(app)

class Image(Resource):
    def get(self):
        result = {'image': 'defect'} # Fetches first column that is Employee ID
        return jsonify(result)

api.add_resource(Image, '/image') # Route_1

if __name__ == '__main__':
     app.run(port='5001')