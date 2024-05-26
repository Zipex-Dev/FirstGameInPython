import random
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

user_wins = 0
ai_wins = 0

options = ["pedra", "papel", "tesoura"]

while True:
    user_input = input("Escreve Pedra/Papel/Tesoura ou 0 para sair/acabar: ").lower()
    limpar_tela()
    if user_input == "0":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # PEDRA=0, PAPEL=1, TESOURA=2
    ai_pick = options[random_number]
    print("AI ESCOLHEU", ai_pick + ".")

    if user_input == "pedra" and ai_pick == "tesoura":
        print("Ganhaste!")
        user_wins += 1

    elif user_input == "papel" and ai_pick == "pedra":
        print("Ganhaste!")
        user_wins += 1

    elif user_input == "tesoura" and ai_pick == "papel":
        print("Ganhaste!")
        user_wins += 1
   
    elif user_input == "pedra" and ai_pick == user_input:
        print("Empate!")

    elif user_input == "papel" and ai_pick == user_input:
        print("Empate!")

    elif user_input == "tesoura" and ai_pick == user_input:
        print("Empate!")

    else:
        print("Perdeste fraco!")
        ai_wins += 1

print("TU GANHASTE ", user_wins, "VEZES.")
print("O AI GANHOU ", ai_wins, "VEZES.")
print("BYE BYE!")