precopao = 0.80
Precobroa = 2.50

qpaesdia  = int(input('Digite a quantidade de Pâes no dia: '))
qbroadia  = int(input('Digite a quantidade de Broas no dia: '))

calculo = (precopao*qbroadia)+(Precobroa*qbroadia)
poupanca = calculo*0.1

print(f'A sua venda no dia foi R$ {calculo} \n')
print(f'Foi armazenado na poupança R$ {poupanca}')