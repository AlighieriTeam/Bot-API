from flask import Flask, request, jsonify
import socketio as sio

from API.User.event_handlers import register_events

app = Flask(__name__)
sio_client = sio.Client()

register_events(sio_client)

ROOM = "3658"
TOKEN = "LBELEVRLZI"
user_json = None
from_website_json = None

@app.route('/json_receiver_user', methods=['POST'])
def receive_json():
    try:
        json_data = request.json
        global user_json
        user_json = json_data
        print("Received JSON:", json_data)
        return '', 200
    except Exception as e:
        return str(e), 500


@app.route('/json_sender_user', methods=['GET'])
def send_json():
    global from_website_json
    data = from_website_json
    from_website_json = None
    return jsonify(data), 200


if __name__ == '__main__':
    sio_client.connect("http://127.0.0.1:5000")
    sio_client.emit("bot_connect", {"room": ROOM, "token": TOKEN})
    # app.run(host='0.0.0.0', port=7000)
