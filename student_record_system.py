import os
import json

class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def to_dict(self):
        return {'roll': self.roll, 'name': self.name, 'marks': self.marks}

def add_student(students):
    try:
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        student = Student(roll, name, marks)
        students.append(student)
        print("Student added successfully!\n")
    except ValueError:
        print("Invalid marks. Please enter numeric value.")

def display_students(students):
    if not students:
        print("No student records found.\n")
    for s in students:
        print(f"Roll: {s.roll}, Name: {s.name}, Marks: {s.marks}")

def search_student(students):
    roll = input("Enter Roll No to search: ")
    found = False
    for s in students:
        if s.roll == roll:
            print(f"Found: Roll: {s.roll}, Name: {s.name}, Marks: {s.marks}")
            found = True
            break
    if not found:
        print("Student not found.\n")

def delete_student(students):
    roll = input("Enter Roll No to delete: ")
    for i, s in enumerate(students):
        if s.roll == roll:
            del students[i]
            print("Student deleted successfully.\n")
            return
    print("Student not found.\n")

def save_to_file(students):
    with open("students.json", "w") as f:
        json.dump([s.to_dict() for s in students], f)
    print("Records saved to students.json\n")

def load_from_file():
    if not os.path.exists("students.json"):
        return []
    with open("students.json", "r") as f:
        data = json.load(f)
        return [Student(d['roll'], d['name'], d['marks']) for d in data]

def main():
    students = load_from_file()

    while True:
        print("\n1. Add Student\n2. Display Students\n3. Search Student\n4. Delete Student\n5. Save to File\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            save_to_file(students)
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
