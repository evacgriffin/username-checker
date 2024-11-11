# Author:       Eva Griffin
# Description:  Test program that simulates a client communicating with the
#               username-checker microservice.

import json
import zmq


def run_test(client_socket, test_user: dict) -> None:
    """
    Tests the username checker using the specified client socket and test user dictionary.
    :param client_socket: Client socket as a zmq socket
    :param test_user: Test user information as a Python dictionary
    :return: No return value
    """
    action = test_user["action"]
    # Serialize the dictionary to a JSON string
    request_string = json.dumps(test_user)

    # Send request to add the new user to the database
    print(f"Requesting to {action} user...")
    # Encode message to binary to send
    binary_msg = request_string.encode('utf-8')
    client_socket.send(binary_msg)

    # Receive server reply
    server_reply = client_socket.recv()
    # Decode the message
    server_string = server_reply.decode('utf-8')
    print(f"Received reply: {server_string}")


def main():
    # Initialize client socket
    context = zmq.Context()
    print("Connecting to username-checker...")
    client_socket = context.socket(zmq.REQ)
    client_socket.connect("tcp://localhost:5555")

    # TEST ADDING THREE NEW USERS
    # Create list of dictionary/JSON for usernames to be added
    test_users = [
        {"action": "add", "username": "test_user1"},
        {"action": "add", "username": "test_user2"},
        {"action": "add", "username": "test_user3"}
    ]
    for test_user in test_users:
        run_test(client_socket, test_user)

    # -------------------------------------------------
    # TEST ADDING A DUPLICATE USER
    # Create dictionary/JSON for a username to be added
    duplicate_test_user = {
        "action": "add",
        "username": "test_user2"
    }
    run_test(client_socket, duplicate_test_user)

    # -------------------------------------------------
    # TEST DELETING A USER
    # Create dictionary/JSON for a username to be deleted
    delete_test_user = {
        "action": "delete",
        "username": "test_user2"
    }
    run_test(client_socket, delete_test_user)


if __name__ == '__main__':
    main()
