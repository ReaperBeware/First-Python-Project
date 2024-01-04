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
    def enemy_nation(self):
        if self.element == "Fire":
            return "Water"
        elif self.element == "Water":
            return "Fire"
        elif self.element == "Air":
            return "Earth"
        elif self.element == "Earth":
            return "Lightning"
        elif self.element == "Lightning":
            return "Air"

    @property
    def max_damage(self):
        if self.element == "Fire":
            return self.level * 2
        elif self.element == "Air":
            return self.level * 1.25
        elif self.element == "Earth":
            return self.level * 1.5
        elif self.element == "Lightning":
            return self.level * 1.75
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
    
    def apply_hp(self):
        self.health = self.max_health

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

# main game
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
input("> ")

print("Enter the name of your attack, {}, to attack your opponent.".format(player.light))

while True:
    attack_2 = input("> ")

    while attack_2 != player.light:
        print("Make sure to enter the name of your attack, {}, to attack your opponent.".format(player.light))
        attack_2 = input("> ")

    if attack_2 == player.light:
        enemy_2.health -= player.light_attack
        player.health -= enemy_2.light_attack

    if enemy_2.health <= 20 and enemy_2.health >= 0.1:
        print("Keep attacking, your enemys health is at {}.".format(enemy_2.health))
        print("{nick} hit you with the {attack} attack! Your health is now at {health}".format(nick=enemy_2.nickname, attack=enemy_2.light, health=player.health))

    if enemy_2.health <= 0:
        player.apply_level(3)
        break
    
print("Congratulations on defeating the second enemy!")
print("You are officially level {}! Now it is time to choose your strong attack! Enter anything to continue.".format(player.level))
input("> ")

print("You will now choose a strong attack. Your options are below.")

if element == "Fire":
    print("Flaming Uppercut|Flaming Pillar")
    strong = input("<")
    while strong != "Flaming Uppercut" and strong != "Flaming Pillar":
        print("Make sure to enter the name of the attack correctly, your options are below.")
        print("Flaming Uppercut|Flaming Pillar")
        strong = input("> ")
elif element == "Water":
    print("Hydro Blast|Water Prison")
    strong = input("< ")
    while strong != "Hydro Blast" and strong != "Water Prison":
        print("Make sure to enter the name of the attack correctly, your options are below.")
        print("Hydro Blast|Water Prison")
        strong = input("> ")
elif element == "Earth":
    print("Earth Crush|Mud Wave")
    strong = input("> ")
    while strong != "Earth Crush" and strong != "Mud Wave":
        print("Make sure to enter the name of the attack correctly, your options are below.")
        print("Earth Crush|Mud Wave")
        strong = input("> ")
elif element == "Air":
    print("Suffocation|Tornado")
    strong = input("> ")
    while strong != "Suffocation" and strong != "Tornado":
        print("Make sure to enter the name of the attack correctly, your options are below.")
        print("Suffocation|Tornado")
        strong = input("> ")
elif element == "Lightning":
    print("Lightning Strike|Electric Field")
    strong = input("> ")
    while strong != "Lightning Strike" and strong != "Electric Field":
        print("Make sure to enter the name of the attack correctly, your options are below.")
        print("Lightning Strike|Electric Field")
        strong = input("> ")

player.strong = strong
enemy_3 = Character("Morris", "Straw", "The Straw Man", "Air", 5, "Air Bullets", "Suffocation", None)
enemy_3.apply_buff()

print("You now have two moves you can use in your battles! The {light} attack and the {strong} attack".format(light=player.light, strong=player.strong))
print("There is only one more challenger left before you can reach max level. After defeating this enemy you will gain 4 levels and reach max level!")
print("Enter anything to continue and face your third opponent!")
input("> ")
print("Your third opponent is {} {}, also known as {}. His level is {}, so this battle is a little more difficult! He uses the {} element and uses the {} light attack and the {} Strong Attack.".format(enemy_3.first, enemy_3.last, enemy_3.nickname, enemy_3.level, enemy_3.element, enemy_3.light, enemy_3.strong))
print("Enter anything to continue.")
input("> ")

print("Enter the name of your attacks, {} and {}, to attack your opponent.".format(player.light, player.strong))

