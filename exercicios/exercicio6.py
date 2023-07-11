"""
Exercício 6

Nome: Catapulta
Objetivo: Receber o número de baterias e duração da bateria e calcular a quantidade de pedras que a catapulta irá soltar.
Dificuldade: Principiante

1 - Uma catapulta lançou 300 pedras em 5 baterias de 15 minutos, cada.
2 - Quantas pedras ela lançaria em 8 baterias de 7 minutos, cada?
3 - Crie um programa que receba os valores base para que a aplicação 
funcione de forma que, se alterarmos o número de bateriais e a
 duração de cada bateria, o programa funcione sem precisar de mais modificações.
"""

def calcular_pedras(num_baterias, duracao_bateria):
    total_pedras = num_baterias * duracao_bateria * 4
    return total_pedras

# Exemplo de uso
num_baterias = int(input("Digite o número de baterias: "))
duracao_bateria = int(input("Digite a duração de cada bateria (em minutos): "))

total_pedras = calcular_pedras(num_baterias, duracao_bateria)
print("A catapulta lançaria um total de", total_pedras, "pedras.")
