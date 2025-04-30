#este programa realiza operações basicos com dois numeros fornecidos pelo usuario.
num1 = float (input("DIGITE O PRIMEIRO NUMERO: "))
num2 = float (input("DIGITE O SEGUNDO NUMERO: "))
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2 

if num2 != 0:
    divisao = num1 / num2 
    
else:
    divisao = "divido por zero não é permitido"
    
media = (num1 + num2) / 2 

print ("---------------------RESULTADO---------------------------------")
print (f"SOMA: {soma}")
print (f"SUBTRAÇÃO: {subtracao}")
print (f"MULTIPLICAÇÃO: {multiplicacao}")
print (f"DIVISÃO: {divisao}") 

print ("----------------------------------------------------------")