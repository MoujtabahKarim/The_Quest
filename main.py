import random

#Global Variables
player_Name = "Bob"
player_Health = 100
material_type = ["wooden", "silver", "golden", "diamond"]
weapon = str(material_type[0]) + " stick"
helmet = str(material_type[0]) + " bucket"
coins = 20
character_inventory = [weapon, helmet, coins]


def go_Sleep():
    clearScreen()
    pass

def go_Battle():
    clearScreen()
    print("\t T H E\t B A T T L E")
    getEnemy()
    print()
    print("1. > Attack")
    print("2. > Run Away ")


def getEnemy():
    enemies = ["Dogs", "Cats", "Trump", "Ghost", "Snake", "Fish"]


    enemy_Health = str(random.randrange(80,300)) + "%"
    enemy_Name = str(enemies[random.randrange(len(enemies))])
    print(enemy_Name, "\t\t", enemy_Health)
    print(player_Name, "\t\t", str(player_Health) + "%")
    print()

def go_Home():
    clearScreen()
    print("\tT H E\t Q U E S T")
    print("1. > Battle")
    print("2. > Store")
    print("3. > Sleep")
    print()

    c = input("Choice: ")

    if c == "1":
           go_Battle()
    elif c == "2" :
            go_Store()
    elif c == "3":
            go_Sleep()
    else:
        go_Home()


def go_Store():
    clearScreen()
    print("\tT H E\t S T O R E")


def displayCharacterInfo():
    clearScreen()
    print("\tCoins: " + str(coins))
    print("\tHelmet: " + helmet)
    print("\tWeapon: " + weapon)
    print()
    print("1. > Go Back")
    print()


#Function used to clear the screen
def clearScreen():
    for x in range(40):
        print()

def main():
    go_Home()


if __name__ == '__main__':
    main()