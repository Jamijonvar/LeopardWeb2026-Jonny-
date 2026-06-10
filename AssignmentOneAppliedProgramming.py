#"Applied programming Assignment 1"
import sqlite3

database = sqlite3.connect("assignment3(2026).db") 
cursor = database.cursor()

#User Class
#Defines the class User and its attributes
class User:
    def __init__(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    #"Method to set the users firstname"
    def set_firstname(self, in_firstname):
        self.firstname = in_firstname

    #"Method to set the users lastname"
    def set_lastname(self, in_lastname):
        self.lastname = in_lastname

    #"Method to set the users ID"
    def set_id(self, in_id):
        self.id = in_id

    #"Method to print the users firstname, lastname, and ID"
    def printAll(self):
        print(f"{self.firstname} {self.lastname} {self.id}")
        
#"Student Class"
#"Defines the Student class and its attributes which are obtained from its parent class User"
class Student(User):
    def __init__(self, firstname, lastname, id, grad_year, major, email):
        super().__init__(firstname, lastname, id)
        self.grad_year = grad_year
        self.major = major
        self.email = email
        
    def printAll(self):
        return super().printAll()
    
    def searchCourses(self):
        name = input("Enter last name to search: ")
        cursor.execute("SELECT * FROM STUDENT WHERE SURNAME = ?", (name,))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No student found.")
        
    def addCourses(self):
        cursor.execute(
            "INSERT OR IGNORE INTO STUDENT VALUES (?, ?, ?, ?, ?, ?)",
            (self.id, self.firstname, self.lastname, self.grad_year, self.major, self.email)
        )
        database.commit()
        print(f"Student {self.firstname} {self.lastname} added.")

    def dropCourses(self):
        sid = input("Enter student ID to remove: ")
        cursor.execute("DELETE FROM STUDENT WHERE ID = ?", (sid,))
        database.commit()
        print(f"Student {sid} removed.")

    def printSchedule(self):
        cursor.execute("SELECT * FROM STUDENT")
        rows = cursor.fetchall()
        print("\n--- All Students ---")
        for row in rows:
            print(row)

#"Admin Class"
#"Defines the Admin class and its attributes which are obtained from its parent class User"
class Admin(User):
    def __init__(self, firstname, lastname, id, title, office, email):
        super().__init__(firstname, lastname, id)
        self.title = title
        self.office = office
        self.email = email
        
 #   "Method to print the Admins firstname, lastname, and ID"
    def printAll(self):
        return super().printAll()

  #  "Method to add courses"
    def addCourses(self):
        print("Inside add courses method (admin)")

   # "Method to remove courses"
    def removeCourses(self):
        print("Inside remove courses method (admin)")

    #"Method to add users"
    def addUser(self):
        print("Inside add user method (admin)")

    #"Method to remove users"
    def removeUser(self):
        print("Inside remove user method (admin)")

    #"Method to add students"
    def addStudent(self):
        print("Inside add student method (admin)")

    #"Method to remove students"
    def removeStudent(self):
        print("Inside remove student method (admin)")

    #"Method to search the roster"
    def searchRoster(self):
        cursor.execute("SELECT * FROM ADMIN")
        rows = cursor.fetchall()
        print("\n--- Admin Roster ---")
        for row in rows:
            print(row)
            
    #"Method to print the roster"
    def printRoster(self):
        print("Inside print roster method (admin)")

    #"Method to search courses"
    def searchCourses(self):
        print("Inside search courses method (admin)")

    #"Method to print courses"
    def printCourses(self):
        cursor.execute("SELECT * FROM COURSE")
        rows = cursor.fetchall()
        print("\n--- All Courses ---")
        for row in rows:
            print(row)
            
    def updateTitle(self, new_title):
        cursor.execute(
            "UPDATE ADMIN SET TITLE = ? WHERE NAME = ? AND SURNAME = ?",
            (new_title, self.firstname, self.lastname)
        )
        database.commit()
        print(f"{self.firstname} {self.lastname}'s title updated to {new_title}.")
        
#"Instructor Class"
#"Defines the Instructor class and its attributes which are obtained from its parent class User"
class Instructor(User):
    def __init__(self, firstname, lastname, id, title, year_of_hire, department, email):
        super().__init__(firstname, lastname, id)
        self.title = title
        self.year_of_hire = year_of_hire
        self.department = department
        self.email = email

    def printAll(self):
        return super().printAll()

    def printSchedule(self):
        cursor.execute("SELECT * FROM INSTRUCTOR")
        rows = cursor.fetchall()
        print("\n--- All Instructors ---")
        for row in rows:
            print(row)

    def classList(self):
        print("Inside print class list method (Instructor)")

    def courseSearch(self):
        dept = input("Enter department to search: ")
        cursor.execute("SELECT * FROM INSTRUCTOR WHERE DEPT = ?", (dept,))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print(f"No instructors found in {dept}.")

    def removeInstructor(self, iid):
        cursor.execute("DELETE FROM INSTRUCTOR WHERE ID = ?", (iid,))
        database.commit()
        print(f"Instructor {iid} removed.")

class Course:
    def __init__(self, crn, title, department, time, days, semester, year, credits):
        self.crn = crn
        self.title = title
        self.department = department
        self.time = time
        self.days = days
        self.semester = semester
        self.year = year
        self.credits = credits

    def createTable(self):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS COURSE (
                CRN INTEGER PRIMARY KEY,
                title TEXT,
                department TEXT,
                time TEXT,
                days TEXT,
                semester TEXT,
                year INTEGER,
                credits INTEGER
            )
        """)
        database.commit()
        print("Course table created.")

    def insertCourse(self):
        cursor.execute(
            "INSERT OR IGNORE INTO COURSE VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (self.crn, self.title, self.department, self.time, self.days, self.semester, self.year, self.credits)
        )
        database.commit()
        print(f"Course '{self.title}' added.")

    def printAll(self):
        cursor.execute("SELECT * FROM COURSE")
        rows = cursor.fetchall()
        print("\n--- All Courses ---")
        for row in rows:
            print(row)

    def matchInstructors(self):
        cursor.execute("SELECT CRN, title, department FROM COURSE")
        courses = cursor.fetchall()
        print("\n--- Course to Instructor Matching ---")
        for crn, title, dept in courses:
            cursor.execute("SELECT NAME, SURNAME FROM INSTRUCTOR WHERE DEPT = ?", (dept,))
            instructors = cursor.fetchall()
            if instructors:
                names = ", ".join(f"{r[0]} {r[1]}" for r in instructors)
                print(f"{title} (CRN {crn}, {dept}) -> {names}")
            else:
                print(f"{title} (CRN {crn}, {dept}) -> NO MATCHING INSTRUCTOR")
                
                
                
# Create course table
c = Course(None, None, None, None, None, None, None, None)
c.createTable()

# Add 2 students
s1 = Student("Jonny", "Wolf", 10011, 2027, "BSCE", "wolfj")
s2 = Student("Sarah", "Connor", 10012, 2028, "BSEE", "connors")
s1.addCourses()
s2.addCourses()

# Remove 1 instructor (Daniel Bernoulli, ID 20006)
i = Instructor("Daniel", "Bernoulli", 20006, "Associate Prof.", 1760, "BSME", "bernoullid")
i.removeInstructor(20006)

# Update Vera Rubin's title to Vice-President
a = Admin("Vera", "Rubin", 30002, "Registrar", "Wentworth 101", "rubinv")
a.updateTitle("Vice-President")

# Add 5 courses
courses = [
    Course(40001, "Circuit Analysis",    "BSEE", "9:00 AM",  "MWF", "Fall", 2026, 3),
    Course(40002, "Algorithms",          "BSCO", "11:00 AM", "TR",  "Fall", 2026, 3),
    Course(40003, "Applied Mathematics", "BSAS", "1:00 PM",  "MWF", "Fall", 2026, 3),
    Course(40004, "Operating Systems",   "BCOS", "3:00 PM",  "TR",  "Fall", 2026, 3),
    Course(40005, "Humanities Elective", "HUSS", "10:00 AM", "MWF", "Fall", 2026, 3),
]
for course in courses:
    course.insertCourse()

# Print everything to verify
s1.printSchedule()
i.printSchedule()
a.printRoster()
c.printAll()
c.matchInstructors()

database.close()

