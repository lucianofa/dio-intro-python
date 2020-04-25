a = 11
b = 5
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b #divisão geram decimais x.x
resto = a % b #restos geram decimais x.x
print(soma, subtracao, multiplicacao, divisao, resto)
print(type(soma), type(divisao))
print(int(divisao))
print(str(soma) + ' resultado de soma convertido')
#comentário
soma2= 5 + int('25')
print(soma2)
print('Soma: {}' .format(soma2))

#format utilizando os parâmetros na ordem que aparecem no print
print('Soma: {} Total: {}' .format(soma2, 100))

#format nomeando os parâmetros (\n quebra a linha)
print('***Soma: {par1} \nTotal: {par2}' .format(par1=soma2, par2=100))

#format nomeando os parâmetros (\n quebra a linha) (quebrando a linha)
print('***Soma: {par1} \nTotal: {par2}' .format(par1=soma2,
                                                par2=100))
a = input('sua idade: ')
b = input('the book is on: ')
print('Sua idade é: ' + str(a) + ' e o livro está na {}' .format(b))
idade = 20
ano = 2000
############ se nomeou os parâmetros dentro da string tem que nomear dentro do format
print('Idade: {idade} Ano: {ano}'.format(idade=idade, ano=ano))