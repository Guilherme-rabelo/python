print('Ola!, esse é um sistema criado por Guilherme Rabelo. Gostaria de saber mais sobre voçê...')
nome=input('Qual seu nome ? ')
print(f'então seu nome é {nome}, que nome bonito')

idade=int(input('E qual sua idade ? '))  
if idade < 18:
        print(f"então sua idade é de {idade} anos de idade ?, voçê é menor de idade!")
    
elif idade <=59: 
     
        print(f"então sua idade é de {idade} anos de idade ?, voçê é um adulto!")
    
else: 
    print  (f"então sua idade é de {idade} anos de idade ?, voçê é um idoso!")

altura=int(input('e por último, qual a sua altura ? '))
if altura <= 1.49:
       print(f'Aah então voçê tem {altura} de altura ? voçê é considerado(a) baixo(a)')
elif altura <=1.79:
       print(f'Aah então voçê tem {altura} de altura ? voçê é considerado(a) de altura normal')  
else:
       print(f'Aah então voçê tem {altura} de altura ? voçê é considerado(a) muito alto(a)')     

print(f'Deixa eu vê se entendi, voçê se chama {nome}, tem {idade} anos e de altura vc mede {altura}.')

