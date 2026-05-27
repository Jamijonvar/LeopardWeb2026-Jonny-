#"Applied programming Assignment 1"

#"User Class"
#"Defines the class User and its attributes"
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
    def __init__(self, firstname, lastname, id):
        super().__init__(firstname, lastname, id)

 #   "Method to print the Students firstname, lastname, and ID"
    def printAll(self):
        return super().printAll()

  #  "Method to search for courses"
    def searchCourses(self):
        print("Inside search courses method (student)")

   # "Method to add courses"
    def addCources(self):
        print("Inside adding courses method (student)")

    #"Method to drop courses"
    def dropCourses(self):
        print("Inside the drop courses method (student)")

    #"Method to print the students schedule"
    def printSchedule(self):
        print("Inside the print schedule method (student)")

#"Admin Class"
#"Defines the Admin class and its attributes which are obtained from its parent class User"
class Admin(User):
    def __init__(self, firstname, lastname, id):
        super().__init__(firstname, lastname, id)

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
        print("Inside search roster method (admin)")

    #"Method to print the roster"
    def printRoster(self):
        print("Inside print roster method (admin)")

    #"Method to search courses"
    def searchCourses(self):
        print("Inside search courses method (admin)")

    #"Method to print courses"
    def printCourses(self):
        print("Inside print courses method (admin)")

#"Instructor Class"
#"Defines the Instructor class and its attributes which are obtained from its parent class User"
class Instructor(User):
    def __init__(self, firstname, lastname, id):
        super().__init__(firstname, lastname, id)

    #"Method to print the Instructors firstname, lastname, and ID"
    def printAll(self):
        return super().printAll()

    #"Method to print schedule"
    def printSchedule(self):
        print("Inside print schedule method (Instructor)")

    #"Method to print class list"
    def classList(self):
        print("Inside print class list method (Instructor)")

    #"Method to search for courses"
    def courseSearch(self):
        print("Inside course search method (Instructor)")

#"Test cases for the User class"

#"Adds a new User (user1) and sets their firstname, lastname, and ID"
user1 = User("Sophia", "Johnson", 10000001)
#"Prints the user1's firstname, lastname, and ID"
user1.printAll()

#"Test cases for the Student class"

#"Adds a new Student (student1) and sets their firstname, lastname, and ID"
student1 = Student("Sarah", "Miller", 100000002)
#"Prints student1's firstname, lastname, and ID"
student1.printAll()
#"Calls the searchCourses method"
student1.searchCourses()
#"Calls the addCourses method"
student1.addCources()
#"Calls the dropCourses method"
student1.dropCourses()
#"Prints student1's schedule"
student1.printSchedule()

#"Test cases for the Admin Class"

#"Adds a new Admin (admin1) and sets their firstname, lastname, and ID"
admin1 = Admin("Tina", "White", 100000003)
#"Prints the admin1's firstname, lastname, and ID"
admin1.printAll()
#"Calls the addCourses method"
admin1.addCourses()
#"Calls the removeCourses method"
admin1.removeCourses()
#"Calls the addUser method"
admin1.addUser()
#"Calls the removeUser method"
admin1.removeUser()
#"Calls the addStudent method"
admin1.addStudent()
#"Calls the removeStudent method"
admin1.removeStudent()
#"Calls the searchRoster method"
admin1.searchRoster()
#"Prints the Roster"
admin1.printRoster()
#"Calls the searchCourses method"
admin1.searchCourses()
#"Prints the courses"
admin1.printCourses()

#"Test cases for the Instructor Class"

#"Adds a new Instructor (instructor1) and sets their firstname, lastname, and ID"
instructor1 = Instructor("Ruby", "Smith", 100000004)
#"Prints the instructor1's firstname, lastname, and ID"
instructor1.printAll()
#"Prints instructor1's schedule"
instructor1.printSchedule()
#"Prints instructor1's class list"
instructor1.classList()
#"Calls the courseSearch method"
instructor1.courseSearch()
