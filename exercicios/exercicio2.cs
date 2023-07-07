﻿/*
Exercício 2

Nome: Formatar Números
Objetivo: Praticar formatação de valores numéricos.
Dificuldade: Principiante

1 - Declare duas variáveis numéricas 'total_conta' e 'valor_pago' e atribua os valores 82.57 e 100, respectivamente;
2 - Declare uma variávei chamada 'troco' e armazene o resultado da subtração entre as duas variáveis declaradas anteriormente;
3 - Exiba o resultado da subtração no console;
4 - Agora utilize o método 'format()' e exiba esse resultado no seguinte formato: 'R$ 17.43';
5 - Reaproveite a linha declarada anteriormente e exiba a seguinte string: "O total da conta foi de R$ 82.57, você pagou R$ 100.00 e o seu troco foi de R$ 17.43.";
6 - Aplique devidamente a formatação dos centavos para cada variável numérica, utilizando a regra: {:.2f}.

Observação: Desenvolva o programa de uma forma que, se alterarmos os valores das variáveis, ele altere automaticamente a exibição do texto na tela, atualizando os valores.
*/

using System;

class programa
{
    static void Main(string[] args)
    {
        double total_conta = 82.57;
        double valor_pago = 100;
        
        double troco = valor_pago - total_conta;

        Console.WriteLine("Troco: " + troco.ToString("C2"));
        Console.WriteLine("Troco formatado: " + troco.ToString("C"));
        Console.WriteLine("O total da conta foi de " + total_conta.ToString("C2") + ", você pagou " + valor_pago.ToString("C2") + " e o seu troco foi de " + troco.)

    }
}