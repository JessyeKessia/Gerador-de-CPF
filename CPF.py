import random

cpf = ''
for i in range(9):
    cpf += str(random.randint(0,9))

j = 10
soma = 0

for i in range(len(cpf)):
    soma += int(cpf[i]) * j
    j -=1

multiplicar = soma * 10
resto = multiplicar % 11

if resto > 9:
    numero = 0
else:
    numero = resto


f = 11
soma2 = 0

for i in range(len(cpf)):
    soma += int(cpf[i]) * f
    j -=1

multiplicar_segundo = soma2 * 10
resto_dois = multiplicar_segundo % 11

if resto_dois > 9:
    numero2 = 0
else:
    numero2 = resto_dois

cpf_gerado = f'{cpf}{numero}{numero2}'

print(f'{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:11]}')
