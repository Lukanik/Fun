import random

print("\n\tCoin Toss\n*************************\n\n")
print("Enter choices (Head/Tail): ")
player_c = input("Your Choice: ")

choices = {'Head': ['head','Head','HEAD', 'H', 'h'], 'Tail': ['tail','TAIL','Tail', 't', 'T']}

n = random.choice(('Head', 'Tail'))
bot_c = choices[n]
print(f"Bot Choice: {n}")

if player_c in bot_c:
    print("\nYou Won")
else:
    print("\nYou Lost")