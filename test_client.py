# Author:       Eva Griffin
# Description:  Test program that simulates a client communicating with the
#               username-checker microservice.

import json
import zmq


def main():
    # Initialize client socket
    context = zmq.Context()
    print("Connecting to username-checker...")
    client_socket = context.socket(zmq.REQ)
    client_socket.connect("tcp://localhost:5555")

    # TEST ADDING A NEW USER
    # Create dictionary/JSON for a username to be added
    test_user = {
        "action": "add",
        "username": "test_user1"
    }

    # Serialize the dictionary to a JSON string
    request_string = json.dumps(test_user)

    # Send request to add the new user to the database
    print("Requesting to add user to the database...")
    # Encode message to binary to send
    binary_msg = request_string.encode('utf-8')
    client_socket.send(binary_msg)

    # Receive server reply
    server_reply = client_socket.recv()
    # Decode the message
    server_string = server_reply.decode('utf-8')
    print(f"Received reply: {server_string}")

    # -------------------------------------------------
    # TEST ADDING ANOTHER USER
    # Create dictionary/JSON for a username to be added
    test_user = {
        "action": "add",
        "username": "test_user2"
    }

    # Serialize the dictionary to a JSON string
    request_string = json.dumps(test_user)

    # Send request to add the new user to the database
    print("Requesting to add user to the database...")
    # Encode message to binary to send
    binary_msg = request_string.encode('utf-8')
    client_socket.send(binary_msg)

    # Receive server reply
    server_reply = client_socket.recv()
    # Decode the message
    server_string = server_reply.decode('utf-8')
    print(f"Received reply: {server_string}")

    # -------------------------------------------------
    # TEST ADDING ANOTHER USER
    # Create dictionary/JSON for a username to be added
    test_user = {
        "action": "add",
        "username": "test_user3"
    }

    # Serialize the dictionary to a JSON string
    request_string = json.dumps(test_user)

    # Send request to add the new user to the database
    print("Requesting to add user to the database...")
    # Encode message to binary to send
    binary_msg = request_string.encode('utf-8')
    client_socket.send(binary_msg)

    # Receive server reply
    server_reply = client_socket.recv()
    # Decode the message
    server_string = server_reply.decode('utf-8')
    print(f"Received reply: {server_string}")

    # -------------------------------------------------
    # TEST ADDING A DUPLICATE USER
    # Create dictionary/JSON for a username to be added
    test_user = {
        "action": "add",
        "username": "test_user2"
    }

    # Serialize the dictionary to a JSON string
    request_string = json.dumps(test_user)

    # Send request to add the new user to the database
    print("Requesting to add user to the database...")
    # Encode message to binary to send
    binary_msg = request_string.encode('utf-8')
    client_socket.send(binary_msg)

    # Receive server reply
    server_reply = client_socket.recv()
    # Decode the message
    server_string = server_reply.decode('utf-8')
    print(f"Received reply: {server_string}")

    # -------------------------------------------------
    # TEST DELETING A USER
    # Create dictionary/JSON for a username to be deleted
    test_user = {
        "action": "delete",
        "username": "test_user2"
    }

    # Serialize the dictionary to a JSON string
    request_string = json.dumps(test_user)

    # Send request to add the new user to the database
    print("Requesting to delete user from the database...")
    # Encode message to binary to send
    binary_msg = request_string.encode('utf-8')
    client_socket.send(binary_msg)

    # Receive server reply
    server_reply = client_socket.recv()
    # Decode the message
    server_string = server_reply.decode('utf-8')
    print(f"Received reply: {server_string}")


if __name__ == '__main__':
    main()
