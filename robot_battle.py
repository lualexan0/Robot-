from IPython.display import clear_output
import random
colors = {
	"red": '\033[1;31m',
  "blue": '\033[1;34m',
  "yellow": '\033[1;33m',
	"green": '\033[1;32m',
  "magenta": '\x1b[1;95m',
  "orange": '\x1b[38;5;202m',
  "gold": '\x1b[38;5;220m',
  "emerald": '\x1b[38;5;34m',
  "diamond": '\x1b[38;5;117m'
   }
text = '\033[37m'
error_list = ['0','1','2','3','4','5']
checkin = {
        '0':'Head is available: True',
        '1':'Weapon is available: True',
        '2':'Left arm is available: True',
        '3':'Right arm is available: True',
        '4':'Left leg is available: True',
        '5':'Right leg is available: True'
}
Game_rules = """
------------------------------------------------------------
Regras do jogo:

 - O robô com energia zero perde;
 - O robô que destruir o inimigo primeiro vence.
 - Robot St: vermelho, azul e amarelo. Nenhuma habilidade adicionada.
 - Robot Agro: magenta, verde, laranja. Perde 1 defesa
   e ganha ataque aleatório entre 5 e 10.
 - Robot Tank: ouro, diamante, esmeralda. Perde 1 ataque
   e ganha defesa aleatória entre 5 e 10.

------------------------------------------------------------
"""

robot_art_agro = r"""|_____________________________________________________________________________|
|                                   |0: {head_name}
|                                   |Head is available: {head_status} , Attack: {head_attack}
|                /\                 |Defense: {head_defense} , Energy consumption: {head_energy_consump}
|               /||\                |
|        ______/ '' \______         |-----------------------------------------|
|       / O O /|=||=|\ O O \        |1: {weapon_name}
|       `----' \_==_/ '----´        |Weapon is available: {weapon_status} , Attack: {weapon_attack}
|      '/ [|=|+------+|=|] \'       |Defense: {weapon_defense} , Energy consumption: {weapon_energy_consump}
|      /  [|=|| |/\| ||=|]  \       |
|     / \_/|_|| |/\| ||_|\_/ \      |-----------------------------------------|
|     |\/    \\=AGRO=//     \/|     |2: {left_arm_name}
|    .||.     |\____/|      .||.    |Left arm is available: {left_arm_status} , Attack: {left_arm_attack}
|    .||.     |-\--/-|      .||.    |Defense: {left_arm_defense} , Energy consumption: {left_arm_energy_consump}
|    .||.   __|=-\/-=|__    .||.    |
|    //\\  / |O|=--=|O| \   //\\    |-----------------------------------------|
|   <|  |  | |O=----=O| |   |  |>   |3: {right_arm_name}
|   <|\/|  \_/        \_/   |\/|>   |Right arm is available: {right_arm_status} , Attack: {right_arm_attack}
|    \__/  _||        ||_   \__/    |Defense: {right_arm_defense} , Energy consumption: {right_arm_energy_consump}
|     \/  | ||        || |   \/     |
|         [=|]        [|=]          |-----------------------------------------|
|         [==]        [==]          |4: {left_leg_name}
|         >_<          >_<          |Left leg is available: {left_leg_status} , Attack: {left_leg_attack}
|        <| |>        <| |>         |Defense: {left_leg_defense} , Energy consumption: {left_leg_energy_consump}
|        <| |>        <| |>         |
|        <| |>        <| |>         |-----------------------------------------|
|       _|\_/|_      _|\_/|_        |5: {right_leg_name}
|      /__n_n__\    /__n_n__\       |Right leg is available: {right_leg_status} , Attack: {right_leg_attack}
|                                   |Defense: {right_leg_defense} , Energy consumption: {right_leg_energy_consump}
|                                   |
|___________________________________|_________________________________________|"""

