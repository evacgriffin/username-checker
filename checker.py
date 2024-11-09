# Author:       Eva Griffin
# Description:  Microservice that keeps a database of username, adds new usernames
#               to the database, and checks is a username already exists in the database.

import json
import sqlite3
import zmq


def main():
    # Initialize server socket
    context = zmq.Context()
    server_socket = context.socket(zmq.REP)
    server_socket.bind("tcp://*:5555")

    while True:
        # Wait for client request
        client_msg = server_socket.recv()
        # Decode client binary into a string
        client_string = client_msg.decode('utf-8')
        # Deserialize the client string to a JSON/dict object
        client_json = json.loads(client_string)
        action = client_json["action"]
        username = client_json["username"]
        print(f"Attempting to {action} the username {username}...")

        # Connect to existing database or create new database if it does not exist
        # Database will be created in working directory
        db_connection = sqlite3.connect("usernames.db")

        # Cursor object for executing SQL commands
        db_cursor = db_connection.cursor()

        # Create table in the database if it doesn't exist yet
        db_cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT
        )
        ''')

        if action.lower() == "add":
            # Run search query to check if username already exists
            db_cursor.execute('''
            SELECT * FROM users WHERE (username) = ?
            ''', (username,))
            # Fetch result
            search_result = db_cursor.fetchone()

            # If the specified username already exists, notify client and continue
            # to next loop iteration
            if search_result:
                # Send confirmation to client
                server_socket.send(b"Username already exists. Duplicate username was not added.")
                continue

            # Otherwise, insert new username into the database
            db_cursor.execute('''
            INSERT INTO users (username) VALUES (?)
            ''', (username,))

            # Send confirmation to client
            server_socket.send(b"Username successfully saved to the database.")

        if action.lower() == "delete":
            # Delete the specified username from the database
            db_cursor.execute('''
            DELETE FROM users WHERE (username) = (?)
            ''', (username,))

            # Send confirmation to client
            server_socket.send(b"Username successfully deleted from the database.")

        # Commit the transaction and close the connection
        db_connection.commit()
        db_connection.close()


if __name__ == '__main__':
    main()