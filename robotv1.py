robot_art = r"""
      0: {head_name}
      Is available: {head_status}
      Attack: {head_attack}                              
      Defense: {head_defense}
      Energy consumption: {head_energy_consump}
              ^
              |                  |1: {weapon_name}
              |                  |Is available: {weapon_status}
     ____     |    ____          |Attack: {weapon_attack}
    |oooo|  ____  |oooo| ------> |Defense: {weapon_defense}
    |oooo| '    ' |oooo|         |Energy consumption: {weapon_energy_consump}
    |oooo|/\_||_/\|oooo|          
    `----' / __ \  `----'           |2: {left_arm_name}
   '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
   /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
  / \_/|_|| |/\| ||_|\_/ \          |Defense: {left_arm_defense}
 |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consump}
 <_>      |=\__/=|      <_> ------> |
 <_>      |------|      <_>         |3: {right_arm_name}
 | |   ___|======|___   | |         |Is available: {right_arm_status}
// \\ / |O|======|O| \  //\\        |Attack: {right_arm_attack}
|  |  | |O+------+O| |  |  |        |Defense: {right_arm_defense}
|\/|  \_+/        \+_/  |\/|        |Energy consumption: {right_arm_energy_consump}
\__/  _|||        |||_  \__/        
      | ||        || |          |4: {left_leg_name} 
     [==|]        [|==]         |Is available: {left_leg_status}
     [===]        [===]         |Attack: {left_leg_attack}
      >_<          >_<          |Defense: {left_leg_defense}
     || ||        || ||         |Energy consumption: {left_leg_energy_consump}
     || ||        || || ------> |
     || ||        || ||         |5: {right_leg_name}
   __|\_/|__    __|\_/|__       |Is available: {right_leg_status}
  /___n_n___\  /___n_n___\      |Attack: {right_leg_attack}
                                |Defense: {right_leg_defense}
                                |Energy consumption: {right_leg_energy_consump}
                                
"""

colors = {
    "Black": "\x1b[90m",
    "Blue": "\x1b[94m",
    "Cyan": "\x1b[96m",
    "Green": "\x1b[92m",
    "Magenta": "\x1b[95m",
    "Red": "\x1b[91m",
    "White": "\x1b[97m",
    "Yellow": "\x1b[93m"
}

class Robot:
    def __init__(self, name, color_code):
        self.name = name
        self.color_code = color_code
        self.energy = 100
        self.attack_count = 0
        self.defense_count = 0
        self.is_defending = False
        self.has_used_the_weapon = False
        self.special_weapons = {
                "Gaster Blaster": 25,
                "Flamethrower": 20
            }
        self.parts = [
            Part("Head", attack_level=5, defense_level=10, energy_consumption=5),
            Part("Weapon", attack_level=15, defense_level=0, energy_consumption=10), 
            Part("Left Arm", attack_level=3, defense_level=20, energy_consumption=10),
            Part("Right Arm", attack_level=6, defense_level=20, energy_consumption=10),
            Part("Left Leg", attack_level=4, defense_level=20, energy_consumption=15),
            Part("Right Leg", attack_level=8, defense_level=20, energy_consumption=15)
        ]

    
    def greet(self):
        print(f"Hello, my name is: {self.name}")

    def print_energy(self):
        print(f"{self.name} has {self.energy} percent energy left")

    def attack(self, enemy_robot, part_to_use, part_to_attack, is_the_enemy_defending):
        if is_the_enemy_defending == True:
            enemy_robot.parts[part_to_attack].defense_level -= (self.parts[part_to_use].attack_level / 2)
        else:
            enemy_robot.parts[part_to_attack].defense_level -= self.parts[part_to_use].attack_level
        self.energy -= self.parts[part_to_use].energy_consumption

    def attack_with_special_weapon(self, enemy_robot, special_weapon, part_to_attack):
        enemy_robot.parts[part_to_attack].defense_level -= special_weapon
        self.energy -= 50

    def is_on(self):
        return self.energy > 0
    
    def is_there_available_parts(self):
        for part in self.parts:
            if part.is_available():
                return True
        return False

    def print_status(self):
        str_robot = robot_art.format(**self.get_part_status())
        self.greet()
        self.print_energy()
        print(str_robot)
        print(self.color_code)

    def get_part_status(self):
        part_status = {}
        for part in self.parts:
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
        return part_status

