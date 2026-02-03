# calculadora simples
# Rafaela
print("Calculadora usando Match Case")
print("Soma (+)\nSubtração (-)\nMultiplicação (*)\nDivisão(/)\n")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operador = input("Digite o operador: ")

match operador:
    case "+":
        resultado = num1 + num2
    case "-":
        resultado = num1 - num2
    case "*":
        resultado = num1 * num2
    case "/":
        if num2 == 0:
            resultado = "Erro de divisão por zero!"
        else:
            resultado = num1 / num2
    case _:
       resultado = "Operador inválido!"

print("Resultado: ", resultado)
