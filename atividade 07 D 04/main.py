item = input('Digite algo:')
print ('O tipo primitivo dese valor é', type(item))
print ('Só tem espaços ?', (item.isspace()))
print ('É um número ?', (item.isnumeric()))
print ('É alfabético ?', (item.isalpha ()))
print ('É alfanúmerico ?', (item.isalnum ()))
print ('Está em maiúscula ?', (item.isupper ()))
print ('Está em minuscula ?', (item.islower ()))
print ('Está capitalizada ?', (item.istitle ()))
