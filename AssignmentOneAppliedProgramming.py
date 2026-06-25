# Applied Programming Assignment 5
# Built on top of Assignment 1/3 code
import sqlite3

database = sqlite3.connect("assignment3(2026).db")
cursor = database.cursor()

# ─────────────────────────────────────────────
# TABLE SETUP
# ─────────────────────────────────────────────

def setup_tables():
    # Course table (from Assignment 3)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS COURSE (
            CRN INTEGER PRIMARY KEY,
            title TEXT,
            department TEXT,
            time TEXT,
            days TEXT,
            semester TEXT,
            year INTEGER,
            credits INTEGER,
            instructor_id INTEGER
        )
    """)
    # Add instructor_id column if it doesn't exist yet (migration for existing DB)
    try:
        cursor.execute("ALTER TABLE COURSE ADD COLUMN instructor_id INTEGER")
    except:
        pass  # Column already exists, that's fine

    # Enrollment table - tracks which student is in which course
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ENROLLMENT (
            student_id INTEGER,
            crn INTEGER,
            PRIMARY KEY (student_id, crn)
        )
    """)

    # Login table - stores credentials and role for every user
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS LOGIN (
            id INTEGER PRIMARY KEY,
            password TEXT,
            role TEXT
        )
    """)

    database.commit()

# ─────────────────────────────────────────────
# SEED DATA
# ─────────────────────────────────────────────

def seed_data():

    # --- STUDENTS (20 total) ---
    students = [
        (10001, "James",    "Martinez",  2026, "BSEE", "martinezj"),
        (10002, "Priya",    "Patel",     2027, "BSCO", "patelp"),
        (10003, "Marcus",   "Johnson",   2026, "BSME", "johnsonm"),
        (10004, "Sofia",    "Nguyen",    2028, "BSCE", "nguyens"),
        (10005, "Ethan",    "Brown",     2027, "BSEE", "browne"),
        (10006, "Aisha",    "Williams",  2026, "BSCO", "williamsa"),
        (10007, "Lucas",    "Garcia",    2028, "BSME", "garcial"),
        (10008, "Mei",      "Chen",      2027, "BSCE", "chenm"),
        (10009, "Tyler",    "Davis",     2026, "BSEE", "davist"),
        (10010, "Fatima",   "Ali",       2028, "BSCO", "alif"),
        (10011, "Jonny",    "Wolf",      2027, "BSCE", "wolfj"),
        (10012, "Sarah",    "Connor",    2028, "BSEE", "connors"),
        (10013, "Olivia",   "Kim",       2026, "BSME", "kimo"),
        (10014, "Noah",     "Thompson",  2027, "BSCO", "thompsonn"),
        (10015, "Amara",    "Okafor",    2028, "BSCE", "okafora"),
        (10016, "Ryan",     "Lee",       2026, "BSEE", "leer"),
        (10017, "Isabella", "Torres",    2027, "BSME", "torresi"),
        (10018, "Kai",      "Nakamura",  2028, "BSCO", "nakamurak"),
        (10019, "Destiny",  "Jackson",   2026, "BSCE", "jacksond"),
        (10020, "Omar",     "Hassan",    2027, "BSEE", "hassano"),
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO STUDENT VALUES (?, ?, ?, ?, ?, ?)",
        students
    )

    # --- INSTRUCTORS (15 total) ---
    instructors = [
        (20001, "Alan",     "Turing",     "Professor",       1990, "BSCO", "turinga"),
        (20002, "Grace",    "Hopper",     "Professor",       1985, "BSCO", "hopperg"),
        (20003, "Nikola",   "Tesla",      "Professor",       1995, "BSEE", "teslan"),
        (20004, "Marie",    "Curie",      "Associate Prof.", 2000, "BSAS", "curiem"),
        (20005, "Ada",      "Lovelace",   "Professor",       1988, "BSCO", "lovelacea"),
        (20007, "James",    "Maxwell",    "Professor",       1992, "BSEE", "maxwellj"),
        (20008, "Lise",     "Meitner",    "Associate Prof.", 2005, "BSME", "meitnerl"),
        (20009, "Richard",  "Feynman",    "Professor",       1998, "BSAS", "feynmanr"),
        (20010, "Katherine","Johnson",    "Associate Prof.", 2003, "BSME", "johnsonk"),
        (20011, "Claude",   "Shannon",    "Professor",       1991, "BSEE", "shannonc"),
        (20012, "Hedy",     "Lamarr",     "Lecturer",        2010, "BSCO", "lamarrh"),
        (20013, "John",     "Von Neumann","Professor",       1987, "BSCO", "vonneumannj"),
        (20014, "Barbara",  "Liskov",     "Associate Prof.", 2007, "BSCO", "liskovb"),
        (20015, "Vera",     "Franklin",   "Lecturer",        2015, "BSEE", "franklinv"),
        (20016, "Tim",      "Berners-Lee","Professor",       1993, "BSCO", "bernerslee"),
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO INSTRUCTOR VALUES (?, ?, ?, ?, ?, ?, ?)",
        instructors
    )

    # --- ADMINS ---
    admins = [
        (30001, "The",  "Registrar", "Registrar",      "Admin Wing 100", "registrar"),
        (30002, "Vera", "Rubin",     "Vice-President", "Wentworth 101",  "rubinv"),
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO ADMIN VALUES (?, ?, ?, ?, ?, ?)",
        admins
    )

    # --- COURSES (20 total, with assigned instructor) ---
    courses = [
        (40001, "Circuit Analysis",         "BSEE", "9:00 AM",  "MWF", "Fall", 2026, 3, 20003),
        (40002, "Algorithms",               "BSCO", "11:00 AM", "TR",  "Fall", 2026, 3, 20001),
        (40003, "Applied Mathematics",      "BSAS", "1:00 PM",  "MWF", "Fall", 2026, 3, 20004),
        (40004, "Operating Systems",        "BSCO", "3:00 PM",  "TR",  "Fall", 2026, 3, 20002),
        (40005, "Humanities Elective",      "HUSS", "10:00 AM", "MWF", "Fall", 2026, 3, None),
        (40006, "Digital Systems",          "BSEE", "8:00 AM",  "MWF", "Fall", 2026, 3, 20007),
        (40007, "Data Structures",          "BSCO", "2:00 PM",  "TR",  "Fall", 2026, 3, 20005),
        (40008, "Thermodynamics",           "BSME", "10:00 AM", "TR",  "Fall", 2026, 3, 20008),
        (40009, "Linear Algebra",           "BSAS", "9:00 AM",  "TR",  "Fall", 2026, 3, 20009),
        (40010, "Signals and Systems",      "BSEE", "1:00 PM",  "TR",  "Fall", 2026, 3, 20011),
        (40011, "Computer Networks",        "BSCO", "11:00 AM", "MWF", "Fall", 2026, 3, 20013),
        (40012, "Fluid Mechanics",          "BSME", "3:00 PM",  "MWF", "Fall", 2026, 3, 20010),
        (40013, "Calculus III",             "BSAS", "8:00 AM",  "MWF", "Fall", 2026, 3, 20004),
        (40014, "Embedded Systems",         "BSEE", "2:00 PM",  "MWF", "Fall", 2026, 3, 20015),
        (40015, "Database Systems",         "BSCO", "4:00 PM",  "TR",  "Fall", 2026, 3, 20014),
        (40016, "Machine Design",           "BSME", "9:00 AM",  "MWF", "Fall", 2026, 3, 20008),
        (40017, "Software Engineering",     "BSCO", "12:00 PM", "MWF", "Fall", 2026, 3, 20016),
        (40018, "Power Systems",            "BSEE", "10:00 AM", "TR",  "Fall", 2026, 3, 20007),
        (40019, "Technical Writing",        "HUSS", "1:00 PM",  "TR",  "Fall", 2026, 3, None),
        (40020, "Statics",                  "BSME", "11:00 AM", "MWF", "Fall", 2026, 3, 20010),
    ]
    # Insert courses — need to handle the extra instructor_id column
    for course in courses:
        cursor.execute(
            "INSERT OR IGNORE INTO COURSE (CRN, title, department, time, days, semester, year, credits, instructor_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            course
        )

    # --- ENROLLMENTS (seed some students into courses for roster testing) ---
    enrollments = [
        (10001, 40001), (10001, 40006), (10001, 40010),
        (10002, 40002), (10002, 40007), (10002, 40011),
        (10003, 40008), (10003, 40012), (10003, 40020),
        (10004, 40001), (10004, 40009), (10004, 40013),
        (10005, 40006), (10005, 40010), (10005, 40018),
        (10006, 40002), (10006, 40015), (10006, 40017),
        (10007, 40008), (10007, 40016), (10007, 40020),
        (10008, 40003), (10008, 40009), (10008, 40013),
        (10009, 40001), (10009, 40014), (10009, 40018),
        (10010, 40004), (10010, 40011), (10010, 40017),
        (10011, 40001), (10011, 40010), (10011, 40006),
        (10012, 40006), (10012, 40018), (10012, 40014),
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO ENROLLMENT VALUES (?, ?)",
        enrollments
    )

    # --- LOGIN TABLE (id, password, role) ---
    logins = [
        # Students
        (10001, "pass1001", "student"),
        (10002, "pass1002", "student"),
        (10003, "pass1003", "student"),
        (10004, "pass1004", "student"),
        (10005, "pass1005", "student"),
        (10006, "pass1006", "student"),
        (10007, "pass1007", "student"),
        (10008, "pass1008", "student"),
        (10009, "pass1009", "student"),
        (10010, "pass1010", "student"),
        (10011, "pass1011", "student"),
        (10012, "pass1012", "student"),
        (10013, "pass1013", "student"),
        (10014, "pass1014", "student"),
        (10015, "pass1015", "student"),
        (10016, "pass1016", "student"),
        (10017, "pass1017", "student"),
        (10018, "pass1018", "student"),
        (10019, "pass1019", "student"),
        (10020, "pass1020", "student"),
        # Instructors
        (20001, "pass2001", "instructor"),
        (20002, "pass2002", "instructor"),
        (20003, "pass2003", "instructor"),
        (20004, "pass2004", "instructor"),
        (20005, "pass2005", "instructor"),
        (20007, "pass2007", "instructor"),
        (20008, "pass2008", "instructor"),
        (20009, "pass2009", "instructor"),
        (20010, "pass2010", "instructor"),
        (20011, "pass2011", "instructor"),
        (20012, "pass2012", "instructor"),
        (20013, "pass2013", "instructor"),
        (20014, "pass2014", "instructor"),
        (20015, "pass2015", "instructor"),
        (20016, "pass2016", "instructor"),
        # Admins
        (30001, "admin123",  "admin"),
        (30002, "admin456",  "admin"),
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO LOGIN VALUES (?, ?, ?)",
        logins
    )

    database.commit()

# ─────────────────────────────────────────────
# USER CLASS
# ─────────────────────────────────────────────

# Defines the class User and its attributes
class User:
    def __init__(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    # Method to set the users firstname
    def set_firstname(self, in_firstname):
        self.firstname = in_firstname

    # Method to set the users lastname
    def set_lastname(self, in_lastname):
        self.lastname = in_lastname

    # Method to set the users ID
    def set_id(self, in_id):
        self.id = in_id

    # Method to print the users firstname, lastname, and ID
    def printAll(self):
        print(f"{self.firstname} {self.lastname} {self.id}")

# ─────────────────────────────────────────────
# STUDENT CLASS
# ─────────────────────────────────────────────

# Defines the Student class and its attributes which are obtained from its parent class User
class Student(User):
    def __init__(self, firstname, lastname, id, grad_year, major, email):
        super().__init__(firstname, lastname, id)
        self.grad_year = grad_year
        self.major = major
        self.email = email

    def printAll(self):
        return super().printAll()

    # Search all courses (default: by department/major)
    def searchCourses(self):
        print(f"\nShowing courses for your major ({self.major}):")
        cursor.execute("SELECT CRN, title, time, days, credits FROM COURSE WHERE department = ?", (self.major,))
        rows = cursor.fetchall()
        if rows:
            print(f"{'CRN':<8} {'Title':<30} {'Time':<12} {'Days':<6} {'Credits'}")
            print("-" * 65)
            for row in rows:
                print(f"{row[0]:<8} {row[1]:<30} {row[2]:<12} {row[3]:<6} {row[4]}")
        else:
            print("No courses found for your major.")

    # Search courses by user-specified parameter
    def searchCoursesByParam(self):
        print("\nSearch courses by:")
        print("1. Department")
        print("2. Day(s) of week")
        print("3. CRN")
        choice = input("Select: ").strip()
        if choice == "1":
            dept = input("Enter department: ").strip()
            cursor.execute("SELECT CRN, title, time, days, credits FROM COURSE WHERE department = ?", (dept,))
        elif choice == "2":
            days = input("Enter day(s) (e.g. MWF or TR): ").strip()
            cursor.execute("SELECT CRN, title, time, days, credits FROM COURSE WHERE days = ?", (days,))
        elif choice == "3":
            crn = input("Enter CRN: ").strip()
            cursor.execute("SELECT CRN, title, time, days, credits FROM COURSE WHERE CRN = ?", (crn,))
        else:
            print("Invalid choice.")
            return
        rows = cursor.fetchall()
        if rows:
            print(f"\n{'CRN':<8} {'Title':<30} {'Time':<12} {'Days':<6} {'Credits'}")
            print("-" * 65)
            for row in rows:
                print(f"{row[0]:<8} {row[1]:<30} {row[2]:<12} {row[3]:<6} {row[4]}")
        else:
            print("No courses found.")

    # Add a course to this student's schedule
    def addCourseToSchedule(self):
        crn = input("Enter CRN of course to add: ").strip()
        cursor.execute("SELECT * FROM COURSE WHERE CRN = ?", (crn,))
        course = cursor.fetchone()
        if not course:
            print("Course not found.")
            return
        # Check for time conflict before enrolling
        cursor.execute("""
            SELECT C.title, C.time, C.days FROM COURSE C
            JOIN ENROLLMENT E ON C.CRN = E.crn
            WHERE E.student_id = ? AND C.time = ? AND C.days = ?
        """, (self.id, course[3], course[4]))
        conflict = cursor.fetchone()
        if conflict:
            print(f"Schedule conflict with '{conflict[0]}' at {conflict[1]} on {conflict[2]}.")
            return
        cursor.execute("INSERT OR IGNORE INTO ENROLLMENT VALUES (?, ?)", (self.id, crn))
        database.commit()
        print(f"Successfully enrolled in '{course[1]}'.")

    # Remove a course from this student's schedule
    def dropCourses(self):
        crn = input("Enter CRN of course to drop: ").strip()
        cursor.execute("SELECT title FROM COURSE WHERE CRN = ?", (crn,))
        course = cursor.fetchone()
        if not course:
            print("Course not found.")
            return
        cursor.execute("DELETE FROM ENROLLMENT WHERE student_id = ? AND crn = ?", (self.id, crn))
        database.commit()
        print(f"Dropped '{course[0]}'.")

    # Check for conflicts in current schedule
    def checkConflicts(self):
        cursor.execute("""
            SELECT C.CRN, C.title, C.time, C.days FROM COURSE C
            JOIN ENROLLMENT E ON C.CRN = E.crn
            WHERE E.student_id = ?
        """, (self.id,))
        enrolled = cursor.fetchall()
        print("\n--- Conflict Check ---")
        conflicts_found = False
        seen = {}
        for row in enrolled:
            key = (row[2], row[3])  # (time, days)
            if key in seen:
                print(f"CONFLICT: '{row[1]}' and '{seen[key]}' both meet {row[3]} at {row[2]}")
                conflicts_found = True
            else:
                seen[key] = row[1]
        if not conflicts_found:
            print("No conflicts found in your schedule.")

    # Print this student's enrolled schedule
    def printSchedule(self):
        cursor.execute("""
            SELECT C.CRN, C.title, C.department, C.time, C.days, C.credits FROM COURSE C
            JOIN ENROLLMENT E ON C.CRN = E.crn
            WHERE E.student_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        print(f"\n--- Schedule for {self.firstname} {self.lastname} ---")
        if rows:
            print(f"{'CRN':<8} {'Title':<30} {'Dept':<8} {'Time':<12} {'Days':<6} {'Cr'}")
            print("-" * 72)
            for row in rows:
                print(f"{row[0]:<8} {row[1]:<30} {row[2]:<8} {row[3]:<12} {row[4]:<6} {row[5]}")
        else:
            print("You are not enrolled in any courses.")

    # Insert this student into the STUDENT table (from Assignment 3)
    def addCourses(self):
        cursor.execute(
            "INSERT OR IGNORE INTO STUDENT VALUES (?, ?, ?, ?, ?, ?)",
            (self.id, self.firstname, self.lastname, self.grad_year, self.major, self.email)
        )
        database.commit()
        print(f"Student {self.firstname} {self.lastname} added.")