robot_art_starter = r"""|_____________________________________________________________________________|
|                                   |0: {head_name}
|                                   |Head is available: {head_status} , Attack: {head_attack}
|                                   |Defense: {head_defense} , Energy consumption: {head_energy_consump}
|        ____  ______  ____         |
|       |OOOO||=----=||OOOO|        |-----------------------------------------|
|       |OOOO||(o  o)||OOOO|        |1: {weapon_name}
|       `----' \_==_/ '----´        |Weapon is available: {weapon_status} , Attack: {weapon_attack}
|      '/  |-|/--""--\|-|  \'       |Defense: {weapon_defense} , Energy consumption: {weapon_energy_consump}
|      /  [|-||  /\  ||-|]  \       |
|     / \_/|_|| |()| ||_|\_/ \      |-----------------------------------------|
|    |_\/    \\  \/  //    \/_|     |2: {left_arm_name}
|    |[|      | (ST) |      |]|     |Left arm is available: {left_arm_status} , Attack: {left_arm_attack}
|    |[|      |------|      |]|     |Defense: {left_arm_defense} , Energy consumption: {left_arm_energy_consump}
|    |[|   ___|======|___   |]|     |
|    /|\   [ |        | ]   /|\     |-----------------------------------------|
|    |\|   | |O+------+O|   |/|     |3: {right_arm_name}
|    |/|   \_/        \_/   |\|     |Right arm is available: {right_arm_status} , Attack: {right_arm_attack}
|    \_/   _||        ||_   \_/     |Defense: {right_arm_defense} , Energy consumption: {right_arm_energy_consump}
|         |||         |||           |
|         [|]         [|]           |-----------------------------------------|
|         [=]         [=]           |4: {left_leg_name}
|         >_<         >_<           |Left leg is available: {left_leg_status} , Attack: {left_leg_attack}
|         |/|         |\|           |Defense: {left_leg_defense} , Energy consumption: {left_leg_energy_consump}
|         |\|         |/|           |
|         |/|         |\|           |-----------------------------------------|
|       _|\_/|_     _|\_/|_         |5: {right_leg_name}
|      |__n_n__|   |__n_n__|        |Right leg is available: {right_leg_status} , Attack: {right_leg_attack}
|                                   |Defense: {right_leg_defense} , Energy consumption: {right_leg_energy_consump}
|                                   |
|___________________________________|_________________________________________|"""

robot_art_tank = r"""|_____________________________________________________________________________|
|                                   |0: {head_name}
|                                   |Head is available: {head_status} , Attack: {head_attack}
|             .______.              |Defense: {head_defense} , Energy consumption: {head_energy_consump}
|             |______|              |
|              |====|               |-----------------------------------------|
|        ______|____|______         |1: {weapon_name}
|       / O O          O O \        |Weapon is available: {weapon_status} , Attack: {weapon_attack}
|       `----'++++++++ '----´       |Defense: {weapon_defense} , Energy consumption: {weapon_energy_consump}
|      |=-=-=-=-=-=-=-=-=-=-=|      |
|      |/ [|=|=|=|=|=|=|=|] \|      |-----------------------------------------|
|      |\_/|_____________ \_/|      |2: {left_arm_name}
|     / \/   \\=----=//    \/ \     |Left arm is available: {left_arm_status} , Attack: {left_arm_attack}
|    |==|] TA |------| TA  [|==|    |Defense: {left_arm_defense} , Energy consumption: {left_arm_energy_consump}
|    |==|| NK |++++++| NK  ||==|    |
|    |__|]____|______|_____[|__|    |-----------------------------------------|
|    |OO||-=-=-=|===|=-=-=-||OO|    |3: {right_arm_name}
|    |__|]______/’’’\______||__|    |Right arm is available: {right_arm_status} , Attack: {right_arm_attack}
|      /        ]___[        \      |Defense: {right_arm_defense} , Energy consumption: {right_arm_energy_consump}
|     |  [[]]]  |===|  [[[]]  |     |
|     |         |   |         |     |-----------------------------------------|
|      \_______/     \_______/      |4: {left_leg_name}
|      |  :::  |     |  :::  |      |Left leg is available: {left_leg_status} , Attack: {left_leg_attack}
|      |_______|     |_______|      |Defense: {left_leg_defense} , Energy consumption: {left_leg_energy_consump}
|      |/\/\/\/|     |\/\/\/\|      |
|     _|/\/\/\/|     |\/\/\/\|_     |-----------------------------------------|
|    |O|=======|     |=======|O|    |5: {right_leg_name}
|    `-|=======|     |=======|-´    |Right leg is available: {right_leg_status} , Attack: {right_leg_attack}
|      `OOOOOOO´     `OOOOOOO´      |Defense: {right_leg_defense} , Energy consumption: {right_leg_energy_consump}
|                                   |
|___________________________________|_________________________________________|"""

