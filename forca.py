import random  # Importa o módulo random para selecionar uma palavra aleatoriamente

# Lista de palavras possíveis para o jogo
palavras = ["foice", "carro", "estratosfera", "efelante", "cabelo", "passaralho"]

# Seleciona aleatoriamente uma palavra da lista
palavra = random.choice(palavras)

# Define o limite de tentativas como o comprimento da palavra mais 5
limite_tentativas = len(palavra) + 5

# Variáveis para controlar o estado do jogo
acertou = False  # Indica se o jogador acertou a palavra
enforcou = False  # Indica se o jogador esgotou as tentativas

# Inicializa a lista de letras acertadas com "_" para cada letra da palavra
letras_acertadas = []
for letra in palavra:
    letras_acertadas.append("_")  # Adiciona "_" para cada letra da palavra

# Inicializa o contador de tentativas
contador = 1

# Inicia um loop que continua enquanto o jogador não acertou a palavra e não enforcou
while(not acertou and not enforcou):
    # Formata as letras acertadas, convertendo a primeira letra para maiúscula
    resultado_formatado = "".join(letras_acertadas).capitalize()
    
    # Exibe o progresso do jogo com a formatação correta
    print(resultado_formatado)  
    # Exibe o número de tentativas realizadas e o limite de tentativas
    print("Tentativas: ", contador, "/", limite_tentativas)
    
    # Solicita ao usuário que digite uma letra e converte para minúsculas
    chute = input("Digite a letra: ").lower()  
    print(chute)  # Exibe o chute do jogador
    contador += 1  # Incrementa o contador de tentativas

    # Inicializa um índice para percorrer as letras da palavra
    indice = 0
    # Percorre cada letra da palavra
    for letra in palavra:
        # Verifica se o chute do jogador corresponde à letra da palavra
        if chute == letra.lower():  # Garante que a comparação seja feita em minúsculo
            letras_acertadas[indice] = letra  # Atualiza a lista com a letra original
        indice += 1  # Incrementa o índice

    # Verifica se o número de tentativas atingiu o limite
    if contador == limite_tentativas:
         enforcou = True  # Define que o jogador enforcou

    # Verifica se todas as letras foram adivinhadas
    if letras_acertadas.count("_") == 0:
        acertou = True  # Define que o jogador acertou
        print("Parabéns, você encontrou a palavra secreta")  # Mensagem de vitória
        print(letras_acertadas)  # Exibe a lista de letras acertadas