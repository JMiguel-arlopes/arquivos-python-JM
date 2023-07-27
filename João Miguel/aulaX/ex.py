import random

def guessgame():
    aleatorio = random.randrange(10)
    chute = int(input("chute um número de 0 a 10: "))
    count = 1

    while not chute <= 10 and chute > 0:
        print('número inválido')
        chute = int(input("chute um número de 0 a 10: "))
    while aleatorio != chute:
        print("você errou, tente novamente")
        chute = int(input("chute um número de 0 a 10: "))
        count += 1
    print(f"parabéns, você acertou em {count} tentativas")
            
    