class Part:

    def __init__(self, name: str, attack_level=0, defense_level=0, energy_consumption=0,):
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
            "{}_energy_consump".format(formatted_name): self.energy_consumption,
}

    def reduce_edefense(self, attack_level):
        self.defense_level -= attack_level
        if self.defense_level <= 0:
            self.defense_level = 0

    def is_available(self):
        return self.defense_level > 0

class Robot:
    def __init__(self, name, color_code):
        self.name = name
        self.color_code = color_code
        self.energy = 100
        self.parts = [
            Part("Head", attack_level=4, defense_level=10, energy_consumption=5),
            Part("Weapon", attack_level=15, defense_level=5, energy_consumption=20),
            Part("Left Arm", attack_level=5, defense_level=20, energy_consumption=10),
            Part("Right Arm", attack_level=5, defense_level=20, energy_consumption=10),
            Part("Left Leg", attack_level=7, defense_level=20, energy_consumption=15),
            Part("Right Leg", attack_level=7, defense_level=20, energy_consumption=15)
        ]

    def print_status(self, color_code):
        if color_code in ['\033[1;31m', '\033[1;34m','\033[1;33m']:
            robot_art = robot_art_starter.format(**self.get_part_status())
        elif color_code in ['\033[1;32m','\x1b[1;95m','\x1b[38;5;202m']:
            robot_art = robot_art_agro.format(**self.get_part_status())
        else:
            robot_art = robot_art_tank.format(**self.get_part_status())
        self.greet()
        self.print_energy()
        print(robot_art)
        print(text,'\n-------------------------------------------------------------------------------')


    def greet(self):
        print(self.color_code,f'''_____________________________________________________________________________
                       Hi {self.name}, destroy the enemy robot''')

    def name(self):
        return self.name

    def color(self):
        print(self.color_code)

    def color_check(self):
        return self.color_code

    def energy_bar(self):
        total_bars = 20
        bars = self.energy * total_bars // 100
        spaces = total_bars - bars
        for _ in range(bars):
            print("█", end="")
        for _ in range(spaces):
            print(" ", end="")

    def print_energy(self):
        print(f"|                     Energy: {self.energy}%", end=" ")
        print("[\033[37m", end="")
        self.energy_bar()
        print(f"{self.color_code}]                     |")

    def is_on(self):
        return self.energy > 0

    def is_there_available_part(self):
        lives_part = 0
        for part in self.parts:
            if part.is_available():
              part = True
            else:
              lives_part += 1
        if lives_part == 6:
          return False

    def attack(self, enemy_robot, part_to_use, part_to_attack):
        enemy_robot.parts[part_to_attack].reduce_edefense(self.parts[part_to_use].attack_level)
        self.energy -= self.parts[part_to_use].energy_consumption

    def get_part_status(self):
      part_status = {}
      for part in self.parts:
        status_dict = part.get_status_dict()
        part_status.update(status_dict)
      return part_status

    def get_part_lives(self):
      robot_art = robot_art_starter.format(**self.get_part_status())
      return robot_art

    def bonus_part(self, color_code):
      for part in self.parts:
        if color_code in ['\033[1;31m', '\033[1;34m','\033[1;33m',]:
          part.attack_level += 1
          part.defense_level +=2

        elif color_code in ['\033[1;32m','\x1b[1;95m','\x1b[38;5;202m']:
          part.attack_level += random.randint(5, 10)
          part.defense_level -= 1
        else:
          part.attack_level -= 1
          part.defense_level += random.randint(5, 10)


    def energy_recovery(self):
         self.color()
         if self.energy < 100:
            self.energy += 15
            if self.energy > 100:
                self.energy = 100
            print("Energy recovered! Current energy:", self.energy)
            print(text,'\n-------------------------------------------------------------------------------')
         else:
            print("Energy is already at maximum.")
            print(text,'\n-------------------------------------------------------------------------------')

    def self_destruction(self):
        clear_output(wait=True)
        print("Are you sure you want to self-destruct? This action cannot be undone.")
        destruction = True
        while destruction:
            choice = input("Type 'yes' to self-destruct or 'no' to continue: ")
            if choice.lower() == "yes":
                destruction = False
                self.energy = 0
                print("Self-destruction initiated. Robot has been destroyed.")
                return True
            elif choice.lower() == 'no':
                destruction = False
                print("Self-destruction cancelled. Continuing the game.")
            else:
                print("repeat, invalid word\n")

