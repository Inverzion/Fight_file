import random

def main():
  hero_life = 100
  enemy_life = 100
  while hero_life >= 0 and enemy_life >= 0:
    prompt = input("How would you like to act: (attack, defend, heal)")
    if prompt == 'attack':
      hero_life, enemy_life = attack(hero_life, enemy_life)
      
    elif prompt == "defend":
      hero_life, enemy_life = defense(hero_life, enemy_life)

    elif prompt == "heal":
      hero_life, enemy_life = defense(hero_life, enemy_life)
      
    else:
      print("Please input a valid response")

    if hero_life <= 0 or enemy_life <= 0:
      if hero_life < enemy_life:
        print("Hero Died")
        break
      else:
        print("Hero Won")
        break

def attack(enemy_life, hero_life):
  enemy_attack = random.randint(0,100)
  hero_attack = random.randint(0, 100)
  hero_life -= enemy_attack
  enemy_life -= hero_attack
  print("Hero Attack: ", hero_attack)
  print("Enemy Attack:", enemy_attack)
  print("Hero Health: ", hero_life)
  print("Enemy Health: ", enemy_life)
  return (hero_life, enemy_life)

def defense(hero_life, enemy_life):
  enemy_attack = random.randint(0,100)
  hero_defend = random.randint(0, enemy_attack)
  hero_life -= (enemy_attack - hero_defend)
  print("Enemy Attack: ", enemy_attack)
  print("Hero Defend: ", hero_defend) 
  print("Hero Health: ", hero_life)
  print("Enemy Health: ", enemy_life)
  return (hero_life, enemy_life)

def heal(hero_life, enemy_life):
  enemy_attack = random.randint(0,100)
  hero_life -= enemy_attack
  hero_heal = random.randint(0, 100)
  hero_life += hero_heal
  print("Enemy Attack: ", enemy_attack)
  print("Hero Heal: ", hero_heal)
  print("Hero Health: ", hero_life)
  print("Enemy Health: ", enemy_life)
  return (hero_life, enemy_life)

main()
