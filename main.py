import requests 

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") 
requisicao_dic = requisicao.json()
cotacao_dolar = requisicao_dic["USDBRL"]['bid']


print("1- Reais p/ Dolares\n2- Dolares p/ Reais")
valor = input("Deseja converter pra Reais (BRL) ou Dolares (USD)? ")

if valor == "1":
    kratos = input("Digite o valor em Reais que deseja converter: ")
    
elif valor == "2":
    kratos2 = input("Digite o valor em Dolares que deseja converter: ")
    
else:
    print("Opção Inválida!")







