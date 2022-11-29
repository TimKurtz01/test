import random

min = 1
max = 20

play = True

while(play):
    player_name = input('Wie heißt du?')
    print(f"Willkommen bei Zahlenraten, {player_name}!")
    print(f"Ich denke mir eine Zahl zwischen {str(min)} und {str(max)} aus, und du musst sie erraten!")
    print("Viel Spaß :^)")

    randInt = random.randint(1, 20)
    tries = 0
    while True:
        guess = int(input(f"Rate eine Zahl zwischen {str(min)} und {str(max)}\n"))
        tries += 1

        if(guess == randInt):
            break

    print(f"Glückwunsch, du hast mit {str(tries)} Versuchen gewonnen.")
    again = input("Noch einmal spielen? (ja = y)\n")
    play = again == "y"

print("Okay, bis zum nächsten Mal")
