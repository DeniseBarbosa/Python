# Exemplo em que a condição é verdadeira
idade = 35
if idade >= 18: 
  print('Idade suficiente para CNH!')
print('Fim do programa')

############################################

# Verifica se uma pessoa está apta para se aposentar
idade = 20
tempo_contrib = 35
if idade >= 65 or tempo_contrib >= 35: 
    print('Habilitado para solicitar aposentadoria!')


# Verifica se uma pessoa não está apta a se aposentar
idade = 70
tempo_contrib = 20

if idade < 65 and tempo_contrib < 35: 
    print('Não habilitado para solicitar aposentadoria!')

####################################################

x = 3
y = 0
if x > 10:
    print(f'O valor de {x} > 10')
    y = x * 2
else:
    print(f'O valor de {x} <= 10')
    y = x ** 2
print(y)


# Exemplo em que a condição é verdadeira
idade = 35

if idade >= 18: 
    print('Idade suficiente para CNH!')
else:
    print('Idade não suficiente para CNH!')

# Exemplo em que a condição é falsa
idade = 15

if idade >= 18: 
    print('Idade suficiente para CNH!')
else:
    print('Idade não suficiente para CNH!')


############################################



idade = 60
tempo_contrib = 30
if idade >= 65:
    print('Habilitado para aposentadoria por idade!')
else:
    print('Não habilitado para solicitar aposentadoria por idade!')

if tempo_contrib >= 35: 
    print('Habilitado para aposentadoria por tempo de contribuição!')
else:
        print('Não habilitado para solicitar aposentadoria por contribuição!')


idade = 15

if idade < 12:
    faixa_etaria = 'Criança'
elif idade < 18:
    faixa_etaria = 'Adolescente'
elif idade < 60:
    faixa_etaria = 'Adulto'
else:
    faixa_etaria = 'Idoso'
print('Faixa Etária: ', faixa_etaria)