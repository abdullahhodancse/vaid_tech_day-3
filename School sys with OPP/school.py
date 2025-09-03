from course import*    #importe korlam
from stute import*     #importe korlam

class School:   #parent class
    def __init__(self,*arges,**kwargs):  #constructor aitar subida hoilo varibable felxible vabe neya jai
        self.school_name=kwargs.get("school_name",arges[0] if len(arges)>0 else None)  #instance variable ja hoy argument theke na hoy keyword the data nibe ,,,aitar ekta problem holo hoy data dictionary akare dau na hole position thik rakhao
        self.school_address=kwargs.get("school_address",arges[1] if len(arges)>1 else None)  #instance variable ja hoy argument theke na hoy keyword the data nibe ,,,aitar ekta problem holo hoy data dictionary akare dau na hole position thik rakhao
        self.students=[] #its a list
        self.teachers=[]  #its a list
        self.courses=[]   #its a list
    

    def show_schoole(self): #function
        return f"School Name:{self.school_name},School Address:{self.school_address}"

    def add_student(self,*arges,**kwargs):
        student=Student(*arges,**kwargs)
        self.students.append(student)
        return student
               

    def add_teacher(self,*arges,**kwargs):
        teacher=Teacher(*arges,**kwargs)
        self.teachers.append(teacher)
        return teacher
    
    def add_course(self,*arges,**kwargs):
        course=Course(*arges,**kwargs)
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
s1=school.add_student(
    name="Korimn",
    student_id="ST001",
    student_class="6",
    student_class_roll="30",
    grade="A+")

s1=school.add_student(
    name="Korimn",
    student_id="ST001",
    student_class="6",
    student_class_roll="30",
    grade="A+")

s1=school.add_student(
    name="Korimn",
    student_id="ST001",
    student_class="6",
    student_class_roll="30",
    grade="A+")

print("All Students")
print(school.show_all_students())

# add teacher

t1=school.add_teacher(
    name="Robi",
    teacher_id="T012",
    subject="bangla")

print("All Teachers")
print(school.show_all_teachers())


#add course
c1=school.add_course(
    course_name="Bangla",
    course_teacher="anik"

)
print ("All subject")
print(school.show_all_course())
                      
                      