t_termo = int(input("Informe o terceiro termo da PA: "))
razão = int(input("Informe a razão: "))
n = int(input("Informe o número de termos a serem descobertos, o valor deve ser maior que 3: "))
contador = 0
while n<=3:
  n = int(input("Informe o número de termos a serem descobertos, o valor deve ser maior que 3: "))
print("\nSegue o desenvolvimento da PA: ")
print(t_termo - (2*razão))
print(t_termo - razão)
  contador += 1
  PA = t_termo + (contador - 1) * razão
  print(PA)
