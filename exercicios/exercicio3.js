/*
Exercício 3

Nome: Input de Informações
Objetivo: Receber dados do usuário, trabalhar com os valores e exibir para o usuário.
Dificuldade: Principiante

1 - Crie um programa que receba do usuário seu nome, idade e gênero;
2 - Exiba na tela seguinte mensagem: "Olá, {nome}, você possui {idade} anos de idade e é do gênero {genero}. Já pensou no que você fará no seu aniversário de {idade + 1} anos?".
*/
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Digite seu nome: ", (nome) => {

    rl.question("Digite sua idade: ", (idade) => {
    
        rl.question("Digite seu gênero (M/F): ", (genero) => {

            console.log(`Olá, ${nome}, você possui ${idade} anos de idade e é do gênero ${genero}. Já pensou no que você fará no seu aniversário de ${idade + 1} anos?`);
        });
    });

});