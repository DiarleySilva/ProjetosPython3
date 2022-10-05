altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso em Kg: '))

imc = peso / (altura * altura)

print(f'\nSua altura é de: {altura}cm')
print(f'Seu peso é de: {peso}Kg')
print(f'Seu IMC é de: {imc:.2f}\n')

if imc < 18.5:
    print('Você está magro.')
elif imc >= 18.5 and imc <= 24.9:
    print('Você está com peso normal.')
elif imc >= 25 and imc <= 29.9:
    print('Você está com sobrepeso.')
elif imc >= 30 and imc <= 34.9:
    print('Você está com obesidade grau I.')
elif imc >= 35 and imc <= 40:
    print('Você está com Obesidade grau II.')
elif imc > 40:
    print('Você está com Obesidade grau III.')