porcento = 105 % 5
print(porcento)

x = 10
y = 4
z = 4.5
print('x + y + z=', x + y + z)
print('x - 3 =', x - 3)
print('x * z =', x * z)
print('x * 2 =', x * 2)
print('x / (y + 2) =', x / (y + 2))
print('x % y =', x % y)
print('x // y =', x // y)
print('x ** z =', x ** z)


B = 15 # Base maior (B)
b = 10 # Base menor (b)
h = 8 # Altura (h)



# Calcula a área do Trapézio
area = (B + b) * h / 2
print('Área do Trapézio: ', area)


x = 5
y = 1
s = 'palavra'

print('x > y:', x > (y + 2))
print('x <= 4.564:', x <= (4.564 + 1))
print('s == palavra:', s != 'palavra')
print('(y * 0) == False:', (y * 0) == False)
print('s != abacaxi:', s != 'abacaxi')

x = 3
y = 'palavra'
print(x == y)
print(x != y)
#print(x > y)

a = 'casa'
b = 'predio'
c = 'elevador'
d = 'casamento'
print(a < b)
print(b < c)
print(b > c)
print(a > d)
print('abacaxi' >= 'abacaxi')

print(True and True and False)

idade = 35
possui_autorizacao = False
print(idade > 18 or possui_autorizacao)

print(True or False)
print((10 > 1) and True)
print(not (True or False))
print(not ('palavra' == 'palavra'))

s1 = 'Belo'
s2 = 'Horizonte'

# Concatenação (+)
print(s1 + s2)
print(s1 + ' ' + s2)
print(s1 + ' Monte')

# Repetição
print(s1 * 5)
print((s1 + ', ') * 4)

s1 = 'consolação'
s2 = 'sola'

print(s1 in s2)
print(s2 in s1)
print('solar' in s1)
print('solar' not in s2)