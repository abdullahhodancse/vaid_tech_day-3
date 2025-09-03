class person: #parent class
    def __init__(self,name,phone): #constructor
        self.name=name
        self.phone=phone


    def show(self): #function
        pass


class Student(person): # child class
    def __init__(self,name,phone,student_id,student_class,student_class_roll,grade):
        super().__init__(name,phone) #aita use kore parent er variable r call kora lage na
        self.__student_id=student_id  #instance variable ja hoy argument theke na hoy keyword the data nibe ,,,aitar ekta problem holo hoy data dictionary akare dau na hole position thik rakhao
        self.student_class=student_class
        self.student_class_roll=student_class_roll
        self.__grade=grade

    def show(self):
        return f"Student Name:{self.name},phone:{self.phone}Student ID:{self.__student_id}, Class:{self.student_class},Class Roll:{self.student_class_roll},Grade:{self.__grade}"


class Teacher(person): #chils class
    def __init__(self,name,phone,teacher_id,subject):
        super().__init__(name,phone)   #aita use kore parent er variable r call kora lage na
        self.__teacher_id=teacher_id  #instance variable ja hoy argument theke na hoy keyword the data nibe ,,,aitar ekta problem holo hoy data dictionary akare dau na hole position thik rakhao
        self.subject=subject

    def show(self):
        return f"Teacher Name:{self.name},Teacher ID:{self.__teacher_id},Subject:{self.subject}"
    


s1=Student("Abid","017222","ST001","6","30","A+") 
print(s1.show())   
        
t1=Teacher("Karim","017333","T001","Math")   
print(t1.show())     