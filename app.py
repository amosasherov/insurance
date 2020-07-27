from flask import Flask, request
from flask_socketio import SocketIO
from calculator_functions import calc_func as cf


app = Flask(__name__)
socketio = SocketIO(app)

app.debug = True


@app.route('/life', methods=['POST'])
def result():
    data = request.get_json()
    sum = 0
    if data["kids"] is not None:
        kid = cf().offspring(data["kids"], data["income"])
        sum += kid
    if data["dependants"] is not None:
        depends = cf().eldery(data["dependants"])
        for dep in depends:
            sum += depends[dep]
    sum = sum * 0.75
    return {"inc_to_buy" : sum}


@app.route('/health', methods=['POST'])

@socketio.on('form')
def get_form():
    pass

if __name__ == '__main__s'
socketio.run(app)
