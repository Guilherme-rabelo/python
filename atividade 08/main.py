n1 = (int(input('Me fale um número:')))
n2 = (int(input('Me fale outro número:')))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f'A soma é {s}, o produto é {m}, e a divisão é {d:.3f}', end=" " )
print(f'A divisão inteira é {di} e a potência é {e}.')

