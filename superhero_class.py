# Activity 1: Superhero Class

class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self._level = level  # Encapsulated attribute (protected)

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Level: {self._level}")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

class FlyingHero(Superhero):
    def __init__(self, name, level, wingspan):
        super().__init__(name, "Flight", level)
        self.wingspan = wingspan

    def show_info(self):
        super().show_info()
        print(f"Wingspan: {self.wingspan} meters")

    def use_power(self):
        print(f"{self.name} takes off and soars into the sky! 🕊️")

class Speedster(Superhero):
    def __init__(self, name, level, top_speed):
        super().__init__(name, "Super Speed", level)
        self.top_speed = top_speed

    def show_info(self):
        super().show_info()
        print(f"Top Speed: {self.top_speed} km/h")

    def use_power(self):
        print(f"{self.name} runs at lightning speed! ⚡")

# Example usage
if __name__ == "__main__":
    flash = Speedster("Flash", 90, 1000)
    falcon = FlyingHero("Falcon", 85, 15)

    flash.show_info()
    flash.use_power()

    print("\n---\n")

    falcon.show_info()
    falcon.use_power()
