class Maksym:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculate_course(self):
        if self.birth_year is None:
            return None
        current_year = 2025
        start_year = self.birth_year + 17
        course = current_year - start_year + 1
        return max(1, min(course, 4)) if course > 0 else None

    def get_name_list(self):
        return [self.first_name, self.last_name]

student = Maksym("Maksym", "Nezdiur", 2007)
print(student.calculate_course())
print(student.get_name_list())