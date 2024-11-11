#Задача "Магические здания":
class House:
    def __init__(self, name, number_of_house):
        self.name = name
        self.number_of_house = number_of_house

    def go_to(self, new_flor):
        n_f = int(new_flor)
        for i in range(1, n_f + 1):
            if n_f <= 1 or n_f >= self.number_of_house:
                print("Такого этажа не существует")
                break
            else:
                print(i)

    def __len__(self): #возвращает кол-во этажей здания
        return self.number_of_house

    def __str__(self): #возвращает строку: "Название: <название>, кол-во этажей: <этажи>"
        return f'Название: {self.name}, кол-во этажей: {self.number_of_house}'

h1 = House("Дом", 5)
h2 = House("Небоскреб", 38)

print(h1)
print(h2)

print(len(h1))
print(len(h2))