
import connexion
from flask import Flask, jsonify
from schematic.utils import general


def create_app():
    connexionapp = connexion.FlaskApp(__name__, specification_dir='openapi/')
    connexionapp.add_api('api.yaml')
    app = connexionapp.app
    # app = Flask(__name__)

    # Configuration
    # init_config()

    # Handle extensions
    # init_extensions()

    # Handle app routes
    init_app_routes(app)

    print(app.url_map)

    return app



def init_app_routes(app):
    @app.route('/')
    def index():
        # Do stuff
        # result = general.dict2list()
        # Format response
        return jsonify({'content': 'ROOT'})
 
    @app.route('/manifest/generate/{id}', methods=['POST'])
    def manifest_generate():
        # Do stuff
        # result = general.dict2list()
        # Format response
        return jsonify({'content': 'ROOT'})

    @app.route('/manifest/generate', methods=['GET'])
    def get_manifest():
        # Do stuff
        # result = general.dict2list()
        # Format response
        return jsonify({'content': 'ROOT'})

    @app.route('/hello_world')
    def hello():
        return jsonify({'content': 'Hello World'})

    @app.route('/hello_world/{name}')
    def hello_name(name):
        print(name)
        # Do work as input

        # Doing work...

        # Format response
        return jsonify({'content': 'Hello World'})
