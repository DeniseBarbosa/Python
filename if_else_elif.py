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


n = 0
while n <= 15 and n == 0:
    print(n, 'Meu nome é Pit')
    n = n + 1
print('Fim do programa')

n = 15
soma = 0
contador = 0

while contador <= n:
    print('soma', soma)
    print('contador', contador)
    soma = soma + contador
    contador = contador + 1
    print('soma depois', soma)
    print('contador depois', contador)
    print()

print(f'A soma dos primeiros {n} inteiros é {soma}')



# exemplo com n = 15
n = 15
soma = 0

while n >= 0:
    soma = soma + n
    n = n - 1

print(f'A soma dos primeiros inteiros é {soma}')


# exemplo de palavra: araraquara
p = 'araraquara'
contador_A = 0
contador_R = 0

for letra in p:
    if letra == 'a':
        contador_A = contador_A + 1
    if letra == 'r':
        contador_R = contador_R + 1
print(f"A palavara {p} possuí {contador_A} letras 'a' e {contador_R} letras 'r'")