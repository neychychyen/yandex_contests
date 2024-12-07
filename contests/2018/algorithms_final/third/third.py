class Person:
    def __init__(self, energy):
        self.energy = energy
        self.sinker = 0


    def __add__(self, food_weight: int) -> None:
        self.sinker += food_weight

    def step(self) -> bool:
        if self.energy - (self.sinker + 1) >= 0:
            self.energy -= (self.sinker + 1)
            print(self.energy)
            return True
        else:
            return False

    def __repr__(self):
        return str(self.energy)



x = Person(2)
x + 1
print(x.sinker)
print(x)

print(x.step())
