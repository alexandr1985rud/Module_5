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


les = House('Пригород лесное', 17)
vid = House('Новое видное', 10)
# print(les.name, les.number_of_floors)
# print(vid.name, vid.number_of_floors)
les.go_to(20)
vid.go_to(7)
