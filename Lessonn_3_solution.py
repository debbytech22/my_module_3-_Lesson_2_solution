class Students:
    def __init__(self,fname,lname,student=[]):
        self.fname = fname
        self.lname = lname
        self.email = fname + "." + lname + "@stutern.com"

        # def fullname(self):
        #     return  "{} {}".format(self.fname,self.lname)

stud_1 = Students("Bukola","Dare")
stud_2 = Students("Temitope","Balogun")

        # Question 1
class Group_Leader(Students):
        def __init__(self,fname,lname,student=[]):
            self.student = student
            super().__init__(fname,lname)
        

        # Question 2
        def add_students(self,student):
            self.student.append(student)
            print( self.student,student)

            # Question 3
        def remove_student(self,student):
            self.student.remove(student)
            print(f"student {student} remove from students list{self.student}")

             # Question 4
        def fullname_Student(self):
            return  "{} {}".format(self.fname,self.lname)

            # Question 5
stud_3 = Students("Kemisola","Aromise")
Stud_4 = Students("Temitayo","Foluwe")
Stud_5 = Students("Telemi","Adekoya")

     # Question 6
Group_Leader_1 = Group_Leader("Tito","Alabi")
Group_Leader_2 = Group_Leader("Kola","Owolabi")

        # Question 7
Group_Leader_1.add_students("Toni")
Group_Leader_1.add_students("Bola")
Group_Leader_2.add_students("Folakemi")
Group_Leader_2.add_students("Desire")
        #Qestion 8
Group_Leader_1.remove_student("Bola")
Group_Leader_2.remove_student("Desire")
        #Question 9
print(Group_Leader_1.fullname_Student())
print(Group_Leader_2.fullname_Student())     

def stud_email(self, fname,lname ):
    self.email = fname + "." + lname + "@stutern.com"
print(Group_Leader_1.email)
print(Group_Leader_2.email)
