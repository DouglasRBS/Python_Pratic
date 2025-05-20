n1 = int(input('Digite algo:'))
n2 = int(input('Digite outro: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
ri = n1 ** n2
di = n1 // n2

print('O valor é {}, Multi: {}, divisao {}, '.format(s, m, d))
print('A potencia é {} e a divisao inteira é {}'.format(ri, di))