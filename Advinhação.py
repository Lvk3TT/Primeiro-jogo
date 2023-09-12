def Jogar_Adivinhação ():

    import random
    print("Bem vindo ao meu primeiro jogo em Python!")

    numero_secreto = random.randrange(0, 101 )
    total_de_tentativas = 20
    pontos = 1000

    print("qual nível de dificuldade ? ")
    print("(1)Fácil (2)Médio (3)Díficil")

    nivel = int(input("Define o nível: "))
    if (nivel==1):
        total_de_tentativas = 20
    elif (nivel==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
        Chute_str = input("digite o seu numero entre 1 e 100: ")
        print("voce digitou", Chute_str)
        Chute = int(Chute_str)

        if(Chute < 1 or Chute > 100):
            print("Voce deve digitar um valor entra 1 e 100")
            continue

        Acertou = Chute == numero_secreto
        Maior   = Chute > numero_secreto
        Menor = Chute < numero_secreto


        if (numero_secreto == Chute):
            print("Voce acertou e fez {} pontos!". format(pontos))
            print("Fim do jogo, Parabéns!!! ")
            break

        else:
            if (Chute > numero_secreto):
                print("Voce errou, seu chute foi maior que o número secreto")
            if (Chute < numero_secreto):
                print("Voce errou, seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - Chute)
            pontos = pontos - pontos_perdidos


        if (numero_secreto == Chute):
            print("Fim do jogo, Parabéns!!! ")
        else:
            print("Fim do Jogo, tente novamente!")
