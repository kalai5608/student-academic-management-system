import csv

def get_student_id(students):
    while True:
        try:
            stud_id = int(input("Enter student id: "))
            if stud_id <= 0:
                print("Student ID must be a positive number.")
                continue

            for student in students:
                if student["id"] == stud_id:
                    print("That student ID already exists.")
                    break
            else:
                return stud_id

        except ValueError:
            print("Please enter a valid number.")

def get_existing_id():
    while True:
        try:
            stud_id = int(input("Enter student id: "))
            if stud_id > 0:
                return stud_id

            print("Student ID must be a positive number.")

        except ValueError:
            print("Please enter a valid number.")

def get_name():
    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name

        print("Name cannot be empty.")

def get_department():
    while True:
        department = input("Enter your department: ").strip()
        if department:
            return department

        print("Department cannot be empty.")

def get_year():
    while True:
        try:
            year = int(input("Enter your year of study: "))
            if 1 <= year <= 4:
                return year
            print("Year must be between 1 and 4.")

        except ValueError:
            print("Please enter a valid number.")

def get_mark(subject):
    while True:
        try:
            mark = int(input(f"Enter your {subject} mark: "))
            if 0 <= mark <= 100:
                return mark

            print("Mark must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

def add_student(students):
    stud_id = get_student_id(students)
    name = get_name()
    dept = get_department()
    yr = get_year()
    python = get_mark("Python")
    cpp = get_mark("C++")
    maths = get_mark("Maths")

    new_student = {
        "id": stud_id,
        "name": name,
        "department": dept,
        "year": yr,
        "python": python,
        "C++": cpp,
        "maths": maths
    }
    students.append(new_student)
    print("Student added successfully.")

def view_students(students):
    if not students:
        print("No students found.")
        return

    for student in students:
        print("\n-----------------------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Department:", student["department"])
        print("Year:", student["year"])
        print("Python:", student["python"])
        print("C++:", student["C++"])
        print("Maths:", student["maths"])

def search_student(students):
    if not students:
        print("No students found.")
        return

    search_id = get_existing_id()
    for student in students:
        if student["id"] == search_id:
            print("\nStudent found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Department:", student["department"])
            print("Year:", student["year"])
            print("Python:", student["python"])
            print("C++:", student["C++"])
            print("Maths:", student["maths"])
            return

    print("Student not found.")

def update_student(students):
    if not students:
        print("No students found.")
        return

    search_id = get_existing_id()
    for student in students:
        if student["id"] == search_id:
            print("\nEnter the new details:")
            student["name"] = get_name()
            student["department"] = get_department()
            student["year"] = get_year()
            student["python"] = get_mark("Python")
            student["C++"] = get_mark("C++")
            student["maths"] = get_mark("Maths")
            print("Student updated successfully.")
            return

    print("Student not found.")

def delete_student(students):
    if not students:
        print("No students found.")
        return

    search_id = get_existing_id()
    for student in students:
        if student["id"] == search_id:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")

def calculate_average(student):
    total = student["python"] + student["maths"] + student["C++"]
    avg = total / 3
    print(f"Total marks obtained by {student['name']} = {total}/300")
    print(f"Average = {avg:.2f}")
    return avg

def calculate_grade(student):
    total = student["python"] + student["maths"] + student["C++"]
    avg = total / 3

    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

def class_statistics(students):
    if not students:
        print("No students found.")
        return

    total = 0
    no = len(students)
    highest_student = None
    lowest_student = None
    highest_avg = -1
    lowest_avg = 101

    grade_count = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }
    for student in students:
        student_total = (
            student["C++"]
            + student["python"]
            + student["maths"]
        )
        student_avg = student_total / 3
        total = total + student_total

        if student_avg > highest_avg:
            highest_avg = student_avg
            highest_student = student

        if student_avg < lowest_avg:
            lowest_avg = student_avg
            lowest_student = student
        grade = calculate_grade(student)
        grade_count[grade] = grade_count[grade] + 1
    avg = total / (no * 3)
    print("\n================================")
    print("       CLASS STATISTICS")
    print("================================")
    print("Total students:", no)
    print(f"Class average: {avg:.2f}")
    print("\nHighest average:")
    print(
        f"{highest_student['name']} - {highest_avg:.2f}"
    )
    print("\nLowest average:")
    print(
        f"{lowest_student['name']} - {lowest_avg:.2f}"
    )
    print("\nGrade distribution:")
    print("A:", grade_count["A"])
    print("B:", grade_count["B"])
    print("C:", grade_count["C"])
    print("D:", grade_count["D"])
    print("F:", grade_count["F"])
    return avg, highest_student, lowest_student, grade_count

def save_students(students):
    with open("students.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "id",
                "name",
                "department",
                "year",
                "python",
                "C++",
                "maths"
            ]
        )
        writer.writeheader()
        for student in students:
            writer.writerow(student)

def load_students():
    students = []

    try:
        with open("students.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "department": row["department"],
                    "year": int(row["year"]),
                    "python": int(row["python"]),
                    "C++": int(row["C++"]),
                    "maths": int(row["maths"])
                }
                students.append(student)

    except FileNotFoundError:
        pass

    return students


def main():
    students = load_students()

    while True:
        print("\n==============================")
        print("   STUDENT ACADEMIC SYSTEM")
        print("==============================")
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Calculate average")
        print("7. Calculate grade")
        print("8. Class statistics")
        print("9. Save students")
        print("10. Exit")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a number from 1 to 10.")
            continue

        if choice < 1 or choice > 10:
            print("Please enter a number from 1 to 10.")
            continue

        if choice == 1:
            add_student(students)

        elif choice == 2:
            view_students(students)

        elif choice == 3:
            search_student(students)

        elif choice == 4:
            update_student(students)

        elif choice == 5:
            delete_student(students)

        elif choice == 6:
            if not students:
                print("No students found.")
            else:
                search_id = get_existing_id()
                found = False
                for student in students:
                    if search_id == student["id"]:
                        calculate_average(student)
                        found = True
                        break
                if not found:
                    print("Student not found.")

        elif choice == 7:
            if not students:
                print("No students found.")
            else:
                search_id = get_existing_id()
                found = False
                for student in students:
                    if search_id == student["id"]:
                        grade = calculate_grade(student)
                        print(f"Grade = {grade}")
                        found = True
                        break
                if not found:
                    print("Student not found.")

        elif choice == 8:
            class_statistics(students)

        elif choice == 9:
            save_students(students)
            print("Students saved successfully!")

        elif choice == 10:
            save_students(students)
            print("Students saved successfully!")
            print("Thank you for using the system!")
            break

if __name__ == "__main__":
    main()
