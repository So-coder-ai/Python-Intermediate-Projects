import random
#print("\u25CF  \u250C  \u2500  \u2510  \u2502  \u2514  \u2518")
# ●  ┌  ─  ┐  │  └  ┘

#"┌─────────┐"
#"│         │"
#"│    ●    │"
#"│         │"
#"└─────────┘"

dice_art = {
    1 :("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘") ,
    2 :("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘") , 
    3 :("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘") ,  
    4 :("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘") , 
    5 :("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘") , 
    6 :("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘") , 
}
dice = []
num_of_dices = int(input("Enter the number of dices : "))
total = 0 
for die in range(num_of_dices):
    dice.append(random.randint(1,6))

for die in range( num_of_dices):
    total += die


for die in range(num_of_dices):
   for line in dice_art.get(dice[die]):
     print(line)

#for line in range(5):
  #  for die in dice:
   #     print(dice_art.get(die)[line], end="")
  #  print()


print(f"total is :{total}")