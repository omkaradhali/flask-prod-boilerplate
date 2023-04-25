from flask import Flask, request, jsonify
from config.load_config import load_config
import util.constants as const
import os


def create_app():

    app = Flask(__name__)
    load_config(app)

    @app.route('/', methods=['GET'])
    def heartbeat():
        return jsonify({'message': 'server is up', 'env': os.getenv('ENV')})

    @app.route('/user/<name>')
    def user(name):
        return "Hello, {}".format(name)

    @app.route('/post', methods=['POST'])
    def post():
        data = request.get_json()
        print(data)
        return data['message']

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(
        host="0.0.0.0", port=application.config[const.PORT], debug=application.config[const.DEBUG])
