import json
import requests


def main():
    try:
        # Define the Flask JSON receiver URL
        url_send_to_website = "http://localhost:5000/json_receiver_user"
        # Define the Flask JSON sender URL
        url_receive_from_website = "http://localhost:5000/json_sender_user"
        # Create a JSON object to send
        data = {
            "action": "up"
        }

        # Send the JSON data
        response_send = requests.post(url_send_to_website, json=data)
        # Receive JSON
        response_get = requests.get(url_receive_from_website)

        # Get the response from the Flask server
        response_code = response_send.status_code
        print("Response Send Code:", response_code)
        response_code = response_get.status_code
        print("Response Get Code:", response_code)
        # Read the response
        response_data = response_get.json()

        # Print the response
        print("Response:", response_data)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
