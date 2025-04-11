"""
Student Management System
This program allows you to manage student enrollment in a course.
It includes functionalities to add students, enroll them, drop them, and view their information.
It uses a class-based approach to encapsulate student data and methods.

Author: Md Majharul Islam
Email: majharul.live@gmail.com
Date: 2023-10-01
Version: 1.0

"""

# Student database class to manage student records
class StudentDatabase:
    _student_list = []  # Protected student list

    # Method add students to the database
    @classmethod
    def add_student(self, student):
        self._student_list.append(student)

    # Method to view all students
    @classmethod
    def find_student_by_id(self, student_id):
        for student in self._student_list:
            if student._Student__student_id == student_id:
                return student
        return 


# Student class to represent individual student
class Student:
    def __init__(self, student_id, name, department):
        self.__student_id = student_id      # Private attribute
        self.__name = name                  # Private attribute
        self.__department = department      # Private attribute
        self.__is_enrolled = False          # Private attribute

    # Methods to manage student enrollment
    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f"{self.__name} has been successfully enrolled.")
        else:
            print(f"{self.__name} is already enrolled.")

    # Method to drop student from the course
    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f"{self.__name} has been dropped from the course.")
        else:
            print(f"{self.__name} is not enrolled.")

    # Method to view student information
    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"
        print(f"Student ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        print(f"Enrollment Status: {status}")
        print("-" * 30)


# Functions to enroll and drop students by ID
def enroll_student_by_id():
    try:
        student_id = int(input("Enter Student ID to Enroll: "))
        student = StudentDatabase.find_student_by_id(student_id)
        if student:
            student.enroll_student()
        else:
            print("Student not found!")
    except:
        print("Something went wrong!")


# Function to drop student by ID
def drop_student_by_id():
    try:
        student_id = int(input("Enter Student ID to Drop: "))
        student = StudentDatabase.find_student_by_id(student_id)
        if student:
            student.drop_student()
        else:
            print("Student not found!")
    except:
        print("Something went wrong!")


# Sample students
s1 = Student(101, "Majharul Islam", "CSE")
s2 = Student(102, "Shakib Al Hasan", "EEE")
s3 = Student(103, "Tamim Iqbal", "BBA")

# Adding sample students to the database
StudentDatabase.add_student(s1)
StudentDatabase.add_student(s2)
StudentDatabase.add_student(s3)


# Menu system for user interaction
while True:
    print("===== Student Management Menu =====")
        
    options = [
        "1. View All Students",
        "2. Enroll Student",
        "3. Drop Student",
        "4. Exit"
    ]

    for option in options:
        print(option)
            
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("\n--- All Students ---")
        for student in StudentDatabase._student_list:
            student.view_student_info()
    elif choice == '2':
        enroll_student_by_id()
    elif choice == '3':
        drop_student_by_id()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.\n")
