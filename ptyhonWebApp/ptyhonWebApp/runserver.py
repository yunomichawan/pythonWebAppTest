import os
from HelloFlask import app    # Imports the code from HelloFlask/__init__.py

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')

    try:
        PORT = int(os.environ.get('SERVER_PORT', '4449'))
    except ValueError:
        PORT = 4449

    app.run(HOST, PORT)