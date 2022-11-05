
class Employee:

    # class variable
    raise_amount = 1.04

    def __init__(self, first, last, pay):

        # setting up a instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email  = first + '.' + last +'@company.com'

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
         # use of self.raise tp allow to change in object instances
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, major):
        super().__init__(first, last, pay)

        self.major = major


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if employees is None:

            self.employees = []

        else:
            self.employees = employees

    def add_employ(self, employ):
        if employ not in self.employees:
            self.employees.append(employ)

    def remove_employ(self, employ):
        if employ  in self.employees:
            self.employees.remove(employ)

    def show_employs(self):

        for emp in self.employees:
            print(f'-->{emp.full_name()}')

    

# emply1 is pass on as self
# instanciating
emply1 = Developer('brian', 'aginga', 6069, 'python')
emply2 = Developer('Mercy', 'macody', 7000, 'Javascript')
emply3 = Developer('James', 'lebron', 8000, 'Golang')

mrg1 = Manager('irene', 'koki', 900000, [emply1])

def main():
    print(mrg1.email)
    mrg1.show_employs()

    print(isinstance(mrg1, Manager))
    print(issubclass(Manager, Developer))


main()





