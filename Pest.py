class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting at midpoint
        self.energy = 5   # Starting at midpoint
        self.happiness = 5  # Starting at midpoint
    
def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} has eaten.")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a good rest.")
