# Инкапсуляция - упаковка данных и функционала в одно место, внутрь одного компонента.

class Dog:
    count_of_dogs = 2 # свойство класса, одно для всех классов

    def __init__(self, color, age, breed, name): # Конструктор объекта
        # через self уже свойства объекта, указываем для каждого объекта
        self.color = color
        self.age = age
        self.breed = breed
        self.name = name

    def walk(self, place):
        print(f'Собака породы {self.breed}, цвет {self.color}, идёт {place}. Ей {self.age} лет.')


dog1 = Dog('Белый', 0.8, 'Французский бульдог', 'Йода')

print(dog1.color, dog1.age, dog1.breed, dog1.name)

# Наследование

class Yato(Dog):
    def __init__(self, color, age, breed, name, behavior):
        super().__init__(color, age, breed, name)
        self.behavior = behavior

    def pissing(self):
        # Полиморфизм - возможность объектов иметь одинаковые методы с разной реализацией
        if (self.age < 2):
            print('Собака ещё молодая')
        print(f'{self.name} Насцал\n')

dog2 = Yato('Рыжий', 1.8, 'Корги', 'Ято', 'Плохой')

print(dog2.color, dog2.age, dog2.breed, dog2.name, dog2.behavior)
dog2.pissing()
dog2.walk('на улицу')
#hehe haha
