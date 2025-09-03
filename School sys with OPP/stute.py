class person:#parent class
    def __init__(self,*arges,**kwargs): #constructor
        self.name=kwargs.get("name",arges[0] if len(arges)>0 else None) #instance variable ja hoy argument theke na hoy keyword the data nibe ,,,aitar ekta problem holo hoy data dictionary akare dau na hole position thik rakhao
        self.phone=kwargs.get("phone",arges[1] if len(arges)>1 else None)
        


        def show(self): #function
            pass


class Student(person): # child class
    def __init__(self,*arges,**kwargs):
        super().__init__(*arges,**kwargs) #aita use kore parent er variable r call kora lage na
        self.__student_id=kwargs.get("student_id",arges[2] if len(arges)>2 else None)  #instance variable ja hoy argument theke na hoy keyword the data nibe ,,,aitar ekta problem holo hoy data dictionary akare dau na hole position thik rakhao
        self.student_class=kwargs.get("student_class",arges[3] if len(arges)>3 else None)
        self.student_class_roll=kwargs.get("student_class_roll",arges[4] if len(arges)>4 else None)
        self.__grade=kwargs.get("grade",arges[5] if len(arges)>5 else None)

    def show(self):
        return f"Student Name:{self.name},Student ID:{self.__student_id}, Class:{self.student_class,}Class Roll:{self.student_class_roll},Grade:{self.__grade}"


class Teacher(person): #chils class
    def __init__(self,*arges,**kwargs):
        super().__init__(*arges,**kwargs)   #aita use kore parent er variable r call kora lage na
        self.__teacher_id=kwargs.get("teacher_id",arges[2] if len(arges)>2 else None)  #instance variable ja hoy argument theke na hoy keyword the data nibe ,,,aitar ekta problem holo hoy data dictionary akare dau na hole position thik rakhao
        self.subject=kwargs.get("subject",arges[3] if len(arges)>3 else None)

    def show(self):
        return f"Teacher Name:{self.name},Teacher ID:{self.__teacher_id},Subject:{self.subject}"
        
        