# ─────────────────────────────────────────────
# ADMIN CLASS
# ─────────────────────────────────────────────

# Defines the Admin class and its attributes which are obtained from its parent class User
class Admin(User):
    def __init__(self, firstname, lastname, id, title, office, email):
        super().__init__(firstname, lastname, id)
        self.title = title
        self.office = office
        self.email = email

    # Method to print the Admins firstname, lastname, and ID
    def printAll(self):
        return super().printAll()

    # Search courses by default parameter (department)
    def searchCourses(self):
        dept = input("Enter department to search: ").strip()
        cursor.execute("SELECT CRN, title, time, days, credits FROM COURSE WHERE department = ?", (dept,))
        rows = cursor.fetchall()
        print(f"\n--- Courses in {dept} ---")
        if rows:
            print(f"{'CRN':<8} {'Title':<30} {'Time':<12} {'Days':<6} {'Credits'}")
            print("-" * 65)
            for row in rows:
                print(f"{row[0]:<8} {row[1]:<30} {row[2]:<12} {row[3]:<6} {row[4]}")
        else:
            print("No courses found.")

    # Search courses by user-specified parameter
    def searchCoursesByParam(self):
        print("\nSearch by: 1. CRN  2. Title  3. Semester")
        choice = input("Select: ").strip()
        if choice == "1":
            crn = input("Enter CRN: ").strip()
            cursor.execute("SELECT * FROM COURSE WHERE CRN = ?", (crn,))
        elif choice == "2":
            title = input("Enter title keyword: ").strip()
            cursor.execute("SELECT * FROM COURSE WHERE title LIKE ?", (f"%{title}%",))
        elif choice == "3":
            sem = input("Enter semester (e.g. Fall): ").strip()
            cursor.execute("SELECT * FROM COURSE WHERE semester = ?", (sem,))
        else:
            print("Invalid choice.")
            return
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No courses found.")

    # Add a course to the system
    def addCourseToSystem(self):
        crn   = input("CRN: ").strip()
        title = input("Title: ").strip()
        dept  = input("Department: ").strip()
        time  = input("Time (e.g. 9:00 AM): ").strip()
        days  = input("Days (e.g. MWF): ").strip()
        sem   = input("Semester: ").strip()
        year  = input("Year: ").strip()
        cred  = input("Credits: ").strip()
        c = Course(int(crn), title, dept, time, days, sem, int(year), int(cred))
        c.insertCourse()

    # Add a student to the system
    def addStudent(self):
        fn  = input("First name: ").strip()
        ln  = input("Last name: ").strip()
        sid = input("Student ID: ").strip()
        gy  = input("Grad year: ").strip()
        maj = input("Major: ").strip()
        em  = input("Email: ").strip()
        s = Student(fn, ln, int(sid), int(gy), maj, em)
        s.addCourses()
        cursor.execute("INSERT OR IGNORE INTO LOGIN VALUES (?, ?, ?)", (int(sid), f"pass{sid}", "student"))
        database.commit()
        print(f"Login created for {fn} {ln}.")

    # Add an instructor to the system
    def addInstructor(self):
        fn   = input("First name: ").strip()
        ln   = input("Last name: ").strip()
        iid  = input("Instructor ID: ").strip()
        title = input("Title: ").strip()
        yoh  = input("Year of hire: ").strip()
        dept = input("Department: ").strip()
        em   = input("Email: ").strip()
        i = Instructor(fn, ln, int(iid), title, int(yoh), dept, em)
        i.addInstructor()
        cursor.execute("INSERT OR IGNORE INTO LOGIN VALUES (?, ?, ?)", (int(iid), f"pass{iid}", "instructor"))
        database.commit()
        print(f"Login created for {fn} {ln}.")

    # Link an instructor to a course
    def linkInstructor(self):
        crn = input("Enter CRN: ").strip()
        iid = input("Enter Instructor ID to assign (leave blank to unlink): ").strip()
        if iid == "":
            cursor.execute("UPDATE COURSE SET instructor_id = NULL WHERE CRN = ?", (crn,))
            print(f"Instructor unlinked from CRN {crn}.")
        else:
            cursor.execute("UPDATE COURSE SET instructor_id = ? WHERE CRN = ?", (iid, crn))
            print(f"Instructor {iid} linked to CRN {crn}.")
        database.commit()

    # Add a student to a specific course
    def addStudentToCourse(self):
        sid = input("Enter student ID: ").strip()
        crn = input("Enter CRN: ").strip()
        cursor.execute("INSERT OR IGNORE INTO ENROLLMENT VALUES (?, ?)", (sid, crn))
        database.commit()
        print(f"Student {sid} added to CRN {crn}.")

    # Remove a student from a specific course
    def removeStudentFromCourse(self):
        sid = input("Enter student ID: ").strip()
        crn = input("Enter CRN: ").strip()
        cursor.execute("DELETE FROM ENROLLMENT WHERE student_id = ? AND crn = ?", (sid, crn))
        database.commit()
        print(f"Student {sid} removed from CRN {crn}.")

    # Method to search the roster
    def searchRoster(self):
        cursor.execute("SELECT * FROM ADMIN")
        rows = cursor.fetchall()
        print("\n--- Admin Roster ---")
        for row in rows:
            print(row)

    # Method to print the roster
    def printRoster(self):
        self.searchRoster()

    # Method to print courses
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

    # Method to add courses (stub kept from Assignment 1)
    def addCourses(self):
        print("Inside add courses method (admin)")

    # Method to remove courses (stub kept from Assignment 1)
    def removeCourses(self):
        print("Inside remove courses method (admin)")

    # Method to add users (stub kept from Assignment 1)
    def addUser(self):
        print("Inside add user method (admin)")

    # Method to remove users (stub kept from Assignment 1)
    def removeUser(self):
        print("Inside remove user method (admin)")

    # Method to remove students (stub kept from Assignment 1)
    def removeStudent(self):
        print("Inside remove student method (admin)")

