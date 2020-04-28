class Car:
    def __init__(self, color, weight, licence_plate):
        self.licence_plate=licence_plate
        self.color=color
        self.weight=weight
        self.distance=0
    
    def drive(self, distance):
        self.distance+=distance

some_car = Car('red',1234,'LI-1234')
some_car.drive(99)

print(f'color = {some_car.color}')
print(f'distance = {some_car.distance}')
some_car.drive(99)
print(f'distance = {some_car.distance}')