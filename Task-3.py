import mysql.connector


'''
This is the steps for making database of the student e.g. Student_profile

host="localhost"
user="root"
password="999999999aA@"

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)

cursor = connection.cursor()

database_name = "Student_profile"

cursor.execute(f"CREATE DATABASE {database_name}")

print(f"Database {database_name} created successfully")

cursor.close()
connection.close()
'''

host="localhost"
user="root"
password="999999999aA@"
database_name="Student_profile"

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database_name
)

cursor = connection.cursor()


# Creating table here
table_creation_query = '''
CREATE TABLE IF NOT EXISTS students(
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    grade FLOAT
)
'''

cursor.execute(table_creation_query)
print("Table created successfully")


#inserting data in table
insert_query = """INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"""

student_data = ("Alice", "Smith", 18, 95.5)

cursor.execute(insert_query, student_data)
connection.commit()
print("Data Submitted Successfully")


# Updating table data
update_query = """UPDATE students SET grade = %s WHERE first_name = %s"""
new_data = (97.0, "Alice")

cursor.execute(update_query, new_data)
connection.commit()
print("Data Updated successfully")


# Deleting table data
delete_query = """DELETE FROM students WHERE last_name = %s"""
delete_data = ("Smith",)

cursor.execute(delete_query,delete_data)
connection.commit()
print("Data deleted successfully")


#fetching table data
selecting_query = """SELECT * FROM students"""

cursor.execute(selecting_query)
total_data = cursor.fetchall()

if total_data:
    print("\nStudent Records:")
    for data in total_data:
        print(data)
else:
    print("No student records found.")

# Closing the cursor and connection
cursor.close()
connection.close()

