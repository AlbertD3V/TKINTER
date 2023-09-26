from calc import*

print('DIGITE 1 PARA SOMA')
print('DIGITE 2 PARA SUBTRAÇÃO')
print('DIGITE 3 PARA MULTIPLICAÇÃO')
print('DIGITE 4 PARA DIVISÃO')

menu = input('Qual operação você deseja realizar?')

     
if menu ==  '1':
    x = int(input('Informe o numero: '))
    y = int(input('Informe outro numero: '))
    print(soma(x,y))
elif menu == '2':
        x = int(input('Informe o numero: '))
        y = int(input('Informe outro numero: '))
        print(subtracao(x,y))
elif menu == '3':
    x = int(input('Informe o numero: '))
    y = int(input('Informe outro numero: '))
    print(multiplicar(x,y))
elif menu == '4':
    x = int(input('Informe o numero: '))
    y = int(input('Informe outro numero: '))
    print(divisao(x,y))
