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

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
         # use of self.raise tp allow to change in object instances
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

# emply1 is pass on as self
emply1 = Employee('brian', 'aginga', 6069)
emply2 = Employee('Mercy', 'macody', 7000)
emply3 = Employee('James', 'lebron', 8000)

print(Employee.num_of_staff)

# looking at every posible scenarios

print(emply1.pay)

# changing data fro only emply1
emply1.raise_amount = 1.14
print(emply1.__dict__)
print(emply1.apply_raise())
print(emply1.pay)
