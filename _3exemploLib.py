# Função que eleva um número a uma potência
def elevar_potencia(a, b):
    return a ** b

# Função que recebe um nome e retorna uma saudação personalizada
def saudar(nome):
    return f"Olá, {nome}, tudo bem?"

# Função que calcula a média de uma lista de números
def calcular_media(numeros):
    if len(numeros) == 0:
        return None  # Retorna None se a lista estiver vazia
    return sum(numeros) / len(numeros)