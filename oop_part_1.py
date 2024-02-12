
mylist = [1, 2, 3]

mylist.append(4)

print(type(32.5))  # create own class


class Sample:
    pass


x = Sample()

print(type(x))


class Dog:

    def __init__(self, breed):
        self.breed = breed


x = Dog(breed="lab")

print(type(x))
print(x.breed)


class Dog:

    # Class Object Attributes
    species = "mammal"

    def __init__(self, breed, name):  # b.attribute
        self.breed = breed
        self.name = name


sam = Dog("huskie", "sammy")

# print(x.breed)
print(sam.breed)
print(sam.name)
print(sam.species)
