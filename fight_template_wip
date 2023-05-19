import random
import time

def main():
  hero_live = True
  hero_life = 100
  enemy_life = 100
  enemy_name = "Juan Cena"
  potions = 3
  while hero_live == True:
    alive_check(hero_life, enemy_life, enemy_name, hero_live)

    prompt = input("How would you like to act: (attack, defend, heal) ")

    alive_check(hero_life, enemy_life, enemy_name, hero_live)

    if prompt == 'attack':
      hero_life, enemy_life = hero_attack_action(hero_life, enemy_life)

    elif prompt == "defend":
      hero_life, enemy_life = hero_defense(hero_life, enemy_life)

    elif prompt == "heal":
      if potions > 0:
        hero_life, enemy_life, potions = hero_heal(hero_life, enemy_life, potions)
      else:
        print("You are out of potions, god speed.")
        time.sleep(1)
        hero_life, enemy_life = hero_mistake(hero_life, enemy_life)

    else:
      print("Please input a valid response")
# Validation alive_check & life_comparison in If/Else format Only left to test out functions
#    if hero_life <= 0 or enemy_life <= 0:
#      if hero_life < enemy_life:
#        print("Hero lost to ", enemy_name, ", better luck next time!")
#        break
#      else:
#        print("Hero defeated", enemy_name, ", congratulations")
#        break

def hero_attack_action(hero_life, enemy_life):
  hero_attack = random.randint(0, 100)  
  enemy_attack = random.randint(0,100)
  hero_life -= enemy_attack
  enemy_life -= hero_attack
  print("Hero Attack: ", hero_attack)
  print("Enemy Attack:", enemy_attack)
  print("Hero Health: ", hero_life)
  print("Enemy Health: ", enemy_life)
  return (hero_life, enemy_life)

def hero_defense(hero_life, enemy_life):
  enemy_attack = random.randint(0,100)
  hero_defend = random.randint(0, enemy_attack)
  hero_life -= (enemy_attack - hero_defend)
  print("Enemy Attack: ", enemy_attack)
  print("Hero Defend: ", hero_defend) 
  print("Hero Health: ", hero_life)
  print("Enemy Health: ", enemy_life)
  return (hero_life, enemy_life)

def hero_heal(hero_life, enemy_life, potions):
  enemy_attack = random.randint(0,100)
  hero_life -= enemy_attack
  hero_heal = random.randint(0, 100)
  hero_life += hero_heal
  potions -= 1
  print("Enemy Attack: ", enemy_attack)
  print("Hero Heal: ", hero_heal)
  print("Hero Health: ", hero_life)
  print("Enemy Health: ", enemy_life)
  print("Used 1 potion, ", potions, "potions left. Use these wisely!")
  return (hero_life, enemy_life, potions)

def hero_mistake(hero_life, enemy_life):
  enemy_attack = random.randint(0,100)
  hero_life -= enemy_attack
  print("Enemy Attack:", enemy_attack)
  print("Hero Health: ", hero_life)
  print("Enemy Health: ", enemy_life)
  return (hero_life, enemy_life)

def alive_check(hero_life, enemy_life, enemy_name, hero_live):
    if hero_life <= 0 or enemy_life <= 0:
        hero_life, enemy_life = life_comparison(hero_life, enemy_life, enemy_name, hero_live)

def life_comparison(hero_life, enemy_life, enemy_name, hero_live):
  if hero_life > enemy_life:
    print("Hero Won against ", enemy_name,"!")
    return (hero_life, enemy_life, enemy_name, hero_live)
  else:
    hero_live == False
    print("Hero Lost to ", enemy_name)
    return (hero_life, enemy_life, enemy_name, hero_live)

main()
