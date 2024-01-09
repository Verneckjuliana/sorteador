import random

#fórmula
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

#seleção
def sortear_numero_primo(minimo, maximo):
    numero_sorteado = random.randint(minimo, maximo)
    while not primo(numero_sorteado):
        numero_sorteado = random.randint(minimo, maximo)
    return numero_sorteado
minimo = 1
maximo = 100
numero_primo_sorteado = sortear_numero_primo(minimo, maximo)


#inicio do jogo
print("BEM VINDO AO JOGO!")
print("VOCÊ TEM 100 VIDAS!")
print("VAMOS SORTEAR UM NÚMERO, SE PREPARE!")
print("DICA: Você é um número primo.")

vidas = 100
while vidas >= 0:
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
        if vidas <= 0:
            print("GAME OVER!")
            break
        else:
            print("Você errou... Tente novamente no próximo round.")
            print(f' Você ainda tem {vidas} vidas!')





