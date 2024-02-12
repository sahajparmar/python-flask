class Dog:

    # Class Object Attributes
    species = "mammal"

    def __init__(self, breed, name):  # b.attribute
        self.breed = breed
        self.name = name


sam = Dog("huskie", "sammy")
new_dog = Dog("golden", "cindy")

# print(x.breed)
print(sam.breed)
print(sam.name)
print(sam.species)
print(new_dog.species)


class circle:

    # Class Object Attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):  # message
        return self.radius * self.radius * self.pi


mycircle = circle(10)
print(mycircle.radius)
print(mycircle.area())
