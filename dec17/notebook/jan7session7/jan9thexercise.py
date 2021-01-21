import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(user="postgres",
                                  password="venmathi4",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="FS104")


cursor = connection.cursor()
    # SQL query to create a new table
create_table_query = '''CREATE TABLE tasks
          (
              id integer     NOT NULL,
          firstname varchar,
          lastname varchar,
          CONSTRAINT primary_key PRIMARY KEY (id)
          ); '''

#autocommit
connection.autocommit = True






select_query = "select * from tasks ORDER BY tasks"
cursor.execute(select_query)
data_fetch_from_db = cursor.fetchall()
#print data one by one
for data in data_fetch_from_db:
    print("Ordered Date: ", data)

if(connection):
    connection.close()