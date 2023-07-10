nome = 'Anderson'

#Tres maneiras de formatar strings em python
print('%s' % nome)
print('{}'.format(nome))
print(f'{nome}')
exemplo = 'O {1} foi a {0}'.format('Anderson', 'Escola')
print(exemplo)
exemplo2 = '{nome1} {sobrenome}'
print(exemplo2.format(nome1 = 'Alex', sobrenome= 'Silva'))

pessoa = {
    'nome':'Anderson',
    'idade': 18,
    'email': 'eusouanderson@outlook.com'
}
s = 'Ola {nome}, vi que você tem {idade} anos, e seu email é {email}'

print(s.format(**pessoa))
nome = 'Anderson'
sobrenome = 'Rodrigues'
print(f'{nome.upper():10} {sobrenome:10}')
print(f'{nome:-^30}') # centro 
print(f'{nome:->30} {sobrenome:15}') # direita
print(f'{nome:<} {sobrenome:<}') # esquerda
print(f'{nome.upper()=!r:\n^15}')

#Conversão de bases 'Numeros'

f'{16:b}' # '1111'
f'{15:o}' # '17'
f'{15:d}' #'15'
f'{15:x}' #'x'
f'{15:X}' #'X'

