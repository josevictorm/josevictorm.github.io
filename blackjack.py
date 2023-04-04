import random
import os
from time import sleep

cartas = ["A", "J", "Q", "K", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
naipes = ["Paus", "Copas", "Ouros", "Espadas"]

player = []
casa = []

def iniciar():
    os.system("cls")
    print(" -------------------------------------- ")
    print(" | Bem vindo ao blackjack do bignejix | ")
    print(" -------------------------------------- ")

    sleep(1)

    for c in range(5,0,-1):
        os.system("cls")
        print(" ------------------------ ")
        print(" | O jogo começará em",c, "|")
        print(" ------------------------ ")
        sleep(0.5)
    
    os.system("cls")


def calculo(opcao):
    
    total = 0

    tem_a = False
    tem_l = False

    for c in range(len(opcao)):
        if (opcao[c][0] == "A"):
            tem_a = True
        
        if (opcao[c][0] in ["J", "K", "Q"]):
            tem_l = True
    
    for c in range(len(opcao)):
        if (opcao[c][0] == "A" and tem_a and tem_l):
            total += 11
        
        elif (opcao[c][0] == "A"):
            total += 1
        
        elif (opcao[c][0] in ["J", "K", "Q", "1"]):
            total += 10
        
        else:
            total += int(opcao[c][0])

    return total

tela_jogo_f = True

def tela_jogo():

    global tela_param, tela_jogo_f

    os.system("cls")

    if len(player) > len(casa):
        tela_param = len(player)
    
    else:
        tela_param = len(casa)

    tela_param *= 14

    tela_param += 15


    # Casa

    espaco = 0

    print("|","-" * tela_param,"|")

    if (tela_jogo_f):
        print(f"|  Casa  = ['{casa[0]}']", end="")

        espaco = len(casa[0]) + 13

        total = "??"

    else:
        print(f"|  Casa  = {casa}", end="")

        for c in range(len(casa)):
            espaco += len(casa[c]) + 2
        
        espaco += (c * 2) + 2 + 9

        total = calculo(casa)

        if (total < 10):
            total = "0" + str(total)

    print(f" = {total}", end="")

    print(" " * (tela_param - espaco - 5), "|")


    # Player

    espaco = 0

    print(f"| Player = {player}",end="")

    for c in range(len(player)):
        espaco += len(player[c]) + 2

    espaco += (c * 2) + 2 + 9

    total = calculo(player)

    if (total < 10):
        total = "0" + str(total)

    print(f" = {total}", end="")

    print(" " * (tela_param - espaco - 5), "|")
    
    print("|","-" * tela_param,"|")


def sortear_carta():

    cartas_s = random.choice(cartas)
    naipes_s = random.choice(naipes) 

    carta_f = cartas_s + " " + naipes_s

    if (carta_f in player) or (carta_f in casa):
        return sortear_carta()
    
    else:
        return carta_f


def primeiro_sorteio():
    for c in range(2):
        casa.append(sortear_carta())
    
    for c in range(2):
        player.append(sortear_carta())


def sair():
    for c in range(5,0,-1):
        os.system("cls")
        print(f"Muito obrigado por jogar, saindo em {c}")
        sleep(0.5)
    os.system("cls")
    quit()


def pos_jogo():
    print("|", "-" * (tela_param), "|")
    print("| Escolha uma opção abaixo:", " " * (tela_param - 26), "|")
    print("|", " " * (tela_param), "|")
    print("| [1] - Recomeçar", " " * (tela_param - 16), "|")
    print("| [9] - Sair do jogo", " " * (tela_param - 19), "|")
    print("|", "-" * (tela_param), "|")

    while True:
        opcao = int(input("Opção: "))

        if (opcao == 1):
            return True
        
        elif (opcao == 9):
            sair()
        
        else:
            print("Opção Invalida tente novamente")


def verificacao_final():
    if (calculo(player) > calculo(casa)):
        print("| Você ganhou! :)", " " * (tela_param - 16), "|")
                
        return pos_jogo()
    
    elif (calculo(casa) > calculo(player)):
        print("| Você perdeu! :(", " " * (tela_param - 16), "|")
            
        return pos_jogo()
    
    elif (calculo(casa) == calculo(player)):
        print("| Empate :|", " " * (tela_param - 10), "|")

        return pos_jogo()


def menu():

    print("| Escolha uma opção abaixo:", " " * (tela_param - 26), "|")
    print("|", " " * (tela_param), "|")
    print("| [1] - Comprar", " " * (tela_param - 14), "|")
    print("| [2] - Parar", " " * (tela_param - 12), "|")
    print("| [9] - Sair do jogo", " " * (tela_param - 19), "|")
    print("|", "-" * (tela_param), "|")

    while True:
        opcao = int(input("Opção: "))

        if (opcao == 1):
        
            player.append(sortear_carta())
            
            if (calculo(player) > 21):
                tela_jogo()
                print("| Você perdeu! :(", " " * (tela_param - 16), "|")
            
                return pos_jogo()
            
            break

        elif (opcao == 2):

            global tela_jogo_f

            tela_jogo_f = False

            tela_jogo()
            sleep(0.5)

            while True:
                if (calculo(casa) < 19):

                    if (calculo(casa) > calculo(player)):
                        return verificacao_final()

                    else:
                        casa.append(sortear_carta())
                    tela_jogo()
                
                elif (calculo(casa) > 21):
                    tela_jogo()
                    print("| Você ganhou! :)", " " * (tela_param - 16), "|")
                
                    return pos_jogo()
                
                else:
                    return verificacao_final()

                sleep(0.5)


        elif (opcao == 9):
            sair()

        else:
            print("Opção invalida tente novamente")


def main():
    global tela_jogo_f

    iniciar()
    primeiro_sorteio()
    tela_jogo_f = True

    while True:
        tela_jogo()
        if menu():
            global casa, player
            player = []
            casa = []
            main()

main()