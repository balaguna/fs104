import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="KA180990",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="Employee Management System")

    connection.autocommit = True

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query = ''' CREATE TABLE IF NOT EXISTS TASKS
                             (
                             TASK_ID SERIAL NOT NULL,
                             TITLE VARCHAR(50) NOT NULL,
                             DESCRIPTION VARCHAR(50) NOT NULL,
                             PRIORITY VARCHAR(50) NOT NULL,
                             DUE_DATE DATE NOT NULL,
                             PRIMARY KEY (TASK_ID)
                             ); '''

    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    print("Table created successfully in PostgreSQL")

    data = (
        (1, "Task 1", "Task 1 Desc", "Medium", "2021-01-09"),
        (2, "Task 2", "Task 2 Desc", "High", "2021-01-11"),
        (3, "Task 3", "Task 3 Desc", "High", "2021-01-12"),
        (4, "Task 4", "Task 4 Desc", "Low", "2021-01-13"),
        (5, "Task 5", "Task 5 Desc", "Medium", "2021-01-14"),
        (6, "Task 6", "Task 6 Desc", "High", "2021-01-09"),
        (7, "Task 7", "Task 7 Desc", "Low", "2021-01-09"),
        (8, "Task 8", "Task 8 Desc", "High", "2021-01-20"),
        (9, "Task 9", "Task 9 Desc", "Medium", "2021-01-12"),
        (10, "Task 10", "Task 10 Desc", "Low", "2021-01-10"),
    )

    insert_query = ''' INSERT INTO TASKS (TASK_ID, TITLE, DESCRIPTION, PRIORITY, DUE_DATE) VALUES (%s, %s, %s, %s, %s); '''
    cursor.executemany(insert_query, data)
    print("Table data inserted successfully in PostgreSQL")

    fetch_duetoday = "select * from TASKS where due_date = current_date"
    cursor.execute(fetch_duetoday)
    record = cursor.fetchall()
    for data in record:
        print("Data today is -", data)

    outputfile = open('task.csv', 'w')

    fetch_priority = "select * from TASKS where priority='High'"
    cursor.execute(fetch_priority)
    record = cursor.fetchall()

    for data in record:
        print("Data with high priority is -", data[1])
        increment = 0
        for column in data:
            if increment < len(data) - 1:
                outputfile.write(str(column) + "|")
                increment = increment + 1
            else:
                outputfile.write(str(column))
                increment = increment + 1
        outputfile.write("\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
