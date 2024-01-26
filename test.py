class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    #метод выставления оценки лекторам    
    def rate_lecturer(self, mentor, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    #функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
    def average_student_grades(self):
        sum_grades = 0
        len_grades = 0
        for list_grades in self.grades.values():
            sum_grades += sum(list_grades)
            len_grades += len(list_grades)
        result = round((sum_grades / len_grades), 2)
    
    #перегрузка класса student           
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_student_grades()}\nКурсы в процессе изучения{", ".join(self.courses_in_progress)}\nЗаверешенные курсы: {", ".join(self.finished_courses)}' 
        return result

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super.__init__(name, surname)
        self.grades = {}

    #функция для подсчета средней оценки за лекции всех лекторов в рамках курса
    def awerage_lecturer_grades():
        sum_grades = 0
        len_grades = 0
        for list_grades in self.grades.values():
            sum_grades += sum(list_grades)
            len_grades += len(list_grades)
        result = round((sum_grades / len_grades), 2)
        return result
        
    #перегрузка класса lecturer
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_student_grades()}' 
        return result    
        
    

class Reviewer(Mentor):
    #метод выставления оценки студентам от ревьюеров    
    def rate_student_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    #перегрузка класса reviewer    
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}' 
        return result        
        








#best_student = Student('Ruoy', 'Eman', 'your_gender')
#best_student.courses_in_progress += ['Python']

#cool_mentor = Mentor('Some', 'Buddy')
#cool_mentor.courses_attached += ['Python']

#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)

#print(best_student.grades)
