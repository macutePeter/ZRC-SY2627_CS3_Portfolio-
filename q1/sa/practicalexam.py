class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = False
        self.__grade = None
        self.__submitted_files = []


    def __validate_grade(self, grade):
            if not isinstance(grade, (int, float)):
                raise ValueError("Grade must be a number.")
            if grade < 0 or grade > 100:
                raise ValueError("Grade must be between 0 and 100.")
            return True


    def __check_submission_student(self):
            if not self.__is_submitted:
                raise ValueError("Assignment has not been submitted yet.")
            return True


    def __is_duplicate_file(self, file_name):
            return file_name in self.__submitted_files


    def add_file(self, file_name):
            if self.__is_duplicate_file(file_name):
                print(f"-----> [ERROR] File '{file_name}' has already been submitted.")
            else:
                self.__submitted_files.append(file_name)
                self.__is_submitted = True
                print(f"-----> [SUCCESS] {self.student_name} attached file {file_name}. Total files: {len(self.__submitted_files)}")


    def new_method(self, file_name):
            raise ValueError(f"File '{file_name}' has already been submitted.")


    def remove_file(self, file_name):
            if file_name not in self.__submitted_files:
                raise ValueError(f"File '{file_name}' is not in the submitted files.")
            self.__submitted_files.remove(file_name)
            if not self.__submitted_files:
                self.__is_submitted = False


    def assign_grade(self, grade):
            self.__validate_grade(grade)
            self.__grade = grade


    def get_grade(self):
            self.__check_submission_student()
            return self.__grade


    def view_files(self):
            self.__check_submission_student()
            return self.__submitted_files


    def get_status_report(self):
            status = "Submitted" if self.__is_submitted else "Not Submitted"
            grade = self.__grade if self.__is_submitted else "N/A"

            return f"ID: {self.student_id} | Name: {self.student_name} | Status: {status} | Grade: {grade}"


print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01")
student3 = AssignmentSubmission("John Doe", "pshs-1080-x", "CS-104", "2026-10-01")
student4 = AssignmentSubmission("Jane Doe", "pshs-1070-x", "CS-107", "2026-10-01")
student5 = AssignmentSubmission("Ellen Joe", "pshs-1060-x", "CS-109", "2026-10-01")
student6 = AssignmentSubmission("Velina", "pshs-1040-x", "CS-102", "2026-10-01")
student7 = AssignmentSubmission("Billy Goat", "pshs-1030-x", "CS-106", "2026-10-01")


print("--- TEST SCENARIO 1: Multiple File via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")


print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")


print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py")
print(f"John Doe's Files: {student3.view_files()}\n")


print("-- TEST SCENARIO 4: Removing File after being graded ---")
student4.add_file("exams_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exams_answers.pdf")
print()


print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100)
print()


print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())

#Hi mom
