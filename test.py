class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    #метод выставления оценки лекторам    
    def rate_lecturer(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    #функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
    def average_grades(self):
        sum_grades = 0
        len_grades = 0
        for list_grades in self.grades.values():
            sum_grades += sum(list_grades)
            len_grades += len(list_grades)
        result = round((sum_grades / len_grades), 1)
    
    #перегрузка класса student           
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grades()}\nКурсы в процессе изучения{", ".join(self.courses_in_progress)}\nЗаверешенные курсы: {", ".join(self.finished_courses)}' 
        return result
    
    #метод выбора студента, относящегося к курсу
    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other} - не является студентом')
            return
        return self.average_grades() < other.average_grades()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    #функция для подсчета средней оценки за лекции всех лекторов в рамках курса
    def average_grades():
        sum_grades = 0
        len_grades = 0
        for list_grades in self.grades.values():
            sum_grades += sum(list_grades)
            len_grades += len(list_grades)
        result = round((sum_grades / len_grades), 1)
        return result
        
    #перегрузка класса lecturer
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades()}' 
        return result   
        
    #метод проверки является ли лектором    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other} - не является лектором')
            return
        return self.average_grades() < other.average_grades()    
    

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


lecturer_1 = Lecturer('Oleg', 'Sidorov')
lecturer_1.courses_attached = ['Python', 'Java']
lecturer_1.grades = {'Python': [7, 9, 9, 10], 'Java': [7, 8, 9, 10]}
    
lecturer_2 = Lecturer('Zina', 'Soboleva')
lecturer_2.courses_attached = ['Python', 'Java']
lecturer_2.grades = {'Python': [6, 6, 9, 10], 'Java': [7, 8, 9, 10]}
    
lecturer_3 = Lecturer('Zina', 'Soboleva')
lecturer_3.courses_attached = ['Python', 'Java']
lecturer_3.grades = {'Java': [9, 9, 9, 10]}

list_lecturer = [lecturer_1, lecturer_2, lecturer_3]

def average_grades_lecturers(list_lecturer, courses):
    summary_grades = 0
    number_grades = 0
    for lecturer in list_lecturer:
        if courses in lecturer.grades:
            grades = lecturer.grades[courses]
            sum_grades = sum(grades)
            len_grades = len(grades)
            summary_grades += sum_grades
            number_grades += len_grades
        else:
            continue
    return summary_grades / number_grades
print(average_grades_lecturers(list_lecturer, 'Java'))

    # Проверка методов
#print(oleg_lec.average_grades())
#print(zina_lec.average_grades())
#print(oleg_lec)
#print(zina_lec)
#print(oleg_lec < zina_lec)



#list_student = [ivan_st, rita_st, ritaa_st]

def average_grades_students(list_student, courses):
    summary_grades = 0
    number_grades = 0
    for student in list_student:
        if courses in student.grades:
            grades = student.grades[courses]
            sum_grades = sum(grades)
            len_grades = len(grades)
            summary_grades += sum_grades
            number_grades += len_grades
        else:
            continue
    return sum_grades / number_grades
#print(average_grades_students(list_student, 'Git'))
