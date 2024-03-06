from datetime import date


class EmailAlreadyExists (Exception):
    pass


class Employee:
    def __init__(self, name: str, salary_day: int, email: str) -> None:
        self.name = name
        self.salary_day = salary_day
        self.email = self.save_email(email)

    def work(self) -> str:
        return "I come to the office"

    def save_email(self, email: str) -> str:
        result = self.validate_email(email)
        if result:
            self.email = email
            with open('emails.csv', 'a') as f:
                f.write(email + ' ')
                return self.email

    def validate_email(self, email: str) -> bool:
        try:
            with open('emails.csv', 'r') as f:
                content = f.read()
                word_array = content.split()
                if email in word_array:
                    raise EmailAlreadyExists
                return True
        except EmailAlreadyExists:
            return False

    def __eq__(self, other: 'Employee') -> bool:
        return self.salary_day == other.salary_day

    def __gt__(self, other: 'Employee') -> bool:
        """
        Compare instance with other instance by salary
        :param other: instance of class Employee
        :return: True if they are the same. False if they are not the same
        """
        return self.salary_day > other.salary_day

    def check_salary(self, days=0) -> float:
        if days:
            return self.salary_day * days
        else:
            today_day = date.today().day
            today_month = date.today().month
            today_year = date.today().year
            for i in range(1, today_day + 1):
                if 1 <= date(today_year, today_month, i).isoweekday() <= 5:
                    days += 1
            return self.salary_day * days


class Recruiter(Employee):
    def work(self) -> str:
        return super().work() + " and start to hiring."

    def __str__(self) -> str:
        return f" Recruiter: {self.name}"


class Developer(Employee):
    def __init__(self, name: str, salary_day, tech_stack, email) -> None:
        super().__init__(name, salary_day, email)
        self.tech_stack = tech_stack

    def work(self) -> str:
        return super().work() + " and start to coding."

    def __str__(self) -> str:
        return f" Developer: {self.name}"

    def __eq__(self, other: 'Developer') -> bool:
        return len(self.tech_stack) == len(other.tech_stack)

    def __add__(self, other: 'Developer') -> 'Developer':
        """
        Function create new object from other objects in class Developer
        :param other: other instance
        :return: new instance
        """
        new_name = self.name + ' ' + other.name
        new_stack = set(self.tech_stack + other.tech_stack)
        new_salary = self.salary_day if self.salary_day > other.salary_day else other.salary_day
        email = 'email@email.com'
        return Developer(new_name, new_salary, new_stack, email)


John = Recruiter("John", 200, 'john@email.com')
Maria = Developer("Maria", 400, ['Java', 'Python', 'C++'], 'maria@email.com')
Ivan = Developer("Ivan", 100, ['Java', 'html', 'C#'], 'ivan@email.com')

print(John.__str__())
print(John.work())
print(Maria.__str__())
print(Maria.work())
print(John == Maria)
print(John > Maria)
print(John.check_salary())
print(Maria.check_salary())
print(date.today())
print(Maria.__dict__)
print(Ivan.__dict__)
print(Ivan == Maria)
new_developer = Ivan + Maria
print(new_developer.__dict__)
