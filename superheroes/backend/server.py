from .db import get_all, delete, create
from flask import Flask, request
from json import loads, dumps
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/superheroes', methods=['GET'])
def superheroes():
    return dumps(get_all())

@app.route('/superheroes', methods=['POST'])
def create_hero():
    req = loads(request.data)
    idx = create(req[0], req[1])
    return str(idx)


@app.route('/superheroes/<idx>', methods=['DELETE'])
def delete_hero(idx):
    delete(idx)
    return ''

if __name__ == '__main__':
    app.run()