
# import our application
# Run our application
from schematic_restapi import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(port=3001, debug=True)
