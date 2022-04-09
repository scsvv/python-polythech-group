class Person: 

    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self) -> str:
        return 'name: ' + self.name + self.surname + 'age' + self.age


class Driver(Person):

    def __init__(self, name, surname, age, car):
        self.car = car
        super().__init__(name, surname, age)


class Boss(Person): 

    def __init__(self, name, surname, age, staff):
        self.staff = staff
        super().__init__(name, surname, age)

p1 = Driver('Sviat', 'Skorobohatov', 21, "VW")