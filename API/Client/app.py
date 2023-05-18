from flask import Flask, request, jsonify

app = Flask(__name__)
TOKEN = None
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
    app.run(host='0.0.0.0', port=5000)
