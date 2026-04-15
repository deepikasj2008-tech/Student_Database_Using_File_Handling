import csv
FILE_NAME = "students(2).csv"
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([sid, name, marks])
    print(" Student added successfully!")
def view_students():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            print("Student Records:")
            for row in reader:
                print(row)
            print()
    except FileNotFoundError:
        print(" File not found!")
def search_student():
    sid = input("Enter Student ID to search: ")
    found = False
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == sid:
                print(" Student Found:", row)
                found = True
                break
    if not found:
        print(" Student not found!")
while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        print(" Exiting Program...")
        break
    else:
        print("Invalid choice! Try again.")
