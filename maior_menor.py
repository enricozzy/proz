# este programa compara três numeros e ira mostrar qual é o maior, o menor e a média desses numeros  

num1 = int (input("digite o primeiro numero: "))
num2 = int (input("digite o segundo numero: "))
num3 = int (input("digite o terceiro numero: "))

#verifica qual e o maior numero
if (num1 > num2) and (num1 > num3): 
    maior = num1 

elif (num2 > num1) and (num2 > num3):
    maior = num2

else:
    maior = num3

    #verifica qual e o menor numero
    if (num1 < num2) and (num1 < num3):
        menor = num1 
    elif (num2 < num1) and (num2 < num3):
        menor = num3 
    else:
        menor = num3
        
        #calcula a media dos três numeros

media = (num1 + num2 + num3) /3 


#exibe os resultados

print ("\n--------------RESULTADO--------------------")
print (f"O MAIOR NUMERO É:{maior}")
print (f"O MENOR NUMERO É: {menor}")
print (f"A MEDIA DOS NUMEROS É: {media:.2f}")

