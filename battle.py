import random

class player:
    def __init__(self, player_health, player_run, player_damage):
        # Instance variable
        self.player_health = player_health
        self.player_run = player_run
        self.player_damage = player_damage
    def punch(self, enemy_block):
        print("You punched!")
        if (enemy_block):
            print("Your attack got blocked!")
            self.player_damage = 0
        else:
            self.player_damage = random.choice([2,3])
            print("Attack damage is " + str(self.player_damage))
    def kick(self):
        self.player_damage = random.choice([1,2])
    def run_away(self):
        self.player_run = True
guy = player(10, False, 0)
def battle(enemy, enemy_health):
    player_health = 10
    enemy_block = False
    enemy_attack_choice = []
    player_run = False
    print("Battle Begin!")
    print(guy.player_damage)
    while enemy_health > 0 and player_health > 0:
        print("Your health: " + str(player_health))
        print(enemy+"'s health: "+str(enemy_health))
        player_action = input("Choose an action: \n Punch \n Kick \n Run Away \n")
        player_action = player_action.lower()
        if player_action == "run away":
            print("wow, really? ok fine, you ran away. good job.")
            guy.run_away
            break
        elif player_action == "punch":
            guy.punch(enemy_block)
            enemy_health = enemy_health - guy.player_damage
        elif player_action == "kick":
            guy.kick()
            enemy_health = enemy_health - guy.player_damage
        print("Enemy Turn!")
        enemy_block = False
        enemy_attack_choice = random.choice([0,1])
        if enemy_attack_choice == 0:
            print("The "+enemy+" prepares to block!")
            enemy_block = True
        else:
            print("The "+enemy+" attacks for 2 damage!")
            player_health=player_health-2
    print("Battle end!")
    if player_health <= 0 and enemy_health <= 0:
        print("Wow, you somehow managed to die at the same time as the "+enemy+ ". Neat. Program's over though, so bye!")
    elif enemy_health <= 0 and player_health > 0:
        print("Great, you lived! Now leave, the program's over.")
    elif player_health <= 0 and enemy_health > 0:
        print("You died! Too bad. Program's over too so you'll have to restart that.")
    else:
        print("How did you get here????")
    
battle("goblin", 5)