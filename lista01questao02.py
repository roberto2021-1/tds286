#Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.
horas = int(input('Digite a hora: '))
minutos = int(input('Digite os minutos: '))

total_de_minutos = (horas * 60) + minutos

print(f'O total de minutos é = {total_de_minutos} minutos')