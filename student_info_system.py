import mysql.connector

def add_student(first_name, last_name, dob, gender, contact_number, email, department):
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(host='localhost',
                                             database='student_info',
                                             user='root',
                                             password='your_password')
        cursor = connection.cursor()

        # Insert the student data
        query = """INSERT INTO students (first_name, last_name, date_of_birth, gender, contact_number, email, department)
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        data = (first_name, last_name, dob, gender, contact_number, email, department)
        cursor.execute(query, data)

        # Commit the transaction
        connection.commit()

        print("Student added successfully.")

    except mysql.connector.Error as error:
        print(f"Failed to add student: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
def view_students():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='student_info',
                                             user='root',
                                             password='your_password')
        cursor = connection.cursor()

        # Select all students
        query = "SELECT * FROM students"
        cursor.execute(query)

        # Fetch and display the data
        students = cursor.fetchall()
        for student in students:
            print(student)

    except mysql.connector.Error as error:
        print(f"Failed to retrieve students: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
def update_student(student_id, contact_number, email):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='student_info',
                                             user='root',
                                             password='your_password')
        cursor = connection.cursor()

        # Update student data
        query = """UPDATE students 
                   SET contact_number = %s, email = %s 
                   WHERE student_id = %s"""
        data = (contact_number, email, student_id)
        cursor.execute(query, data)

        connection.commit()
        print("Student updated successfully.")

    except mysql.connector.Error as error:
        print(f"Failed to update student: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
def delete_student(student_id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='student_info',
                                             user='root',
                                             password='your_password')
        cursor = connection.cursor()

        # Delete the student
        query = "DELETE FROM students WHERE student_id = %s"
        cursor.execute(query, (student_id,))

        connection.commit()
        print("Student deleted successfully.")

    except mysql.connector.Error as error:
        print(f"Failed to delete student: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
def enroll_student(student_id, course_id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='student_info',
                                             user='root',
                                             password='your_password')
        cursor = connection.cursor()

        # Insert into enrollments table
        query = """INSERT INTO enrollments (student_id, course_id, enrollment_date)
                   VALUES (%s, %s, CURDATE())"""
        cursor.execute(query, (student_id, course_id))

        connection.commit()
        print("Student enrolled in course successfully.")

    except mysql.connector.Error as error:
        print(f"Failed to enroll student: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
def view_enrollments():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='student_info',
                                             user='root',
                                             password='your_password')
        cursor = connection.cursor()

        # Select all enrollments
        query = """SELECT s.first_name, s.last_name, c.course_name, e.enrollment_date
                   FROM students s
                   JOIN enrollments e ON s.student_id = e.student_id
                   JOIN courses c ON e.course_id = c.course_id"""
        cursor.execute(query)

        # Fetch and display the data
        enrollments = cursor.fetchall()
        for enrollment in enrollments:
            print(enrollment)


    except mysql.connector.Error as error:
        print(f"Failed to retrieve enrollments: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
