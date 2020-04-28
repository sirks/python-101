class Animal:
    def __init__(self, species):
        self.species=species
    
    def breath(self):
        print(f'{self.species} is breathing')
    
    def move(self):
        raise NotImplementedError

class Limb:
    def __init__(self, side_x, side_y):
        self.side_x=side_x
        self.side_y=side_y

    def __str__(self):
        return f'{self.side_x}-{self.side_y}'
    
    def __repr__(self):
        return str(self)

class Head:
    pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__('dog')
        self.name = name
        self.limbs = [
            Limb('right','front'),
            Limb('left','front'),
            Limb('right','rear'),
            Limb('left','rear'),
        ]
        self.head = Head()
    
    def move(self):
        print(f'{self.species} is running by moving {self.limbs}')

class Bird(Animal):
    def __init__(self, species):
        super().__init__(species)
        self.legs = [
            Limb('right','rear'),
            Limb('left','rear'),
        ]
        self.wings=[
            Limb('right','front'),
            Limb('left','front'),
        ]
        self.head = Head()
    def move(self):
        print(f'{self.species} is flying by flapping {self.wings}')

dog = Dog()
# dog.move()
bird = Bird('parrot')
# bird.move()

def moover(animal:Animal):
    animal.move()

# moover(dog)
moover(bird)
# moover('not an animal')

