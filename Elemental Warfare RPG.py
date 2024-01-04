import random as random

# Game Storage
class Character:
    def __init__(self, first, last, nickname, element, level, light, strong, ultimate):
        self.first = first
        self.last = last
        self.nickname = nickname
        self.level = level
        self.damage = level
        self.health = self.level * 10.0
        self.element = element
        self.nation = element + " Nation"
        self.light = light
        self.strong = strong
        self.ultimate = ultimate

    def fullname(self):
        return self.first + " " + self.last
    
    @property
    def max_damage(self):
        if self.element == "Fire":
            return self.level * 2
        elif self.element == "Air":
            return self.level * 1.25
        elif self.element == "Earth":
            return self.level * 1.5
        elif self.element == "Lightning":
            return self.level * 1.25
        else:
            return self.level

    @property
    def light_attack(self):
        return self.damage * 1.5
    
    @property
    def strong_attack(self):
        return self.damage * 2.5
    
    @property
    def ultimate_attack(self):
        return self.damage * 5
    
    @property
    def max_health(self):
        if self.element == "Air":
            return self.level * 10 * 1.25
        elif self.element == "Earth":
            return self.level * 10 * 1.5
        elif self.element == "Water":
            return self.level * 10 * 2
        elif self.element == "Lightning":
            return self.level * 10 * 1.25
        else:
            return self.level * 10
    
    def apply_buff(self):
        self.damage = self.max_damage
        self.health = self.max_health

    def apply_level(self, num):
        self.level += num
        self.health = self.max_health
        self.damage = self.max_damage
    

# Beginning Menu
print("Welcome to Elemental Warfare! Elemental Warfare is an rpg game that takes place during a great war between the 5 elemental nations. The fire nation, the water nation, the earth nation, the air nation, and the lightning nation are at war with eachother and it is your duty to claim victory for your nation!")

print("Before we begin, you will create your character!")

print("What would you like your first name to be?")
first = input("> ")
print("{}, what would you like your last name to be?".format(first))
last = input("> ")
print("What would you like your nickname to be? ")
nickname = input("> ")

print("Now you will receive a random element. Keep in mind, the element you receive will determine the nation you will fight for.")
print("The five elements are Fire, Water, Earth, Air, and Lightning. Enter anything to receive your element.")
input("> ")

elements = ["Fire", "Water", "Earth", "Air", "Lightning"]
element = random.choice(elements)
print("You received the power of {}! You will fight for the {} Nation!".format(element, element))

print("Now that you have received your element, you will begin to train to level up and fight the enemy nations.")
print("Your starting level is 1 and the max level is 10. You will need to defeat 3 enemies to reach max level.")
print("Before then, you will choose your first move. You will have two options, choose wisely.")
if element == "Fire":
    print("The first attack will be a light attack. Your options are below.")
    print("Fire Flies|Fire Ball")
    light = input("> ")
    while light != "Fire Flies" and light != "Fire Ball":
        print("Make sure to type the attack correctly. Your options are below.")
        print("Fire Flies|Fire Ball")
        light = input("> ")

elif element == "Water":
    print("The first attack will be a light attack. Your options are below.")
    print("Aqua Bullets|Water Spear")
    light = input("> ")
    while light != "Aqua Bullets" and light != "Water Spear":
        print("Make sure to type the attack correctly. Your options are below.")
        print("Aqua Bullets|Water Spear")
        light = input("> ")

elif element == "Earth":
    print("The first attack will be a light attack. Your options are below.")
    print("Earth Punch|Raining Rocks")
    light = input("> ")
    while light != "Earth Punch" and light != "Raining Rocks":
        print("Make sure to type the attack correctly. Your options are below.")
        print("Earth Punch|Raining Rocks")
        light = input("> ")

