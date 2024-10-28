'''
Создать базовый класс – работник, и производные классы – служащий с почасовой оплатой, служащий в штате и служащий с процентной ставкой.
Определить функцию начисления зарплаты
'''

class Worker:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class EmployeeHourlyPay(Worker):
    def __init__(self, name, hours, price):
        Worker.__init__(self, name)
        self.__hours = hours
        self.__price = price

    def calculate_pay(self):
        return self.__hours * self.__price

class EmployeeState(Worker):
    def __init__(self, name, salary):
        Worker.__init__(self, name)
        self.__salary = salary

    def calculate_pay(self):
        return self.__salary


class EmployeeInterestRate(Worker):
    def __init__(self, name, scope_work):
        self.__basic_salary = 10000  # базовый оклад
        self.__interest_rate = 0.15  # процент ставка
        Worker.__init__(self, name)
        self.__scope_work = scope_work # объем выполненной работы

    def calculate_pay(self):
        if (self.__scope_work > 100):
            return self.__basic_salary + (self.__interest_rate * self.__scope_work)
        else:
            return self.__basic_salary

w1 = EmployeeHourlyPay('Иван', 8, 1000.4)
print(f'{w1.get_name()}: {w1.calculate_pay()}')

w2 = EmployeeState('Дмитрий', 55295.133)
print(f'{w2.get_name()}: {w2.calculate_pay()}')

w3 = EmployeeInterestRate('Александра', 257)
print(f'{w3.get_name()}: {w3.calculate_pay()}')
