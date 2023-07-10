"""
Exercício 6

Nome: Catapulta
Objetivo: Receber o número de baterias e duração da bateria e calcular a quantidade de pedras que a catapulta irá soltar.
Dificuldade: Principiante

1 - Uma catapulta lançou 300 pedras em 5 baterias de 15 minutos, cada.
2 - Quantas pedras ela lançaria em 8 baterias de 7 minutos, cada?
3 - Crie um programa que receba os valores base para que a aplicação funcione de forma que, se alterarmos o número de bateriais e a duração de cada bateria, o programa funcione sem precisar de mais modificações.
"""

qtd_de_baterias = 5
lacamento = 300 
tempo = 15


def catapulta(qtd_de_baterias, lacamento, tempo):
    pedras_por_minuto = lacamento / (qtd_de_baterias * tempo)
    return pedras_por_minuto

print(catapulta(tempo=tempo, qtd_de_baterias=qtd_de_baterias, lacamento=lacamento))