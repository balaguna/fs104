import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(user="postgres",
                                  password="password",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="FS104")


cursor = connection.cursor()
    # SQL query to create a new table
create_table_query = '''CREATE TABLE users
          (
              id integer     NOT NULL,
          firstname varchar,
          lastname varchar,
          CONSTRAINT primary_key PRIMARY KEY (id)
          ); '''


#executemany
users = (
(3, 'Allen', 'Iverson'),
(4, 'Ayrton', 'Senna')

)

insert_query = "INSERT INTO users (id, firstname, lastname) VALUES (%s, %s, %s)"
cursor.executemany(insert_query, users)

select_query = "select * from users ORDER BY users"
cursor.execute(select_query)
data_fetch_from_db = cursor.fetchall()
#print data one by one
for data in data_fetch_from_db:
    print("Ordered Date: ", data)

if(connection):
    connection.close()