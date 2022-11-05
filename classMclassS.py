import datetime

class Employee:

    # class variable
    raise_amount = 1.12
    num_of_staff = 0

    def __init__(self, first, last, pay):

        # setting up a instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email  = first + '.' + last +'@company.com'

        Employee.num_of_staff += 1

    # putting functionality in one place
    # use self so that it work with all instances
    # regular method take self as first argument
    # self is instance variable
    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
         # use of self.raise tp allow to change in object instances
        self.pay = int(self.pay * self.raise_amount)
        return self.pay
    
    @classmethod
    def set_raise_fee(cls, amount):
        
        cls.raise_amount = amount

    #using class method as alternative constructor
    @classmethod
    def from_str(cls, emp_str):
        first, last , pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):

        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    

# emply1 is pass on as self
# instanciating
emply1 = Employee('brian', 'aginga', 6069)
emply2 = Employee('Mercy', 'macody', 7000)
emply3 = Employee('James', 'lebron', 8000)

# change the raise amount using class method
#Employee.set_raise_fee(2.09)
#name = 'ruth-berly-5863'
#new_emp4 = Employee.from_str(name)


my_date = datetime.date(2022, 5, 11)

print(Employee.is_workday(my_date))
