# Student Learning Portal
**Course:** PROG211 Object-Oriented Programming 1  
**Project domain:** Education  
**Language:** Python 3  
**Project type:** Beginner-friendly console application

## 1. Project overview
The Student Learning Portal is a small educational application that manages basic student learning records. It allows a user to add a student, display all student records, search for a student by ID, update learning progress, and view the number of Student objects created.

This project is an educational prototype for demonstrating OOP concepts. It is not a production student information system.

## 2. Problem statement
Keeping simple learning records manually can make it difficult to find a student's record or update their progress consistently. This prototype demonstrates how a small program can organize fictional student records and provide basic record-management operations.

## 3. Objectives
- Create at least two classes relevant to the education domain.
- Give classes attributes and methods.
- Create objects and demonstrate interaction between objects.
- Use exactly one main collection data structure: a Python list.
- Include at least one instance method and one class method.
- Document how the project aligns with Digital Public Goods (DPG) principles.

## 4. Features
1. Add a student record.
2. Display all student records.
3. Find a student using their ID.
4. Update progress to `Not started`, `In progress`, or `Completed`.
5. Display the number of Student objects created.
6. Reject duplicate student IDs.
7. Validate progress values and empty input fields.

## 5. Project files
- `main.py`  -complete Python source code.
- `README.md` -setup, usage, design, testing, and DPG documentation.
- `OOP1_Assignment_Documentation.docx`  -full written assignment report.

## 6. Requirements
- Python 3.9 or newer recommended.
- No third-party Python packages are required.
- Windows, macOS, or Linux terminal/command prompt.

## 7. How to run
1. Download and extract the project files.
2. Open Command Prompt or a terminal in the folder containing `main.py`.
3. Run one of these commands:
   - **Windows:** `py main.py`
   - **macOS/Linux:** `python3 main.py`
4. Follow the menu prompts.

## 8. Menu options
| Option | Action |
|---|---|
| 1 | Add a student |
| 2 | Display all students |
| 3 | Update learning progress |
| 4 | Show total Student objects created |
| 5 | Exit |

## 9. Object-oriented design
### `Student` class
Represents one student record.

**Attributes**
- `student_id`: unique record identifier.
- `name`: student's display name.
- `course`: course or module name.
- `progress`: current learning progress.
- `total_students`: class attribute that counts Student objects created.

**Methods**
- `update_progress(new_progress)`: instance method that validates and changes progress.
- `display_info()`: instance method that displays the record.
- `get_total_students()`: class method, marked with `@classmethod`, that returns the shared object count.

### `LearningPortal` class
Manages Student objects using the `students` list.

**Methods**
- `add_student(student)`: checks for duplicate IDs and adds a record.
- `display_all_students()`: loops through the list and displays each record.
- `find_student(student_id)`: searches the list and returns a matching object or `None`.
- `update_student_progress(student_id, new_progress)`: finds a student and updates progress.

## 10. Data structure
The application uses one collection data structure: a Python **list** (`self.students`). The list stores Student objects. Loops are used to display and search records. No dictionary is used as a second collection for storing student records.

## 11. Example run
The program starts with fictional sample records. Choosing option 2 should show records similar to:

```text
--- Student Learning Records ---
ID: S001 | Name: Aminata Kamara | Course: Introduction to Python | Progress: Not started
ID: S002 | Name: Joseph Conteh | Course: Database Fundamentals | Progress: Not started
```

The sample names and IDs are fictional demonstration data. Do not replace them with real student personal information for a public demo.

## 12. Test plan
| Test | Action | Expected result |
|---|---|---|
| 1 | Display all students | Sample records appear. |
| 2 | Add a new unique ID | System confirms successful addition. |
| 3 | Add an existing ID such as `S001` | System rejects the duplicate. |
| 4 | Update `S001` to `Completed` | Progress is updated. |
| 5 | Enter an invalid progress value | System shows valid progress choices. |
| 6 | Search for a nonexistent ID | System reports that the ID was not found. |
| 7 | Enter an invalid menu option | System asks the user to choose 1-5. |
| 8 | Display total students | Shared Student object count is displayed. |

## 13. Digital Public Goods (DPG) alignment
The assignment brief names these principles:

- **Open source:** MIT License
- **Inclusive and accessible design:** The interface uses a plain-text menu, clear prompts, and text labels rather than relying only on colour or icons.
- **Privacy-respecting:** The sample data is fictional. The program does not request passwords, phone numbers, home addresses, or other sensitive personal data. Records are held in memory and are not transmitted to a server.
- **Modular and reusable:** The `Student` class represents student data and behavior, while `LearningPortal` manages collections of Student objects. This separation supports maintenance and future extension.

These design choices are a basic demonstration of alignment; they do not constitute formal certification as a Digital Public Good.

## 14. Limitations and future improvements
- Records are stored in memory and disappear when the program exits.
- The prototype has no login system or persistent database.
- It is designed for learning and should not be used to store real student records.
- Future improvements could include file/database persistence, automated unit tests, a graphical interface, and a reviewed privacy/security design.

## 15. GitHub submission checklist
1. i Sign in to GitHub and create a repository named `oop1-student-learning-portal`.
2. Upload `main.py`, `README.md`.
3. i Confirm that the repository contains no real or sensitive personal data.
4. And i Add the lecturer as a collaborator for assignment brief.
5. i also Run the program and take screenshots of its execution for the hardcopy submission.
6.And i Print the assignment documentation and attach the required screenshots.
7. And i Verify the repository link and files before submission.

## 16. Academic note
i Review the code, and run it myself, and  explain the classes, attributes, methods, list operations, and DPG principles. 
