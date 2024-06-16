class Fruit:
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"
        self.name = "Apple"

honeycrisp = Fruit()
print(honeycrisp.color)


class Fruit:
    ##Contructor
    def __init__(self, name, color, flavor):
        self.name = name
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "a fruit which is {} and {}".format(self.name, self.color, self.flavor)

fruit = Fruit("Apply","red", "sweet")
print(fruit)
#or 
print(f'This {fruit.name} is so {fruit.flavor}')
