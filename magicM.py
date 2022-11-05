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
    # debugging
    def __repr__(self):

        return f'{self.first} {self.last} {self.pay}'

    #readable for the end user
    def __str__(self):

        return f'{self.full_name()}, {self.email}'

    #combine employee salary
    def __add__(self, other):
        return self.pay + other.pay

    # getting total number of character
    def __len__(self):

        return len(self.full_name())


def main():
    emply1 = Employee('brian', 'aginga', 6069)
    emply2 = Employee('Mercy', 'macody', 7000)

    print(repr(emply1))
    print(str(emply1))
    print(emply1 + emply2)

    print(len(emply1))


main()