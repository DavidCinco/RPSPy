import sqlite3
from sqlite3 import Error, Cursor

#Database Class
class SqlQueries:
    
    def create_connection(db_path):
        connection = None
        try:
            connection = sqlite3.connect(db_path)
        except Error as e:
            print(f"Found an Error as '{e}'")
        return connection

    #Execute query 
    def create_table(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed succesfully")
        except Error as e:
            print(f"The error '{e}' occurred")
