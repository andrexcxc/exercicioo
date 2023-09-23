# define uma funcao 
def f(x, y):
    y_temp = y.replace('x', str(x))
    return eval(y_temp)
# requisita as funcoes e o valor de x
f1 = input("Digite a primeira funcao ")
f2 = input("Digite a segunda funcao ")
x = str(input("Digite o valor de x "))
## imprime o resultado
print(f(f(x, f1), f2))