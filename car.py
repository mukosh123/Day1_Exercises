
class Car:
    def __init__(self, name = 'General', model = 'GM', _type = ''):
        self.type = _type
        self.model = model
        self.name = name
        self.num_of_doors = 4
        if self.name == 'Porshe':
            self.num_of_doors = 2
        if self.name == 'Koenigsegg':
            self.num_of_doors =2
        self.num_of_wheels = 4
        if self.type == 'trailer':
            self.num_of_wheels = 8 
        self.speed = 0

    def is_saloon(self):
        if self.type != 'trailer':
            self.type = 'saloon'
        return True

    def drive(self, speed):
        if self.type == 'trailer':
            self.speed = (speed * 11)
        if self.name == 'Mercedes':
            self.speed = (speed * (1000/3))
        return self





