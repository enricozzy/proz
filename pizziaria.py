print ("PIZZARIA COMA BASTANTE - SEJA BEM VINDO")
print ("_______CARDAPIO - PREÇO______")
print (" ")
print (" PIZZAS - SABORES ")
print (" CALABRESA, FRANGO, CATUPIRY" )
print (" PIZZAS - TAMANHO ")
print ("PIZZA PEQUENA R$ 20.00 ")
print ("PIZZA MEDIA R$ 25.00" )
print (" PIZZA GRANDE r$ 30.00")
print (" REFRIGENTES ")
print (" COCA-COLA      R$ 7.00")
print (" GUARANA        R$ 6.00")
print (" FANTA          R$ 5.00")
print ("_________________________")
print (" ")
print ("FAÇA O SEU PEDIDO PARA PIZZA")
print ("1 - CALABRESA")
print ("2 - FRANGO")
print ("3 - CATUPIRY")
print (" ")

pedidopizza = int (input())

print ("________________________")
print (" DIGITE O TAMANHO DA PIZZA ")
print ("P - PEQUENA")
print ("M - MEDIA")
print ("G - GRANDE")
print ("______________________________")
tampizza = input().upper

print ("FAÇA O SEU PEDIDO PARA REFRIGERANTE")
print ("1 - COCA-COLA")
print ("2 - GUARANÁ")
print ("3 - FANTA")
pedidorefri = int(input())

if (pedidopizza == 1) and ( tampizza == "P") and (pedidorefri == 1):
 precopagar = 20.00 + 7.00
 pedidos = "CALABREZA, PEQUENA, COCA-COLA"

elif (pedidopizza == 1) and (tampizza == "p") and (pedidorefri == 2):
  precopagar = 20.00 + 6.00
  pedidos = "CALABREZA, PEQUENA, GUARANÁ"

elif (pedidopizza == 1 ) and (tampizza == "p") and (pedidorefri == 3):
  precopagar = 20.00 + 5.00
  pedidos = "CALABREZA , PEQUENA , FANTA"

elif (pedidopizza == 1) and ( tampizza == "M") and (pedidorefri == 1):
 precopagar = 20.00 + 7.00
 pedidos = "CALABREZA, MEDIA, COCA-COLA"

elif (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 2):
  precopagar = 20.00 + 6.00
  pedidos = "CALABREZA, MEDIA, GUARANÁ"

elif (pedidopizza == 1 ) and (tampizza == "M") and (pedidorefri == 3):
  precopagar = 20.00 + 5.00
  pedidos = "CALABREZA , MEDIA , FANTA"

elif (pedidopizza == 1) and ( tampizza == "G") and (pedidorefri == 1):
   precopagar = 30.00 + 7.00
   pedidos = "CALABREZA, GRANDE, COCA-COLA"

elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 2):
  precopagar = 30.00 + 6.00
  pedidos = "CALABREZA, GRANDE, GUARANÁ"

elif (pedidopizza == 1 ) and (tampizza == "G") and (pedidorefri == 3):
  precopagar = 30.00 + 5.00
  pedidos = "CALABREZA , GRANDE , FANTA"

elif (pedidopizza == 2) and ( tampizza == "P") and (pedidorefri == 1):
   precopagar = 20.00 + 7.00
   pedidos = "FRANGO, PEQUENA, COCA-COLA"

elif (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 1):
  precopagar = 25.00 + 7.00
  pedidos = "FRANGO, MEDIA, COCA-COLA"

elif (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 1):
  precopagar = 30.00 + 7.00
  pedidos = "FRANGO , GRANDE , COCA-COLA"

elif (pedidopizza == 2) and ( tampizza == "P") and (pedidorefri == 2):
   precopagar = 20.00 + 6.00
   pedidos = "FRANGO, PEQUENA, GUARANÁ"

elif (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 2):
  precopagar = 25.00 + 6.00
  pedidos = "FRANGO, MEDIA, GUARANÁ"

elif (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 2):
  precopagar = 30.00 + 6.00
  pedidos = "FRANGO , GRANDE , GUARANÁ"
  
elif (pedidopizza == 2) and ( tampizza == "P") and (pedidorefri == 3):
   precopagar = 20.00 + 5.00
   pedidos = "FRANGO, PEQUENA, FANTA"

elif (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 3):
  precopagar = 25.00 + 5.00
  pedidos = "FRANGO, MEDIA, FANTA"

elif (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 3):
  precopagar = 30.00 + 5.00
  pedidos = "FRANGO , GRANDE , FANTA"

elif (pedidopizza == 3) and ( tampizza == "P") and (pedidorefri == 1):
   precopagar = 20.00 + 7.00
   pedidos = "CATUPIRY, PEQUENA, COCA-COLA"

elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 1):
  precopagar = 25.00 + 7.00
  pedidos = "CATUPIRY, MEDIA, COCA-COLA"

elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 1):
  precopagar = 30.00 + 7.00
  pedidos = "CATUPIRY , GRANDE , COCA-COLA"
  
elif (pedidopizza == 3) and ( tampizza == "P") and (pedidorefri == 2):
   precopagar = 20.00 + 6.00
   pedidos = "CATUPIRY, PEQUENA, GUARANÁ"

elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 2):
  precopagar = 25.00 + 6.00
  pedidos = "CATUPIRY, MEDIA, GUARANÁ"

elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 2):
  precopagar = 30.00 + 6.00
  pedidos = "CATUPIRY , GRANDE , GUARANÁ"

elif (pedidopizza == 3) and ( tampizza == "P") and (pedidorefri == 3):
   precopagar = 20.00 + 5.00
   pedidos = "CATUPIRY, PEQUENA, FANTA"

elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 3):
  precopagar = 25.00 + 5.00
  pedidos = "CATUPIRY, MEDIA, FANTA"

elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 3):
  precopagar = 30.00 + 5.00
  pedidos = "CATUPIRY , GRANDE , FANTA"

  print ("___________________________________________________________")
  print (f"O TOTAL A PAGAR É: R$ {precopagar:.2}")
  print ("___________________________________________________________")
  print (f"OS PEDIDOS FORAM {pedidos}")
  print ("___________________________________________________________")
  print ("BOM APETITE E SEJA BEM VINDO")