import json
import os

def add_students(students):
    student = {}
    name = input("Enter students name: ").strip()
    if not name:
        print("Name can't be empty!")
        return
    if any(student['name'] == name for student in students):
        print("Such student already exists!")
        return
    else:
        try:
            grades_input = input("Enter grades separated by comma: ")
            grades = list(map(int, grades_input.split(',')))
            age = int(input("Enter the age of student: "))
            student['name'] = name
            student['age'] = age
            student['grade'] = grades
            students.append(student)
            print(f"Student {name} was added.")
        except ValueError:
            print("Error. Age and grades should be a numbers!")

def del_students(students):
    if students:
        print(f"List of students: {[student['name'] for student in students]}")
        student_name = input("Who you want to delete?: ")
        for student in students:
            if student['name'] == student_name:
                students.remove(student)
                print(f"{student_name} was deleted!")
                break
        else:
            print(f"Student with name {student_name} is not found.")
    else:
        print("No students to delete!")

def show_students(students):
    if students:
        print("Students list: ")
        for student in students:
            print(f"{student['name']}, {student['age']} years old, grades: {student['grade']}")
    else:
        print("Student list is empty!")

def save_students(students):
    with open("students.json", "w", encoding='utf-8') as file:
        json.dump(students, file, ensure_ascii=False, indent=4)
        print("Students are saved!")

def main():
    if os.path.exists("students.json"):
        try:
            with open('students.json', encoding='utf-8') as file:
                students = json.load(file)
                print(f"File is found. Students in list: {students}")
        except json.JSONDecodeError:
            print("Error: file is broken. Starting with empty register.")
            students = []
    else:
        print("Register is empty, no file detected.")
        students = []
    while True:
        print("Welcome to the student record book!")
        user_options = input("What you want to do?(Add/Delete/Show/Save/Exit): ").strip().lower()

        if user_options == 'add':
            add_students(students)
        elif user_options == 'delete':
            del_students(students)
        elif user_options == 'show':
            show_students(students)
        elif user_options == 'save':
            save_students(students)
        elif user_options == 'exit':
            print("Information was saved. You have exited the program")
            break
        else:
            print("Such command does not exist!")

if __name__ == "__main__":
    main()