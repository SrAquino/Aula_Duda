# Algoritmo: Sequência de passos para resolver um problema.

# Variáveis e Tipos de Dados
# Em Python, você não precisa especificar o tipo de dado da variável. O Python determina o tipo automaticamente com base no valor que você atribui a ela.

idade = 25  # Inteiro
nome = "Ana"  # String
altura = 1.75  # Float
eh_maior = True  # Booleano

numeros = [1, 2, 3, 4, 5] # Listas
coordenadas = (10.0, 20.0) # Tuplas
aluno = {"nome": "Ana", 
         "idade": 25, 
         "curso": "Biomedicina"} # Dicionários

# Operações

x = 10 # Atribuição 
soma = 10 + 5 
produto = 4 * 2

# Operações com Strings:

nome_completo = "Ana" + " " + "Silva"  # Concatenação

# Conversão de Tipos

# Às vezes, é necessário converter entre tipos de dados. Isso pode ser feito usando funções de conversão como
# int(), float(), str(), etc.

altura_str = "1.75"
altura = float(altura_str)  # Converte string para float

texto = "abc" # Quando a conversão não faz sentido resultam em erros.
# numero = int(texto)  # Gera um ValueError

def confere_se_digito(entrada):
    if str(entrada).isdigit():
        return int(entrada)
    else:
        n = input("Entrada inválida, por favor, digite um número.")
        return confere_se_digito(n)

def contador(a):
    a = confere_se_digito(a)
    for i in range(a):
        print(i)

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

def imc():
    altura = float(input("Digite sua altura em metros: "))
    peso = float(input("Digite seu peso em kg: "))
    imc = peso / (altura ** 2)

    print("Seu IMC é: {imc} \n", )

    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc < 24.9:
        print("Peso normal")
    elif 25 <= imc < 29.9:
        print("Sobrepeso")
    else:
        print("Obesidade")

n = input("Até quanto você deseja contar?\n ")
contador(n)
imc()