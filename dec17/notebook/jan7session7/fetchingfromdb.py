
#fetching and displaying one by one
select_query = "select * from users ORDER BY users"
cursor.execute(select_query)
data_fetch_from_db = cursor.fetchall()
for data in data_fetch_from_db:
    print("Ordered Date: ", data)