class Part:
    def __init__(self, name, attack_level=0, defense_level=0, energy_consumption=0):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption

    def get_status_dict(self):
        formatted_name = self.name.replace(" ", "_").lower()
        return {
            "{}_name".format(formatted_name): self.name.upper(),
            "{}_status".format(formatted_name): self.is_available(),
            "{}_attack".format(formatted_name): self.attack_level,
            "{}_defense".format(formatted_name): self.defense_level,
            "{}_energy_consump".format(formatted_name): self.energy_consumption
        }
    
    def is_available(self):
        return not self.defense_level < 0
    

        
def build_robot():
    robot_name = input("Robot name: ")
    if robot_name == "":
        robot_name = "Vanguard"
    color_code = choose_color()
    robot = Robot(robot_name, color_code)
    robot.print_status()
    return robot

def choose_color():
    chosen_color = input("What robot color do you want? (Choose from Black, Blue, Cyan, Green, Magenta, Red, White and Yellow): ").capitalize()
    try:
        return colors[chosen_color]
    except KeyError:
        return colors["Cyan"]

def announce_winner(winner_robot, condition):
    print("Congratulations, you won")
    print(winner_robot.name)
    print(f"Because of enemy {condition}.")

def play():
    playing = True
    print("Welcome to the game")
    print("Remember that you can use the robot part attack 4 times and the energy shield 2 times.")
    print("Also the special weapon is for one use only.")
    print("Data for player 1")
    robot_one = build_robot()
    print("Data for player 2")
    robot_two = build_robot()
    round_ = 0

    while playing:
        if round_ % 2 == 0:
            current_robot = robot_one
            enemy_robot = robot_two
        else:
            current_robot = robot_two
            enemy_robot = robot_one

        current_robot.print_status()
        player_action = input("Do you want to use the special 'weapon', 'defend' with an energy shield or 'attack' with a part of the robot: ").lower()

        if player_action == "attack":
            if current_robot.attack_count == 4:
                playing = False
                announce_winner(enemy_robot, "max attacks reached")
                break

            print("What part should I use to attack?")
            try:
                part_to_use = input("Choose a number part: ")
                part_to_use = int(part_to_use)
            except IndexError:
                part_to_use = 4
            except ValueError:
                part_to_use = 3
            enemy_robot.print_status()
            print("Which part of the enemy should we attack?")
            try:
                part_to_attack = input("Choose a enemy part to attack: ")
                part_to_attack = int(part_to_attack)
            except IndexError:
                part_to_attack = 2
            except ValueError:
                part_to_attack = 3
            is_enemy_robot_defending = enemy_robot.is_defending

            current_robot.attack(enemy_robot, part_to_use, part_to_attack, is_enemy_robot_defending)
            if is_enemy_robot_defending == True:
                enemy_robot.is_defending = False

            current_robot.attack_count += 1
        elif player_action == "defend":
            if current_robot.defense_count == 2:
                playing = False
                announce_winner(enemy_robot, "max defense count reached")
                break
            print(f"{current_robot.name} is defending the next enemy attack with an energy shield!")
            current_robot.is_defending = True
            current_robot.defense_count += 1
        elif player_action == "weapon":
            if current_robot.has_used_the_weapon == True:
                playing = False
                announce_winner(enemy_robot, "special weapon used another time")
                break

            print(f"Gaster Blaster with a dagame of: {current_robot.special_weapons['Gaster Blaster']}")
            print(f"Flamethrower with a dagame of: {current_robot.special_weapons['Flamethrower']}")
            try:
                user_chosen_weapon = input("Choose your special weapon from the ones shown above!: ")
            except ValueError:
                user_chosen_weapon = "Gaster Blaster"
            
            enemy_robot.print_status()
            print("Which part of the enemy should we attack?")
            try:
                part_to_attack = input("Choose a enemy part to attack: ")
                part_to_attack = int(part_to_attack)
            except IndexError:
                part_to_attack = 2
            except ValueError:
                part_to_attack = 3
            
            try:
                current_robot.attack_with_special_weapon(enemy_robot, current_robot.special_weapons[user_chosen_weapon], part_to_attack)
            except KeyError:
                current_robot.attack_with_special_weapon(enemy_robot, current_robot.special_weapons["Gaster Blaster"], part_to_attack)
            
            current_robot.has_used_the_weapon = True
        else:
            print("Skipping round because of bad input...")
    
        round_ += 1
        
        if not enemy_robot.is_on() or enemy_robot.is_there_available_parts() == False:
            playing = False
            print("Congratulations, you won")
            print(current_robot.name)

play()



