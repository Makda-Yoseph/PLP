# Activity one
class Smartphone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

# Inherited class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, price, gpu):
        super().__init__(brand, model, storage, price)
        self.gpu = gpu

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with GPU {self.gpu}!")

# Create objects
phone1 = Smartphone("Apple", "iPhone 15", "128GB", 999)
phone2 = GamingPhone("ASUS", "ROG Phone 7", "256GB", 799, "Adreno 730")

# Test methods
phone1.make_call("123-456-7890")
phone2.play_game("Genshin Impact")

# Activity 2

class Vehicle:
    def move(self):
        pass  # Base class method

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
