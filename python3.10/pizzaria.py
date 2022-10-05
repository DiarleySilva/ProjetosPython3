print('Olá, seja bem-vindo à pizzaria do Diarley Silva Santos (RU 4095617).\n')

print('------------------CARDÁPIO---------------------')
print('| Código |      Descrição       | Pizza Média - M | Pizza Grande - G |')
print('|   21   |     Napolitana       |      R$20,00    |       R$26,00    |')
print('|   22   |     Marguerita       |      R$20,00    |       R$26,00    |')
print('|   23   |     Calabresa        |      R$25,00    |       R$32,00    |')
print('|   24   |     Toscana          |      R$30,00    |       R$39,00    |')
print('|   25   |     Portuguesa       |      R$30,00    |       R$39,00    |')
print('-----------------------------------------------')

contador = 0  # Contador de pedidos

while True:  # Laço de repetição do menu

    tamanho = input('Digite o tamanho da pizza (M ou G): ')

    if tamanho == 'M' or tamanho == 'm':

        #codigo = int(input('Digite o código do produto desejado: '))
        try:
            codigo = int(input('Digite o código do produto desejado: '))
            if codigo == 21:
                print('Você pediu uma pizza Napolitana de tamanho M no valor de R$20,00.')
                contador = contador + 20
            elif codigo == 22:
                print('Você pediu uma pizza Marguerita de tamanho M no valor de R$20,00.')
                contador = contador + 20
            elif codigo == 23:
                print('Você pediu uma pizza Calabresa de tamanho M no valor de R$25,00.')
                contador = contador + 25
            elif codigo == 24:
                print('Você pediu uma pizza Toscana de tamanho M no valor de R$30,00.')
                contador = contador + 30
            elif codigo == 25:
                print('Você pediu uma pizza Portuguesa de tamanho M no valor de R$30,00.')
                contador = contador + 30
            #else:
             #   print('Opção inválida. Digite o código novamente.')  #
              #  continue
        except ValueError as error:
            print('Valor digitado não é aceito.')
            continue

    if tamanho == 'G' or tamanho == 'g':

        codigo = int(input('Digite o código do produto desejado: '))

        if codigo == 21:
            print('Você pediu uma pizza Napolitana de tamanho M no valor de R$26,00.')
            contador = contador + 26
        elif codigo == 22:
            print('Você pediu uma pizza Marguerita de tamanho M no valor de R$26,00.')
            contador = contador + 26
        elif codigo == 23:
            print('Você pediu uma pizza Calabresa de tamanho M no valor de R$32,00.')
            contador = contador + 32
        elif codigo == 24:
            print('Você pediu uma pizza Toscana de tamanho M no valor de R$39,00.')
            contador = contador + 39
        elif codigo == 25:
            print('Você pediu uma pizza Portuguesa de tamanho M no valor de R$39,00.')
            contador = contador + 39
        else:
            print('Opção inválida. Digite o código novamente.')
            continue

    else:
        print('Opção invalida. Digite o tamanho novamente.')
        continue

    opcao = input('Deseja pedir mais alguma coisa?\nDigite 1 para "Sim" e 0 para "Não": ')

    if opcao == '1':
     continue

    elif opcao == '0':
     break

print(f'O total a pagar será de R${contador}.')  # Print do total a pagar somando todos os pedidos
print('Obrigado! Volte sempre!')  # Mensagem final