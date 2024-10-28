"""
Создайте класс компания Company, содержащей сотрудников и реализующей методы:
•	найм одного сотрудника — hire(),
•	найм списка сотрудников – hireAll(),
•	увольнение сотрудника – fire(),
•	получение значения дохода компании – getIncome().
Аргументы и возвращаемое значение методов выберите на основании логики работы вашего приложения.
"""

class Employee:
    def __init__(self, name, income):
        self.__name = name
        self.__income = income  # доход сотрудника
    def get_name(self):
        return self.__name
    def get_income_employee(self):
        return self.__income

class Company:
    def __init__(self):
        self.__employees = []
        self.__income = 0.0

    # одного сотрудника
    def hire(self, employee1: Employee):
        self.__employees.append(employee1)

    # список сотрудников
    def hireAll(self, employees: list):
        self.__employees.extend(employees)

    # увольнение
    def fire(self, employee: Employee):
        self.__employees.remove(employee)

    def get_income(self):
        total = 0
        for e in self.__employees:
            total += e.get_income_employee()
        return total
    def get_Employees(self):
        return [e.get_name() for e in self.__employees]


employee1 = Employee('Иван', 1000.34)
employee2 = Employee('Дмитрий', 2991)
employee3 = Employee('Александра', 1393)
employee4 = Employee('Ольга', 9391)

company1 = Company()

company1.hire(employee2)
print(company1.get_Employees())
company1.hireAll([employee1, employee3, employee4])
print(company1.get_Employees())
company1.fire(employee2)
print(company1.get_Employees())
print(f'доход компании: {company1.get_income()}')
