import pandas as pd

class Student:
    def __init__(self, name, age, grade, student_id):
        self.name = name
        self.age = age
        self.grade = grade
        self.student_id = student_id

    def display_info(self):
        print("\nStudent Details:")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Grade      : {self.grade}")
        print(f"Student ID : {self.student_id}")


students = []

print("===== Welcome to Student Management System =====")

while True:
    print("\nMenu")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Show All Students")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:

        # 1. Add Student
        case '1':
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            grade = input("Enter Grade: ")
            student_id = input("Enter Student ID: ")
            if student_id in [student.student_id for student in students]:
                print("Student ID already exists! Please try again.")
                continue
            student = Student(name, age, grade, student_id)
            students.append(student)

            print("Student Added Successfully!")

        # 2. Search Student
        case '2':
            student_id = input("Enter Student ID to Search: ")

            found = False

            for student in students:
                if student.student_id == student_id:
                    print("\nStudent Found!")
                    student.display_info()
                    found = True
                    break

            if not found:
                print("Student Not Found!")

        # 3. Update Student
        case '3':
            student_id = input("Enter Student ID to Update: ")

            found = False

            for student in students:
                if student.student_id == student_id:

                    print("\nEnter New Details")

                    student.name = input("Enter New Name: ")
                    student.age = input("Enter New Age: ")
                    student.grade = input("Enter New Grade: ")

                    print("Student Updated Successfully!")
                    found = True
                    break

            if not found:
                print("Student Not Found!")

        # 4. Show All Students using Pandas
        case '4':
            if not students:
                print("No Students Found!")

            else:
                data = []

                for student in students:
                    data.append({
                        "Name": student.name,
                        "Age": student.age,
                        "Grade": student.grade,
                        "Student ID": student.student_id
                    })

                df = pd.DataFrame(data)

                print("\n===== All Students =====")
                print(df.to_string(index=False))

        # 5. Delete Student
        case '5':
            student_id = input("Enter Student ID to Delete: ")

            found = False

            for student in students:
                if student.student_id == student_id:
                    students.remove(student)

                    print("Student Deleted Successfully!")
                    found = True
                    break

            if not found:
                print("Student Not Found!")

        # 6. Exit
        case '6':
            data = []

            for student in students:
                    data.append({
                        "Name": student.name,
                        "Age": student.age,
                        "Grade": student.grade,
                        "Student ID": student.student_id
                    })

            Data_in_pd = pd.DataFrame(data)
            Data_in_pd.to_csv("data.csv", index=False)

            print("Exiting Student Management System...")
            print("Goodbye!")
            break

        # Invalid Input
        case _:
            print("Invalid Choice! Please Try Again.")
        