elif element == "Air":
    print("The first attack will be a light attack. Your options are below.")
    print("Wind Bullets|Wind Cutter")
    light = input("> ")
    while light != "Wind Bullets" and light != "Wind Cutter":
        print("Make sure to type the attack correctly. Your options are below.")
        print("Wind Bullets|Wind Cutter")
        light = input("> ")

elif element == "Lightning":
    print("The first attack will be a light attack. Your options are below.")
    print("Flashing Bolt|Quick Jab")
    light = input("> ")
    while light != "Flashing Bolt" and light != "Quick Jab":
        print("Make sure to type the attack correctly. Your options are below.")
        print("Flashing Bolt|Quick Jab")
        light = input("> ")

print("You are now ready to begin your adventure! Type anything to continue!")
input("> ")

player = Character(first, last, nickname, element, 1, light, None, None)
player.apply_buff()
enemy_1 = Character("Bol", "Dar", "The Mushroom", "Fire", 1, "Fire Ball", None, None)
enemy_2 = Character("Con", "Sol", "The Dwarf", "Water", 2, "Aqua bullets", None, None)

print("Welcome {full}, you are officially a part of the {nation}! Your element is {element}, your level is {level}, and your health is {health}".format(full=player.nickname, nation=player.nation, element=player.element, level=player.level, health=player.health))
print("Your first task is to get to the max level by defeating 3 enemies. The enemies will go from weakest to strongest.")
print("You will use your light attack, {light}, to defeat these enemies. You will receive a strong attack once you reach level 5 and then receive an ultimate attack once you reach level 10.".format(light=player.light))
print("If you are ready to fight the first enemy? Enter 'yes' to continue.")
ready = input("> ")

while ready != "yes":
    print("Enter 'yes' to continue.")
    ready = input("> ")

if ready == "yes":
    print("Your first enemy is {name} {last}, also known as {nick}. His level is only {level} so this battle shouldn't be too difficult! He uses the {element} element and uses the {attack} attack.".format(name=enemy_1.first, last=enemy_1.last, nick=enemy_1.nickname,level=enemy_1.level, element=enemy_1.element, attack=enemy_1.light))
    print("If you win this battle, you will receive 2 levels and reach level 3!")
    print("Type anything to continue.")
    input("> ")

print("Enter the name of your attack, {}, to attack your opponent.".format(player.light))

while True:
    attack_1 = input("> ")
    
    while attack_1 != player.light:
        print("Make sure to enter the name of your attack, {}, to attack your opponent.".format(player.light))
        attack_1 = input("> ")
    
    if attack_1 == player.light:
        enemy_1.health -= player.light_attack
    
    if enemy_1.health <= 10 and enemy_1.health >= 0.1:
        print("Keep attacking, your enemys health is at {}.".format(enemy_1.health))
    
    if enemy_1.health <= 0:
        player.apply_level(2)
        break

print("Congratulations on defeating your first opponent!")
print("You are officially level {}! Now it is time to battle the second enemy! If you defeat this enemy you will receive 3 levels and unlock your strong attack!".format(player.level))
print("Your second enemy is {first} {last}, also known as {nick}. His level is {level} so this battle is a bit more difficult! He uses the {element} element and uses the {attack} attack.".format(first=enemy_2.first, last=enemy_2.last, nick=enemy_2.nickname, level=enemy_2.level, element=enemy_2.element, attack=enemy_2.light))
print("This enemy attacks back so be careful! Enter anything to continue.")
f = input("> ")

print("Enter the name of your attack, {}, to attack your opponent.".format(player.light))

while True:
    attack_2 = input("> ")

    while attack_2 != player.light:
        print("Make sure to enter the name of your attack, {}, to atack your opponent.".format(player.light))
        attack_2 = input("> ")

    if attack_2 == player.light:
        enemy_2.health -= player.light_attack

    if enemy_2.health <= 20 and enemy_2.health >= 0.1:
        print("Keep attacking, your enemys health is at {}.".format(enemy_2.health))

    if enemy_2.health <= 0:
        player.apply_level(3)
        break
    
    







