
/*Exercício 1

Nome: Operações Matemáticas
Objetivo: Praticar declaração de variáveis, operações matemáticas e exibição de informações no console.
Dificuldade: Principiante

1 - Declare duas variáveis numéricas 'a' e 'b' e atribua os valores 7 e 12, respectivamente;
2 - Declare uma variável chamada 'resultado' e armazene o resultado da soma entre as duas variáveis declaradas anteriormente;
3 - Exiba o resultado da soma no console;
4 - Agora declare novas linhas de exibição no console e exiba o resultado da subtração, multiplicação, divisão, exponenciação e resto da divisão inteira.
*/
using System;

class Program {
    static void Main(string[] args)
    {
        int a = 7;
        int b = 12;

        

        int resultado = a + b;

        Console.WriteLine("Resultado da soma: " + resultado);
        Console.WriteLine("Resultado da subtração: " + (a - b));
        Console.WriteLine("Resultado da multiplicação" + (b * a));
        Console.WriteLine("Resultado da divisão: " + (a / b));
        Console.WriteLine("Resultado da exponençação: " + (a ** b));
        
    }
}