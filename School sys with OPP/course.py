class Course:     # normal class becarar kono chaild nai
    def __init__(self,course_name,course_teacher):  #constructor aitar subida hoilo varibable felxible vabe neya jai
        self.course_name=course_name #instance variable ja hoy argument theke na hoy keyword the data nibe ,,,aitar ekta problem holo hoy data dictionary akare dau na hole position thik rakhao
        self.course_teacher=course_teacher #instance variable ja hoy argument theke na hoy keyword the data nibe ,,,aitar ekta problem holo hoy data dictionary akare dau na hole position thik rakhao
        self.students=[] #ists a list



    def add_student(self,student):  #course e kara kara add hobe taler append kora hobe ai khane
        self.students.append(student)



    def show_course(self):
        student_name=", ".join([stu.name for stu in self.students]) if self.students else "Empty"# accha aitar kahini hoilo syudent der list  " ", soho add kora,,,like=["korim","rohim"]

        return f"Course Name:{self.course_name},Course Teacher:{self.course_teacher},students:[{student_name}]" 
        

c1=Course("Hodan","Math")
print(c1.show_course())
    