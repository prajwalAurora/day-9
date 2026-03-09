class Student:
    def __init__(self,fullname):
        self.name=fullname
        print("adding new student to database")

s1=Student("Praj")
print(s1.name)