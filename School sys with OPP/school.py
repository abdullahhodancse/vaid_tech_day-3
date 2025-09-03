from course import*    #importe korlam
from stute import*     #importe korlam

class School:   #parent class
    def __init__(self,school_name,school_address):  #constructor aitar subida hoilo varibable felxible vabe neya jai
        self.school_name=school_name  #instance variable ja hoy argument theke na hoy keyword the data nibe ,,,aitar ekta problem holo hoy data dictionary akare dau na hole position thik rakhao
        self.school_address=school_address  #instance variable ja hoy argument theke na hoy keyword the data nibe ,,,aitar ekta problem holo hoy data dictionary akare dau na hole position thik rakhao
        self.students=[] #its a list
        self.teachers=[]  #its a list
        self.courses=[]   #its a list
    

    def show_schoole(self): #function
        return f"School Name:{self.school_name},School Address:{self.school_address}"

    def add_student(self,name,phone,student_id,student_class,student_class_roll,grade):
        student=Student(name,phone,student_id,student_class,student_class_roll,grade)
        self.students.append(student)
        return student
               

    def add_teacher(self,name,phone,teacher_id,subject):
        teacher=Teacher(name,phone,teacher_id,subject)
        self.teachers.append(teacher)
        return teacher
    
    def add_course(self,course_name,course_teacher):
        course=Course(course_name,course_teacher)
        self.courses.append(course)
        return course
    
    def show_all_students(self):
        for s in self.students:
            print(s.show())

    
    def show_all_teachers(self):
        for t in self.teachers:
            print(t.show())
            

    def show_all_course(self):
        for c in self.courses:
            print(c.show_course())





school=School("Hossaindi High School","hossaindi,pakundia kishorehanj,Dhaka,banglasedh")

print(school.show_schoole())

#add students


s1=school.add_student("Abid","017222","ST001","6","30","A+")
   



print("All Students")
print(school.show_all_students())

# add teacher

t1=school.add_teacher("Karim","017333","T001","Math"
    )

print("All Teachers")
print(school.show_all_teachers())


#add course
c1=school.add_course("Hodan","Math")
    
c1.add_student(s1)
c1.add_student(s1)

print ("All subject")
print(school.show_all_course())
                      
                      