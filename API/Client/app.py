from flask import Flask, request, jsonify
import threading
import time

app = Flask(__name__)
data_queue = []
token = ""


@app.route('/json receiver_user', methods=['POST'])
def json_receiver():
    data = request.get_json()
    return 'JSON received'


@app.route('/json sender_user', methods=['GET'])
def json_sender():
    if len(data_queue) > 0:
        data = data_queue.pop(0)
        return jsonify(data)
    else:
        return jsonify({})


def send_json_periodically():
    while True:
        json_data = {'message': 'Hello from JSON sender'}
        data_queue.append(json_data)

        time.sleep(5)


sender_thread = threading.Thread(target=send_json_periodically)
sender_thread.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
