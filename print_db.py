# Author:       Eva Griffin
# Description:  Script to print out current contents of the username database.
#               Can be used for visualization or debugging purposes.

import sqlite3


def main():
    # Connect to existing database or create new database if it does not exist
    # Database will be created in working directory
    db_connection = sqlite3.connect("usernames.db")

    # Cursor object for executing SQL commands
    db_cursor = db_connection.cursor()

    tbl_name = "users"
    # Check if the table exists
    db_cursor.execute('''
    SELECT name FROM sqlite_master
    WHERE type='table' AND name=?
    ''', (tbl_name,))
    # Fetch result
    table = db_cursor.fetchone()

    if not table:
        print(f"The {tbl_name} table does not exist.")
        return

    # Otherwise, fetch all data from the table
    db_cursor.execute('''
    SELECT * FROM users
    ''')
    result = db_cursor.fetchall()

    # If there is no data
    if not result:
        print(f"The {tbl_name} table is empty.")
        return

    # Otherwise, print the result
    for user in result:
        print(f"{user[0]}: {user[1]}")

    # Close database connection
    db_connection.close()


if __name__ == '__main__':
    main()
