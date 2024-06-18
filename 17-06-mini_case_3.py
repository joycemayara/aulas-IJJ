import math
# Objetivo: Retorno de 5 outputs
# Obtenção do valor
valor = float(input("Digite o valor a ser transformado: "))
# Cálculo dos Outputs
dobro_do_valor = valor * 2
triplo_do_valor = valor * 3
valor_ao_quadrado = valor ** 2
raiz_quadrada_do_valor_formula = math.sqrt(valor) 
raiz_quadrada_do_valor = valor ** (1/2)
raiz_cubica_do_valor = valor ** (1/3)
# Impressão dos valores
print(f"O valor inserido é:  {valor}")
print(f"O dobro do valor é: {dobro_do_valor}")
print(f"O triplo do valor é: {triplo_do_valor}")
print(f"O valor ao quadrado é: {valor_ao_quadrado}")
print(f"A raiz quadrada do valor, usando fórmula, é:  {raiz_quadrada_do_valor_formula}")
print(f"A raiz quadrada do valor, sem fórmula, é:  {raiz_quadrada_do_valor}")
print(f"A raiz cúbica do valor é:  {raiz_cubica_do_valor}")
