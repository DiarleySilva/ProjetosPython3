# -*- coding: utf-8 -*-
def cadastrarPeca(codigoPeca): # Função de cadastrar peça

  print(f'Código gerado: {codigoPeca}') # Print do código gerado para cada peça
  
  nome = input('Digite o nome da peça: ') # Nome da peça a ser cadastrada
  fabricante = input('Digite a fabricante da peça: ') # Fabricante da peça a ser cadastrada
  valor = input('Digite o valor da peça: ') # Valor da peça a ser cadastrada

  estoque = {'Código:' : codigoPeca, 'Peça:' : nome, 'Fabricante:' : fabricante, 'Valor:' : valor} # Dicionário das peças cadastradas
  pecas.append(estoque.copy()) # Cria uma cópia do dicionário

  print('\nPeça cadastrada com sucesso!') # Print quando a peça é cadastrada

def consultarPeca(): # Função de consultar peça
 
 while True: # Laço de repetição das opções de consulta
  
  # Print das opções de consulta 
  print('1 - Consultar todas as peças')
  print('2 - Consultar peças por código')
  print('3 - Consultar peças por fabricante')
  print('4 - Retornar')
  
  opcao = input('Qual opção deseja: ') # Variável da opção de consulta escolhida
  
  if opcao == '1': # Se a opção for 1, será consultada todas as peças
    print('Consultando todas as peças!') # Mensagem indicando que irá consultar todas as peças
    for peca in pecas: # Realiza uma varredura no dicionário
      for chave, valor in peca.items(): # Captura os itens dentro do dicionário
        print(f'{chave} : {valor}') # Print da chave e do valor do dicionário
  
  elif opcao == '2': # Se a opção for 2, será consultada as peças por código
    print('Consultando peças por código...') # Mensagem indicando que irá consultar uma peça por código
    codigoconsulta = int(input('Digite o código para ser consultado: ')) # Código da peça a ser consultada
    for peca in pecas: # Realiza uma varredura no dicionário
      if peca['Código:'] == codigoconsulta: # Verifica se o código é igual ao do dicionário
        for chave, valor in peca.items(): # Captura os itens dentro do dicionário
          print(f'{chave} : {valor}') # Print da chave e do valor do dicionário
        
  elif opcao == '3': # Se a opção for 3, será consultada as peças por fabricante
    print('Consultando peças por fabricante...') # Mensagem indicando que irá consultar uma peça por fabricante
    fabricante = input('Digite o fabricante para ser consultado: ') # Fabricante da peça a ser consultada
    for peca in pecas: # Realiza uma varredura no dicionário
      if peca['Fabricante:'] == fabricante: # Verifica se o fabricante é igual ao do dicionário
        for chave, valor in peca.items(): # Captura os itens dentro do dicionário
          print(f'{chave} : {valor}') # Print da chave e do valor do dicionário
  
  elif opcao == '4': # Se a opção for 4, será retornado ao menu principal
    return
  
  else: # Se a opção for inválida, voltará para as opções
    print('Opção inválida!')
    continue

def removerPeca(): # Função de remover peça
  print('Removendo peça...') # Mensagem indicando que irá remover uma peça
  remover = int(input('Digite o código da peça para ser removido: ')) # Variável do código que irá ser removido
  for peca in pecas: # Realiza uma varredura no dicionário
    if peca['Código:'] == remover: # Verifica se o código é igual ao do dicionário
      pecas.remove(peca) # Se for igual, a peça será removida do dicionário
      print('Peça removida com sucesso!') # Print quando a peça é removida

# Programa principal
print('Olá, seja bem-vindo a loja de peças do Diarley Silva Santos (RU 4095617).\n')

pecas = [] # Lista para ser adicionada o dicionário
codigo = 0 # Contador para cada peça cadastrada
while True: # Laço de repetição do menu principal
  # Print do menu principal
  print('-' * 20)
  print('1 - Cadastrar peças')
  print('2 - Consultar peças')
  print('3 - Remover peças')
  print('4 - Sair')
  print('-' * 20)

  opcao = input('Qual opção deseja realizar: ') # Variável da opção escolhida no menu principal

  if opcao == '1': # Se a opção for 1, irá cadastrar uma peça
    codigo = codigo + 1 # Atribuindo mais um valor no contador
    cadastrarPeca(codigo) # Chamando a função de cadastro
  elif opcao == '2': # Se a opção for 2, irá consultar uma peça
    consultarPeca() # Chamando a função de consulta
  elif opcao == '3': # Se a opção for 3, irá remover uma peça
    removerPeca() # Chamando a função de remover
  elif opcao == '4': # Se a opção for 4, o programa será encerrado
    break