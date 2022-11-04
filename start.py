class Employee:

    def __init__(self, first, last, pay):

        # setting up a instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email  = first + '.' + last +'@company.com'

    # putting functionality in one place
    # use self so that it work with all instances

    def full_name(self):
        return f'{self.first} {self.last}'

    pass

# emply1 is pass on as self
emply1 = Employee('brian', 'aginga', 6000)
emply2 = Employee('Mercy', 'macody', 7000)
emply3 = Employee('James', 'lebron', 8000)

# looking at every posible scenarios
print(emply2.full_name())
print(emply1.full_name())
print(Employee.full_name(emply3))