while True:
    enemy_3_attks = [enemy_3.light_attack, enemy_3.strong_attack]
    enemy_3_attk = random.choice(enemy_3_attks)
    attack_3 = input("> ")
    while attack_3 != player.light and attack_3 != player.strong:
        print("Make sure to enter the correct name of your attacks, {} and {}, to attack your opponent.".format(player.light, player.strong))
        attack_3 = input("> ")
    
    if attack_3 == player.light:
        enemy_3.health -= player.light_attack
        player.health -= enemy_3_attk
    elif attack_3 == player.strong:
        enemy_3.health -= player.strong_attack
        player.health -= enemy_3_attk
    
    if enemy_3.health <= enemy_3.max_health and enemy_3.health >= 0.000001:
        print("Keep attacking, your enemy is now at {} health.".format(enemy_3.health))
        print("{} hit you with an attack, your health is now at {}.".format(enemy_3.nickname, player.health))

    if enemy_3.health <= 0:
        player.apply_level(4)
        break

print("Congratulations on defeating the third enemy.")
print("You are officially level {}! Your max health is at {} and your max damage is at {}! Enter anything to continue.".format(player.level, player.max_health, player.max_damage))
input("> ")

print("Since you have reached the max level, you will now choose your ultimate attack. Your options are below.")

if player.element == "Fire":
    print("Solar Flare|Blast Breath")
    ult = input("> ")
    while ult != "Solar Flare" and ult != "Fire Impale":
        print("Make sure to enter the name of the attack correctly. Your options are below.")
        print("Solar Flare|Blast Breath")
        ult = input("> ")
elif player.element == "Water":
    print("Grand Tsunami|Sharknado")
    ult = input("> ")
    while ult != "Grand Tsunami" and ult != "Sharknado":
        print("Make sure to enter the name of the attack correctly. Your options are below.")
        print("Grand Tsunami|Sharknado")
        ult = input("> ")
elif player.element == "Earth":
    print("Molten Core|Earth Splitter")
    ult = input("> ")
    while ult != "Molten Core" and ult != "Earth Splitter":
        print("Make sure to enter the name of the attack correctly. Your options are below.")
        print("Molten Core|Earth Splitter")
        ult = input("> ")
elif player.element == "Air":
    print("Gale Slicer|Slicing Hurricane")
    strong = input("> ")
    while ult != "Gale Slicer" and ult != "Grand Tornado":
        print("Make sure to enter the name of the attack correctly. Your options are below.")
        print("Gale Slicer|Slicing Hurricane")
        ult = input("> ")
elif player.element == "Lightning":
    print("Liger Bomb|Lightning Dragon")
    ult = input("> ")
    while ult != "Liger Bomb" and ult != "Lightning Dragon":
        print("Make sure to enter the name of the attack correctly. Your options are below.")
        print("Liger Bomb|Lightning Dragon")
        ult = input("> ")

player.ultimate = ult
print("Now you are all prepared for the Elemental War. Enter anything to continue.")
input("> ")

print("In the Elemental War, the {} is at war with the {} Nation. In order to be successful in this war, you will need to defeat the 3 {} Generals and then the {} Lord!".format(player.nation, player.enemy_nation, player.enemy_nation, player.enemy_nation))
print("Enter anything to continue.")
input("> ")

general_1 = Character("Magnus", "Chorat", "The Ogor", player.enemy_nation, 5, None, None, None)
general_1.apply_buff()

print("You have now entered {} Nation territory. As you advance further into the territory, the first {} General spots you and stops you.".format(player.enemy_nation, player.enemy_nation))
print("You will now have to defeat the first {} General to get closer to the {} Lord! He is the weakest General so this battle shouldn't take long. Enter anything to continue.".format(player.enemy_nation, player.enemy_nation))
input("> ")

print("When you defeat the first {} General, you will regain any lost health in the battle!".format(player.enemy_nation))
print("Enter the name of your attacks, {}, {}, and {}, to attack the General.".format(player.light, player.strong, player.ultimate))

while True:
    general_attacks = [general_1.light_attack, general_1.strong_attack]
    general_attack = random.choice(general_attacks)
    attack_4 = input("> ")
    while attack_4 != player.light and attack_4 != player.strong and attack_4 != player.ultimate:
        print("Make sure to enter the name of your attacks, {}, {}, and {}, to attack your opponent.".format(player.light, player.strong, player.ultimate))
        attack_4 = input("> ")

    if attack_4 == player.light:
        general_1.health -= player.light_attack
        player.health -= general_attack
    elif attack_4 == player.strong:
        general_1.health -= player.strong_attack
        player.health -= general_attack
    elif attack_4 == player.ultimate:
        general_1.health -= player.ultimate_attack
        player.health -= general_attack

    if general_1.health <= general_1.max_health and general_1.health >= 0.00000001:
        print("Keep attacking, the Generals health is at {}".format(general_1.health))
        print("{} hit you with an attack, your health is now at {}".format(general_1.nickname, player.health))
    
    if general_1.health <= 0:
        player.apply_hp()
        break
    
    







