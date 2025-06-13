class Maksym:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name  # Ім'я студента
        self.last_name = last_name  # Прізвище студента
        self.birth_year = birth_year  # Рік народження студента

    def calculate_course(self):
        """Метод обчислює курс навчання студента залежно від року народження"""
        if self.birth_year is None:
            return None  # Якщо рік народження не вказано, повертаємо None
        current_year = 2025  # Поточний рік
        start_year = self.birth_year + 17  # Рік вступу в університет (припустимо, що вступ у 17 років)
        course = current_year - start_year + 1  # Обчислюємо курс
        return max(1, min(course, 4)) if course > 0 else None  # Курс може бути від 1 до 4


class AdvancedIllya(Maksym):
    def __init__(self, first_name=None, last_name=None, birth_year=None, university=None, major=None, gpa=None):
        super().__init__(first_name, last_name, birth_year)  # Викликаємо конструктор батьківського класу
        self.university = university  # Назва університету
        self.major = major  # Спеціальність
        self.gpa = gpa  # Середній бал
        self._student_id = self._generate_student_id()  # Захищений атрибут (ID студента)

    def _generate_student_id(self):
        """Захищений метод для генерації унікального ID студента"""
        return f"{self.last_name[:3].upper()}{self.birth_year % 100}{id(self) % 10000}"  # Формуємо унікальний ID

    def get_full_info(self):
        """Метод повертає повну інформацію про студента"""
        return {
            "Ім'я": self.first_name,  # Зберігає ім'я
            "Прізвище": self.last_name,  # Зберігає прізвище
            "Рік народження": self.birth_year,  # Зберігає рік народження
            "Курс": self.calculate_course(),  # Обчислює курс навчання
            "Університет": self.university,  # Зберігає назву університету
            "Спеціальність": self.major,  # Зберігає спеціальність
            "Середній бал": self.gpa,  # Зберігає середній бал студента
            "ID студента": self._student_id  # Виводить згенерований ID студента
        }

    def is_scholarship_eligible(self):
        """Метод перевіряє, чи студент має право на стипендію (GPA >= 85)"""
        return self.gpa is not None and self.gpa >= 85  # Повертає True, якщо бал >= 85, інакше False


# Приклад використання
student = AdvancedIllya("Anton", "Mazur", 2007, "ТФК ЛНТУ", "Програмування", 150)# Створюємо екземпляр класу
print(student.get_full_info())  # Виводимо всю інформацію про студента
print("Стипендія:", "Так" if student.is_scholarship_eligible() else "Ні")  # Перевіряємо, чи є стипендія