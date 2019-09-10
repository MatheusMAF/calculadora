#Complete as funcoes a seguir

def soma(a, b):
	#Insira o codigo aqui
	print("A soma deu, ", a + b)
def subtrai(a, b):
	#Insira o codigo aqui
	print("A subtração é, ", a - b)
def multiplica(a, b):
	#Insira o codigo aqui
	print("A multiplicação é, ", a * b)	
def divide(a, b):
	if( divide == 0):
		print("O valor tem que ser diferente de 0")
	else:
	#Insira o codigo aqui
	print("A multiplicação é, ", a / b)	

#Programa principal

print("Calculadora simples")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

soma(num1, num2)
subtrai(num1, num2)
multiplica(num1, num2)
divide(num1, num2)

