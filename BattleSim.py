# Video Game Battle Simulator

# This program simulates a battle scenario in a video game. It prompts the player to enter their name, character class,
# enemy name, and enemy type. Then, it simulates a battle between the player and the enemy, displaying the health points
# of each after each attack. Finally, it determines the winner based on the remaining health points.

# Input: Player name, character class, enemy name, enemy type.
# Output: Battle simulation results and winner.

# Valid character classes and enemy types
VALID_CLASSES = ["warrior", "mage", "rogue", "warlock", "druid"]
VALID_ENEMY_TYPES = ["humanoid", "monster", "boss"]

# Function to check if a class is valid
def is_valid_class(character_class):
    return character_class.lower() in VALID_CLASSES

# Function to check if an enemy type is valid
def is_valid_enemy_type(enemy_type):
    return enemy_type.lower() in VALID_ENEMY_TYPES

# Class representing a character
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target):
        print(f"{self.name} attacks {target.name}")
        # Simulate attack and reduce target's health
        target.health -= 10
        print(f"{target.name} health: {target.health}")

# Main function
def main():
    # Prompt the player to enter their information
    player_name = input("Enter your name: ")
    character_class = input("Choose your character class (Warrior, Mage, Rogue, Warlock, Druid): ").lower()
    while not is_valid_class(character_class):
        print("Invalid character class! Please choose from: Warrior, Mage, Rogue, Warlock, Druid")
        character_class = input("Choose your character class: ").lower()
    
    enemy_name = input("Enter enemy name: ")
    enemy_type = input("Choose enemy type (Humanoid, Monster, Boss): ").lower()
    while not is_valid_enemy_type(enemy_type):
        print("Invalid enemy type! Please choose from: Humanoid, Monster, Boss")
        enemy_type = input("Choose enemy type: ").lower()

    # Create player and enemy characters
    player = Character(player_name, 100)
    enemy = Character(enemy_name, 100)

    # Perform battle simulation
    print("Let the battle begin!")
    while player.health > 0 and enemy.health > 0:
        # Player attacks enemy
        player.attack(enemy)
        if enemy.health <= 0:
            print(f"{player.name} wins!")
            break

        # Enemy attacks player
        enemy.attack(player)
        if player.health <= 0:
            print(f"{enemy.name} wins!")
            break

# Call the main function to start the program
if __name__ == "__main__":
    main()
