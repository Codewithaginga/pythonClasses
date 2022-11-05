class Employee:

    def __init__(self, first, last):

        # setting up a instance variable
        self.first = first
        self.last = last
    # accessing a function like an attribute
    @property
    def email(self):

        return f'{self.first}{self.last}@gmail.com'
    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @full_name.setter

    def full_name(self, name):
        first, last = name.split(' ')

        self.first = first
        self.last = last


    

def main():
    emply1 = Employee('brian', 'aginga')
    emply2 = Employee('Mercy', 'macody')
    # emply1.first = 'madiang'
    emply1.full_name = 'james madiang'
    print(emply1.first)
    print(emply1.email)
    print(emply1.full_name)


main()