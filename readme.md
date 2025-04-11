# Student Management System

## Description

The **Student Management System** allows you to manage student enrollment in a course. This program provides functionalities to:

- Add students to the system
- Enroll students in a course
- Drop students from the course
- View student information

It uses a class-based approach to encapsulate student data and methods. The system supports adding students, enrolling and dropping them from courses, and viewing their status.

## Author

- **Md Majharul Islam**
- Email: [majharul.live@gmail.com](mailto:majharul.live@gmail.com)

## Date

- **April 4, 2025**

## Version

- **1.0**

## Clone this repository using the following command:

```bash
git clone https://github.com/majharul-web/student-management.git
```

---

## Features

- **Add Student**: Adds students to the system's student database.
- **Enroll Student**: Enrolls a student in the course (if not already enrolled).
- **Drop Student**: Drops a student from the course (if they are enrolled).
- **View Student Info**: Displays student details, including their enrollment status.

---

## Classes

### `StudentDatabase`

This class manages the student database. It includes methods to add students and find a student by their ID.

#### Methods:

- `add_student(student)`: Adds a student to the database.
- `find_student_by_id(student_id)`: Finds a student by their student ID.

### `Student`

This class represents an individual student. It includes methods to enroll, drop, and view student information.

#### Methods:

- `enroll_student()`: Enrolls the student in the course.
- `drop_student()`: Drops the student from the course.
- `view_student_info()`: Displays the student's ID, name, department, and enrollment status.

---

## Functions

### `enroll_student_by_id()`

Prompts the user to enter a student ID and enrolls the student if found.

### `drop_student_by_id()`

Prompts the user to enter a student ID and drops the student if found.

---

## How to Use

1. Run the program.
2. Choose an option from the menu:
   - **1**: View all students.
   - **2**: Enroll a student by their ID.
   - **3**: Drop a student by their ID.
   - **4**: Exit the program.

---

## Sample Output

```plaintext
===== Student Management Menu =====
1. View All Students
2. Enroll Student
3. Drop Student
4. Exit
Enter your choice (1-4): 1

--- All Students ---
Student ID: 101
Name: Majharul Islam
Department: CSE
Enrollment Status: Not Enrolled
------------------------------
Student ID: 102
Name: Shakib Al Hasan
Department: EEE
Enrollment Status: Not Enrolled
------------------------------
Student ID: 103
Name: Tamim Iqbal
Department: BBA
Enrollment Status: Not Enrolled
------------------------------

Enter Student ID to Enroll: 101
Majharul Islam has been successfully enrolled.
```
