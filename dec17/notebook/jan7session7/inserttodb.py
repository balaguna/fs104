#insert 
insert_query = """ INSERT INTO users (id, firstname, lastname) VALUES (1, 'Bala', ' Murali')"""
cursor.execute(insert_query)
connection.commit()
print("1 Record inserted successfully")
