import random as random

# Game Storage
class Character:
    def __init__(self, first, last, nickname, weapon, element, level):
        self.first = first
        self.last = last
        self.nickname = nickname
        self.weapon = weapon
        self.level = level
        self.health = level * 10
        self.max_hp = level * 10
        self.damage = level * 1
        self.element = element
        self.nation = element + "Nation"
    def fullname(self):
        print(self.first + " " + self.last)
    
    def element_buff(self):
        if self.element == "Fire":
            self.damage *= 2
        elif self.element == "Water":
            self.health *= 2
            self.max_hp *= 2
        elif self.element == "Earth":
            self.damage *= 1.5
            self.health *= 1.5
            self.max_hp *= 1.5
        elif self.element == "Air":
            self.damage *= 1.25
            self.health *= 1.75
            self.max_hp *= 1.75
        elif self.element == "Lightning":
            self.damage *= 1.90
            self.health *= 1.10
            self.max_hp *= 1.10
        
    
















# Beginning Menu
print("Welcome to Elemental Warfare! Elemental Warfare is an rpg game that takes place during a great war between the 5 elemental nations. The fire nation, the water nation, the earth nation, the air nation, and the lightning nation are at war with eachother and it is your duty to claim victory for your nation!")
print("Before we begin, you will create your character!")

print("What would you like your first name to be?")
first = input("> ")
print("{}, what would you like your last name to be?".format(first))
last = input("> ")
print("What would you like your nickname to be? ")
nickname = input("> ")
print("Would you like to be a weapon user? Answer with either 'yes' or 'no'.")
weaponChoice = input("> ")

while weaponChoice != "yes" and weaponChoice != "no":
    print("Answer with either 'yes' or 'no'.")
    weaponChoice = input("> ")

if weaponChoice == "yes":
    print("Choose the weapon you would like to receive. List of weapons below.")
    print("Katana | Spear | Dagger | Scythe")
    weapon = input("> ")
    
    while weapon != "Katana" and weapon != "Spear" and weapon != "Dagger" and weapon != "Scythe":
        print("Error.. answer with either 'Katana', 'Spear', 'Dagger', 'Scythe'.")
        weapon = input("> ")

else:
    weapon = None

print("Now you will receive a random element. Keep in mind, the element you receive will determine the nation you will fight for.")
print("The five elements are Fire, Water, Earth, Air, and Lightning. Enter anything to receive your element.")
input("> ")

elements = ["Fire", "Water", "Earth", "Air", "Lightning"]
element = random.choice(elements)
print("You received the power of {}! You will fight for the {} Nation!".format(element, element))








