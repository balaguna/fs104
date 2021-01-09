import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(user="postgres",
                                  password="venmathi4",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="FS104")


cursor = connection.cursor()
    # SQL query to create a new table
create_table_query = '''CREATE TABLE todolist
          (
          task varchar,
          priority varchar,
          due varchar,
          CONSTRAINT primary_key PRIMARY KEY (id)
          ); '''

select_query = "select * from todolist"
cursor.execute(select_query)
data_fetched_from_db = cursor.fetchall()
print("data from table", data_fetched_from_db)

if(connection):
    connection.close()