# ─────────────────────────────────────────────
# INSTRUCTOR CLASS
# ─────────────────────────────────────────────

# Defines the Instructor class and its attributes which are obtained from its parent class User
class Instructor(User):
    def __init__(self, firstname, lastname, id, title, year_of_hire, department, email):
        super().__init__(firstname, lastname, id)
        self.title = title
        self.year_of_hire = year_of_hire
        self.department = department
        self.email = email

    def printAll(self):
        return super().printAll()

    # Insert this instructor into the INSTRUCTOR table
    def addInstructor(self):
        cursor.execute(
            "INSERT OR IGNORE INTO INSTRUCTOR VALUES (?, ?, ?, ?, ?, ?, ?)",
            (self.id, self.firstname, self.lastname, self.title, self.year_of_hire, self.department, self.email)
        )
        database.commit()
        print(f"Instructor {self.firstname} {self.lastname} added.")

    # Search courses by default (this instructor's department)
    def searchCourses(self):
        print(f"\nCourses in your department ({self.department}):")
        cursor.execute("SELECT CRN, title, time, days, credits FROM COURSE WHERE department = ?", (self.department,))
        rows = cursor.fetchall()
        if rows:
            print(f"{'CRN':<8} {'Title':<30} {'Time':<12} {'Days':<6} {'Credits'}")
            print("-" * 65)
            for row in rows:
                print(f"{row[0]:<8} {row[1]:<30} {row[2]:<12} {row[3]:<6} {row[4]}")
        else:
            print("No courses found.")

    # Search courses by user-specified parameter
    def searchCoursesByParam(self):
        print("\nSearch by: 1. Department  2. Days  3. CRN")
        choice = input("Select: ").strip()
        if choice == "1":
            dept = input("Enter department: ").strip()
            cursor.execute("SELECT CRN, title, time, days, credits FROM COURSE WHERE department = ?", (dept,))
        elif choice == "2":
            days = input("Enter days (e.g. MWF): ").strip()
            cursor.execute("SELECT CRN, title, time, days, credits FROM COURSE WHERE days = ?", (days,))
        elif choice == "3":
            crn = input("Enter CRN: ").strip()
            cursor.execute("SELECT CRN, title, time, days, credits FROM COURSE WHERE CRN = ?", (crn,))
        else:
            print("Invalid choice.")
            return
        rows = cursor.fetchall()
        if rows:
            print(f"\n{'CRN':<8} {'Title':<30} {'Time':<12} {'Days':<6} {'Credits'}")
            print("-" * 65)
            for row in rows:
                print(f"{row[0]:<8} {row[1]:<30} {row[2]:<12} {row[3]:<6} {row[4]}")
        else:
            print("No courses found.")

    # Print this instructor's teaching schedule (courses assigned to them)
    def printSchedule(self):
        cursor.execute("""
            SELECT CRN, title, time, days, credits FROM COURSE
            WHERE instructor_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        print(f"\n--- Teaching Schedule for {self.firstname} {self.lastname} ---")
        if rows:
            print(f"{'CRN':<8} {'Title':<30} {'Time':<12} {'Days':<6} {'Credits'}")
            print("-" * 65)
            for row in rows:
                print(f"{row[0]:<8} {row[1]:<30} {row[2]:<12} {row[3]:<6} {row[4]}")
        else:
            print("You are not assigned to any courses.")

    # Search a course's roster for a specific student
    def classList(self):
        crn = input("Enter CRN to search roster: ").strip()
        name = input("Enter student last name to search: ").strip()
        cursor.execute("""
            SELECT S.ID, S.NAME, S.SURNAME FROM STUDENT S
            JOIN ENROLLMENT E ON S.ID = E.student_id
            WHERE E.crn = ? AND S.SURNAME = ?
        """, (crn, name))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(f"ID: {row[0]}  Name: {row[1]} {row[2]}")
        else:
            print("Student not found in that course.")

    # Print full roster for a course this instructor teaches
    def courseSearch(self):
        crn = input("Enter CRN to print roster: ").strip()
        cursor.execute("""
            SELECT S.ID, S.NAME, S.SURNAME, S.MAJOR FROM STUDENT S
            JOIN ENROLLMENT E ON S.ID = E.student_id
            WHERE E.crn = ?
        """, (crn,))
        rows = cursor.fetchall()
        cursor.execute("SELECT title FROM COURSE WHERE CRN = ?", (crn,))
        course = cursor.fetchone()
        title = course[0] if course else f"CRN {crn}"
        print(f"\n--- Roster for {title} ---")
        if rows:
            print(f"{'ID':<8} {'First':<15} {'Last':<15} {'Major'}")
            print("-" * 50)
            for row in rows:
                print(f"{row[0]:<8} {row[1]:<15} {row[2]:<15} {row[3]}")
        else:
            print("No students enrolled.")

    def removeInstructor(self, iid):
        cursor.execute("DELETE FROM INSTRUCTOR WHERE ID = ?", (iid,))
        database.commit()
        print(f"Instructor {iid} removed.")

# ─────────────────────────────────────────────
# COURSE CLASS
# ─────────────────────────────────────────────

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
                credits INTEGER,
                instructor_id INTEGER
            )
        """)
        database.commit()
        print("Course table created.")

    def insertCourse(self):
        cursor.execute(
            "INSERT OR IGNORE INTO COURSE (CRN, title, department, time, days, semester, year, credits) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
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

# ─────────────────────────────────────────────
# LOGIN SYSTEM
# ─────────────────────────────────────────────

def login():
    print("\n=============================")
    print("   Welcome to LeopardWeb")
    print("=============================")
    uid      = input("Enter your ID: ").strip()
    password = input("Enter your password: ").strip()
    cursor.execute("SELECT role FROM LOGIN WHERE id = ? AND password = ?", (uid, password))
    result = cursor.fetchone()
    if not result:
        print("Invalid credentials. Please try again.")
        return None, None
    role = result[0]
    print(f"\nLogin successful! Role: {role.capitalize()}")
    return int(uid), role

# ─────────────────────────────────────────────
# MENUS
# ─────────────────────────────────────────────

def student_menu(uid):
    # Load student object from DB
    cursor.execute("SELECT * FROM STUDENT WHERE ID = ?", (uid,))
    row = cursor.fetchone()
    if not row:
        print("Student record not found.")
        return
    s = Student(row[1], row[2], row[0], row[3], row[4], row[5])

    while True:
        print(f"\n--- Student Menu ({s.firstname} {s.lastname}) ---")
        print("1. Search courses (by my major)")
        print("2. Search courses (by custom parameter)")
        print("3. Add a course to my schedule")
        print("4. Drop a course from my schedule")
        print("5. Check for schedule conflicts")
        print("6. Print my schedule")
        print("7. Logout")
        choice = input("Select: ").strip()

        if choice == "1":
            s.searchCourses()
        elif choice == "2":
            s.searchCoursesByParam()
        elif choice == "3":
            s.addCourseToSchedule()
        elif choice == "4":
            s.dropCourses()
        elif choice == "5":
            s.checkConflicts()
        elif choice == "6":
            s.printSchedule()
        elif choice == "7":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")

def instructor_menu(uid):
    # Load instructor object from DB
    cursor.execute("SELECT * FROM INSTRUCTOR WHERE ID = ?", (uid,))
    row = cursor.fetchone()
    if not row:
        print("Instructor record not found.")
        return
    i = Instructor(row[1], row[2], row[0], row[3], row[4], row[5], row[6])

    while True:
        print(f"\n--- Instructor Menu ({i.firstname} {i.lastname}) ---")
        print("1. Search courses (by my department)")
        print("2. Search courses (by custom parameter)")
        print("3. Print my teaching schedule")
        print("4. Search course roster for a student")
        print("5. Print full course roster")
        print("6. Logout")
        choice = input("Select: ").strip()

        if choice == "1":
            i.searchCourses()
        elif choice == "2":
            i.searchCoursesByParam()
        elif choice == "3":
            i.printSchedule()
        elif choice == "4":
            i.classList()
        elif choice == "5":
            i.courseSearch()
        elif choice == "6":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")

def admin_menu(uid):
    # Load admin object from DB
    cursor.execute("SELECT * FROM ADMIN WHERE ID = ?", (uid,))
    row = cursor.fetchone()
    if not row:
        print("Admin record not found.")
        return
    a = Admin(row[1], row[2], row[0], row[3], row[4], row[5])

    while True:
        print(f"\n--- Admin Menu ({a.firstname} {a.lastname}) ---")
        print("1.  Search courses (by department)")
        print("2.  Search courses (by custom parameter)")
        print("3.  Add a course to the system")
        print("4.  Add a student to the system")
        print("5.  Add an instructor to the system")
        print("6.  Link/unlink instructor to a course")
        print("7.  Add a student to a course")
        print("8.  Remove a student from a course")
        print("9.  Print all courses")
        print("10. Print admin roster")
        print("11. Logout")
        choice = input("Select: ").strip()

        if choice == "1":
            a.searchCourses()
        elif choice == "2":
            a.searchCoursesByParam()
        elif choice == "3":
            a.addCourseToSystem()
        elif choice == "4":
            a.addStudent()
        elif choice == "5":
            a.addInstructor()
        elif choice == "6":
            a.linkInstructor()
        elif choice == "7":
            a.addStudentToCourse()
        elif choice == "8":
            a.removeStudentFromCourse()
        elif choice == "9":
            a.printCourses()
        elif choice == "10":
            a.printRoster()
        elif choice == "11":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")

# ─────────────────────────────────────────────
# MAIN PROGRAM
# ─────────────────────────────────────────────

# Setup tables and seed data (safe to run multiple times — INSERT OR IGNORE)
setup_tables()
seed_data()

# Main login loop
while True:
    uid, role = login()
    if uid is None:
        continue
    if role == "student":
        student_menu(uid)
    elif role == "instructor":
        instructor_menu(uid)
    elif role == "admin":
        admin_menu(uid)
    again = input("\nReturn to login screen? (y/n): ").strip().lower()
    if again != "y":
        break

database.close()