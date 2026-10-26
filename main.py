
class Course:
    """Represents a course."""

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def display_info(self):
        return f"{self.code} - {self.name}"


class Student:
    """Represents a student."""

    institution = "Limkokwing University of Creative Technology"

    def __init__(self, student_id, name, programme, course,
                 grade="Not graded"):
        self.student_id = student_id
        self.name = name
        self.programme = programme
        self.course = course
        self.grade = grade

    def display_info(self):
        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Programme: {self.programme}\n"
            f"Course: {self.course.display_info()}\n"
            f"Grade: {self.grade}"
        )

    def update_grade(self, grade):
        grade = grade.strip().upper()

        if grade not in ("A", "B", "C", "D", "E", "F"):
            raise ValueError("Enter a valid grade from A to F.")

        self.grade = grade

    @classmethod
    def from_record(cls, record, course):
        parts = [part.strip() for part in record.split("|")]

        if len(parts) != 4:
            raise ValueError(
                "Format: ID|Name|Programme|Grade"
            )

        student_id, name, programme, grade = parts

        student = cls(
            student_id, name, programme, course
        )

        if grade:
            student.update_grade(grade)

        return student


def add_student(students, course):
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if student_id in students:
        print("This student ID already exists.")
        return

    name = input("Enter full name: ").strip()
    programme = input("Enter programme: ").strip()

    if not name or not programme:
        print("Name and programme are required.")
        return

    students[student_id] = Student(
        student_id, name, programme, course
    )

    print("Student registered successfully.")


def display_students(students):
    if not students:
        print("No student records found.")
        return

    for student in students.values():
        print("-" * 30)
        print(student.display_info())


def search_student(students):
    student_id = input("Enter student ID: ").strip()
    student = students.get(student_id)

    if student:
        print(student.display_info())
    else:
        print("Student record not found.")


def update_grade(students):
    student_id = input("Enter student ID: ").strip()
    student = students.get(student_id)

    if student is None:
        print("Student record not found.")
        return

    grade = input("Enter grade (A-F): ")

    try:
        student.update_grade(grade)
        print("Grade updated successfully.")
    except ValueError as error:
        print(error)


def main():
    # The dictionary is the main collection of Student objects.
    students = {}

    course = Course(
        "PROG211",
        "Object-Oriented Programming 1"
    )

    while True:
        print("\nSTUDENT LEARNING AND RECORDS SYSTEM")
        print("1. Register student")
        print("2. Display all students")
        print("3. Search student")
        print("4. Update grade")
        print("5. Display course")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students, course)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_grade(students)

        elif choice == "5":
            print(course.display_info())
            print("Institution:", Student.institution)

        elif choice == "0":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
