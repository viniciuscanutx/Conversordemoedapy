#Bibliotecas usadas no projeto.
import requests
import sys

#Aqui a biblioteca requests vai fazer a requisição para conseguir a cotação do dólar em tempo real!
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") 
requisicao_dic = requisicao.json()
cotacao_dolar = requisicao_dic["USDBRL"]['bid']

#Aqui criamos aonde vai ser feita a conversão e vai ser exibida na tela do usuário.
def convertpapai():

 while True:

     print("1-USD para BRL\n2-BRL para USD")
     valor = input("Deseja converter pra Reais (BRL) ou Dolares (USD)? ")
     print("\n")

#Aqui tive que usar float porque os válores são quebrados.
     if valor == "1":
      flowers = float(cotacao_dolar)
      print("Cotação atual do Dólar =",cotacao_dolar)
      print("\n")
      kratos = float(input("Informe o valor em Reais para conversão: "))
      print("\n")
      valorresult = kratos * flowers
      print("O resultado da conversão de Reais para Dólares é:\n US$:",valorresult)
      print("\n")
      choiceuser2()
    
     elif valor == "2":
      flowers2 = float(cotacao_dolar)
      print("Cotação Atual =",cotacao_dolar)
      kratos2 = float(input("Informe o valor em Dólar para conversão: "))
      print("\n")
      valorresult2 = flowers2 * kratos2
      print("O resultado da conversão de USD para BRL é:\n RS$:",valorresult2)
      print("\n")
      choiceuser2()

#Caso o usuário digite a opção errada ele retornará para o menu, assim, impedindo que o programa crashe.
     else:
      print("Opção Inválida!")
      print("\n")
      return convertpapai()


#Aqui é uma pequena tela de seleção para saber se o usuário deseja fazer alguma outra conversão.
def choiceuser2():
    
 while True:

  print("1-Sim\n2-Não")
  notime = input("Deseja converter outro valor?\n==> ")
 
  if notime == "1":
    print("\n")
    return convertpapai()

  elif notime == "2":
   print("\n")
   print("Good Bye =)")
   return fechar()

  else:
    print("Opção Inválida!")
    print("\n")
    return choiceuser2()


#Prefiro usar a biblioteca sys para fazer o comando de fechar o programa pois evita bugs e vou compilar em .exe depois.
def fechar():
    sys.exit()


#Sem isso, o programa não roda!
convertpapai()
choiceuser2()
