#
# import psycopg2
#from psycopg2 import Error
#
#connection = psycopg2.connect(user="postgres",
 #                                 password="venmathi4",
  #                                host="127.0.0.1",
   #                               port="5432",
    #                              database="FS104")
#


##Executemany
#users = (
#(3, 'Allen', 'Iverson'),
#(4, 'Ayrton', 'Senna')

#)

#insert_query = "INSERT INTO users (id, firstname, lastname) VALUES (%s, %s, %s)"
#cursor.executemany(insert_query, users)

#
# select_query = "select * from users"
#cursor.execute(select_query)
#data_fetched_from_db = cursor.fetchall()
#print("data from table", data_fetched_from_db)

#if(connection):
#    connection.close()
