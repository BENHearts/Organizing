class Student:
    def __init__(self, name, grade_level, average):
        if average < 0.0 or average > 100.0:
            raise ValueError("Average must be between 0 and 100.")
        self.name = name
        self.grade_level = grade_level
        self.average = average


    # hours of studying increases average
    def homework(self, hours):
        self.average= min(100.0, self.average + hours *1.5) # caps at 100
        if self.average > 100.0:
            raise ValueError("Average cannot exceed 100.")
        print(f"{self.name} slaved away for {hours} hours. Their new average is {self.average}%.")

    # string function
    def __str__(self):
        return f"Student Name: {self.name}, Grade Level: {self.grade_level}, Average: {self.average}%"
        
class Teacher:
    # creates new teacher
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    # give student grade
    def give_grade(self, student, grade):
        if grade > 100.0 or grade < 0.0:
            raise ValueError("Grade must be between 0 and 100.")
        student.average = grade
        print(f"{self.name} has given {student.name} a grade of {grade}% in {self.subject}.")

    #string function
    def __str__(self):
        return f"Teacher Name: {self.name}, Subject: {self.subject}"

# code to do it
try:
    print("TEACHER INFO")
    teacher_name = input("Enter teacher's name: ")
    teacher_subject = input("Enter teacher's subject: ")
    print("STUDENT INFO")
    student_name = input("Enter student's name: ")    
    student_grade_level = input("Enter student's grade level: ")
    initial_average = float(input("Enter student's initial average: "))
    homework_done = float(input("Enter Homework Hours: "))

    teacher = Teacher(teacher_name, teacher_subject)
    student = Student(student_name, student_grade_level, initial_average)

    print("Before homework:")
    print(teacher)
    print(student)

    student.homework(homework_done)

    final_grade = float(input(f"Enter final grade for {student.name}: "))
    teacher.give_grade(student, final_grade)
    print("Updated student info:")
    print(student)

except ValueError as ve:
    print(f"Error: {ve}")
