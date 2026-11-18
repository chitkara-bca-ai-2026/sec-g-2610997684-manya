
def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def display_student(roll, student):
    total, average = calculate_results(student["marks"])
    print(f"Roll No: {roll} | Name: {student['name']} | Marks: {student['marks']} | Total: {total} | Average: {average:.2f}%")

def add_student(records, roll, name, marks):
    if roll in records:
        print(f"[ERROR] Roll number {roll} already exists.")
    else:
        records[roll] = {"name": name, "marks": marks}
        print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) added successfully.")


students = {
    "101": {"name": "Harshita", "marks": [85, 90, 78]},
    "102": {"name": "Manya", "marks": [92, 94, 95]},
    "103": {"name": "Nishtha", "marks": [74, 80, 82]}
}

while True:
    print(" STUDENT RECORDS MANAGEMENT SYSTEM")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        print("All Student Records")
        for roll, student in students.items():
            display_student(roll, student)
        print(f"Total Students: {len(students)}")

    elif choice == "2":
        print("Add New Student")
        roll = input("Enter Roll Number: ").strip()
        name = input("Enter Student Name: ").strip()
        m1 = int(input("Subject 1: "))
        m2 = int(input("Subject 2: "))
        m3 = int(input("Subject 3: "))
        add_student(students, roll, name, [m1, m2, m3])

    elif choice == "3":
        print("Search Student")
        roll = input("Enter Roll Number to search: ").strip()
        student = students.get(roll)
        if student:
            print("[RECORD FOUND]")
            display_student(roll, student)
        else:
            print(f"[ERROR] No student found with Roll Number '{roll}'.")

    elif choice == "4":
        print("\nThank you for using the Student Records System. Goodbye!")
        break

    else:
        print("Invalid choice, please enter a number from 1 to 4.")