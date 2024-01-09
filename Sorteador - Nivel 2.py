import random
import time

def primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sortear_numero_primo(minimo, maximo):
    numero_sorteado = random.randint(minimo, maximo)
    while not primo(numero_sorteado):
        numero_sorteado = random.randint(minimo, maximo)
    return numero_sorteado

minimo = 1
maximo = 100
numero_primo_sorteado = sortear_numero_primo(minimo, maximo)

print("BEM VINDO AO JOGO!")
print("VOCÊ TEM 100 VIDAS E 3 ROUNDS!")
print("VAMOS SORTEAR UM NÚMERO, SE PREPARE!")
print("DICA: Você é um número primo.")

vidas = 100
round = 1 #rounds
tempo_inicio = time.time() #tempo

while vidas >= 0 and round <= 3:
    pergunta = int(input("Qual seu chute? "))

    if numero_primo_sorteado > pergunta:
        chutes = numero_primo_sorteado - pergunta
    else:
        chutes = pergunta - numero_primo_sorteado

    vidas = vidas - chutes

    if pergunta == numero_primo_sorteado:
        print("Parabéns! Você venceu.")
        break
    else:
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - tempo_inicio
        if vidas <= 0 or round >= 3 or tempo_decorrido >= 10:
            print("GAME OVER!")
            break
        else:
            print("Você errou... Tente novamente no próximo round.")
            round += 1
            print(f'Você ainda tem {vidas} vidas!')