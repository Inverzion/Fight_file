import random
import time

def main():
  hero_life = 100
  enemy_life = 100
  potions = 3
  while hero_life >= 0 and enemy_life >= 0:
    if hero_life <= 0 or enemy_life <= 0:
      if hero_life < enemy_life:
        print("Hero Died")
        break
      else:
        print("Hero Won")
        break

    prompt = input("How would you like to act: (attack, defend, heal) ")

    if hero_life <= 0 or enemy_life <= 0:
      if hero_life < enemy_life:
        print("Hero Died")
        break
      else:
        print("Hero Won")
        break

    elif prompt == 'attack':
      hero_life, enemy_life = hero_attack(hero_life, enemy_life)

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

    if hero_life <= 0 or enemy_life <= 0:
      if hero_life < enemy_life:
        print("Hero Died")
        break
      else:
        print("Hero Won")
        break

def hero_attack(hero_life, enemy_life):
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

main()
