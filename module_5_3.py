class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        return self + value

    def __radd__(self, value):
        return self + value


les = House('Пригород Лесное', 17)
vid = House('Новое Видное', 10)
# print(les.name, les.number_of_floors)
# print(vid.name, vid.number_of_floors)

# print(len(les))
# print(len(vid))

print(les)
print(vid)

print(les == vid)

vid = vid + 7
print(vid)
print(les == vid)

les += 10  # __iadd__
print(les)

vid = 10 + vid  # __radd__
print(vid)


print(les < vid)
print(les <= vid)
print(les > vid)
print(les >= vid)
print(les != vid)

# les.go_to(20)
# vid.go_to(7)
