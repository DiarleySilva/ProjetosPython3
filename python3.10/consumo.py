# Variáveis
watts = float(input('Digite o consumo em Watts do aparelho: '))
horas = float(input('Digite quantas horas o aparelho fica ligado por dia: '))
dias = int(input('Quantos dias o aparelho fica ligado por mês: '))
kwh = float(input('Quanto está custando o Kwh na sua cidade: '))

# Calculo
consumo = (watts * horas * dias / 1000) * kwh

# Resultado
print(f'O seu aparelho consome R${consumo:.2f} por mês.')
