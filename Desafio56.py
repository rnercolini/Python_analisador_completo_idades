# Retorna com a média das idades, o nome do homem mais velho e quantas mulheres há menores de 20 anos.
media = 0
idadeh = 0
nomeh = ''
idadem = 0
for c in range(1, 5):
    print('\033[31m|---------- {}ª pessoa ----------|\033[m'.format(c))
    nome = str(input('Digite o nome da pessoa: ')).strip().upper()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [ M / F ]: ')).strip()
# Calcula a média das idades
    media += idade
# Retorna com o nome do homem mais velho
    if c == 1 and sexo in 'Mm':
        idadeh = idade
        nomeh = nome
    if idadeh < idade and sexo in 'Mm':
        idadeh = idade
        nomeh = nome
# Calcula quantas mulheres tem menos que 20 anos
    if idade < 20 and sexo in 'Ff':
        idadem = idadem + 1
print('A média das idades digitadas é de {} anos.'.format(media/4))
print('O homem mais velho é o {} e a sua idade é de {} anos.'.format(nomeh, idadeh))
print('No total da listagem há {} mulher(es) com menos de 20 anos.'.format(idadem))
