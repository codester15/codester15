# character.py

class RobloxCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Level: {self.level}")

if __name__ == "__main__":
    # Creating an instance of the RobloxCharacter class
    my_character = RobloxCharacter(name="raddogs14", health=100, level="any")
    my_character.display_info()
