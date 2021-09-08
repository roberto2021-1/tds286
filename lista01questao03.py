#Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos
minuto = int(input('Digite os minutos a serem convertidos: '))

hora = minuto // 60
resto_minuto = minuto % 60

print(f'O valor digitado corresponde a {hora} hora(as) e {resto_minuto} minutos(s)')