def build_robot():
    robot_name = input("Your name: ").title()
    clear_output(wait= True)
    color_code = choose_color()
    robot = Robot(robot_name, color_code)
    robot.bonus_part(color_code)
    clear_output(wait= True)
    robot.print_status(color_code)
    return robot

def choose_color():
    erro_cor = True
    while erro_cor:
        available_colors = colors
        print("Available colors:")
        for key, value in available_colors.items():
            print(value, key)
        print(text)
        chosen_color = input("Choose a color: ").lower()
        if chosen_color in available_colors:
            color_code = available_colors[chosen_color]
            erro_cor = False
        else:
            clear_output(wait= True)
            print('Repeat the color, you typed a nonexistent color')
    return color_code

def play():
    print(text)
    playing = True
    print("Datas for Raging Demon:")
    robot_one = build_robot()
    print("\nDatas for Pure Light:")
    robot_two = build_robot()

    current_robot = robot_one
    enemy_robot = robot_two
    rount = 0

    while playing:
        if rount % 2 == 0:
            current_robot = robot_one
            enemy_robot = robot_two
            robot_one.color()
            print(f" That's {robot_one.name}'s turn")
        else:
            current_robot = robot_two
            enemy_robot = robot_one
            robot_two.color()
            print(f" That's {robot_two.name}'s turn")
        action_error = True
        while action_error:
            action_choice = (input("Choose an action:\n1: Attack;\n2: Energy Recoover;\n3: Selfdestruction.\n"))
            if action_choice == '1':
                action_error = False
                part_attack_error = True
                current_robot.print_status(current_robot.color_check())
                while part_attack_error:
                  part_to_use = input("What part should I use to attack?:\nChoose a number part: ")
                  if part_to_use in error_list and checkin[part_to_use] in current_robot.get_part_lives():
                    part_to_use = int(part_to_use)
                    part_attack_error = False
                  elif not part_to_use in error_list:
                    print("That part doesn't exist.\n")
                  else:
                    print('Please try again, that part has already been destroyed.\n')
                enemy_robot.print_status(enemy_robot.color_check())
                part_attack_error = True
                while part_attack_error:
                  part_to_attack = input("Which part of the enemy should we attack?:\nChoose a number part: ")
                  if part_to_attack in error_list and checkin[part_to_attack] in enemy_robot.get_part_lives():
                    part_to_attack = int(part_to_attack)
                    clear_output(wait=True)
                    part_attack_error = False
                  elif not part_to_attack in error_list:
                    print("That part doesn't exist.\n")
                  else:
                    print('Please try again, that part has already been destroyed.\n')
                current_robot.attack(enemy_robot, part_to_use, part_to_attack)
            elif action_choice == '2':
                action_error = False
                clear_output(wait=True)
                current_robot.energy_recovery()
            elif action_choice == '3':
                action_error = False
                if current_robot.self_destruction():
                   enemy_robot.color()
                   playing = False
                   clear_output(wait=True)
                   enemy_robot.color()
                   print(f"{current_robot.name} has self-destructed.{enemy_robot.name} is the winner!")
                   break
            else:
              clear_output(wait=True)
              print("Invalid choice. Try again.")
        rount += 1

        if not enemy_robot.is_on() or enemy_robot.is_there_available_part() == False:
            playing = False
            current_robot.color()
            print(f"Congratulations, {current_robot.name}. You destroyed the enemy robot, you are the ultimate winner.")
        else:
            continue

play()