import requests
import sys

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") 
requisicao_dic = requisicao.json()
cotacao_dolar = requisicao_dic["USDBRL"]['bid']


def convertpapai():

 while True:

     print("1-USD para BRL\n2-BRL para USD")
     valor = input("Deseja converter pra Reais (BRL) ou Dolares (USD)? ")
     print("\n")

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
    
     else:
      print("Opção Inválida!")
      print("\n")
      return convertpapai()


def choiceuser2():
    
 while True:

  print("1-Sim\n2-Não")
  notime = input("Deseja converter outro valor?\n==> ")
 
  if notime == "1":
    return convertpapai()

  elif notime == "2":
   return fechar()

  else:
    print("Opção Inválida!")
    print("\n")
    return choiceuser2()



def fechar():
    sys.exit()



convertpapai()
choiceuser2()
