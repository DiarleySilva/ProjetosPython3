#!/usr/bin/env python3.10
while True:
    print('1 - Adição ')
    print('2 - Subtração ')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('Digite qualquer número para sair')

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        valor1 = float(input('Digite o primeiro número para somar: '))
        valor2 = float(input('Digite o segundo número para somar: '))
        resultado = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} é {resultado}.')
    elif opcao == 2:
        valor1 = float(input('Digite o primeiro número para subtrair: '))
        valor2 = float(input('Digite o segundo número para subtrair: '))
        resultado = valor1 - valor2
        print(f'A subtração entre {valor1} e {valor2} é {resultado}.')
    elif opcao == 3:
        valor1 = float(input('Digite o primeiro número para multiplicar: '))
        valor2 = float(input('Digite o segundo número para multiplicar: '))
        resultado = valor1 * valor2
        print(f'A multiplicação entre {valor1} e {valor2} é {resultado}.')
    elif opcao == 4:
        valor1 = float(input('Digite o primeiro número para dividir: '))
        valor2 = float(input('Digite o segundo número para dividir: '))
        resultado = valor1 / valor2
        print(f'A divisão entre {valor1} e {valor2} é {resultado}.')
    else:
        print('Encerrando programa...')
        break
    continue