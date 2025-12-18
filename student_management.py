students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    students[roll] = {"Name": name, "Branch": branch}
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
    else:
        for roll, details in students.items():
            print(f"Roll: {roll}, Name: {details['Name']}, Branch: {details['Branch']}")

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        name = input("Enter new name: ")
        branch = input("Enter new branch: ")
        students[roll] = {"Name": name, "Branch": branch}
        print("Student updated successfully!")
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student
