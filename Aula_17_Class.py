class Fruit:
    #Contructor
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"
        self.name = "Apple"

fruit = Fruit()
print(fruit.color)


class Fruit:
    #Contructor
    def __init__(self, name, color, flavor):
        self.name = name
        self.color = color
        self.flavor = flavor

    #Method that return value
    def eat(self):
        return f'I am eating a {self.name}'

    #Method with out return value
    def eat(self):
        print(f'I am eating a {self.name}')
        
    def __str__(self):
        return "an {} which is {} and {}".format(self.name, self.color, self.flavor)

fruit = Fruit("Apply","red", "sweet")
print(fruit)
#or 
print(f'This {fruit.name} is so {fruit.flavor}')
