from flask import Flask, jsonify
from flask_restful import Resource, Api

from api.main import api_bp

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return jsonify({'hello': 'world'})


api.add_resource(HelloWorld, '/hello2')

app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)
