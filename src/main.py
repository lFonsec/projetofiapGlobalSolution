"""
Bandeira verde: condições favoráveis de geração de energia. A tarifa não sofre nenhum acréscimo.
Bandeira amarela: condições de geração menos favoráveis. A tarifa sofre acréscimo de R$ 1,885 para cada 100 kWh (quilowatts-hora) consumidos.
Bandeira vermelha - Patamar 1: condições mais custosas de geração. A tarifa sofre acréscimo de R$ 4,463 para cada 100 kWh (quilowatts-hora) consumidos.
Bandeira vermelha - Patamar 2: condições ainda mais custosas de geração. A tarifa sofre acréscimo de R$ 7,877 para cada 100 kWh (quilowatts-hora) consumidos.
Enel São Paulo (SP): O preço do kWh pode variar entre R$ 0,80 e R$ 1,10, dependendo da categoria e da bandeira tarifária. -> 1.00 por kWh
Residências pequenas (1 a 2 pessoas): Entre 150 kWh e 250 kWh por mês. -> 200
Residências médias (3 a 4 pessoas): Entre 250 kWh e 400 kWh por mês. -> 300
Residências grandes (5 ou mais pessoas): Entre 400 kWh e 600 kWh por mês ou mais. -> 500

Fonte de Energia	  Custo Médio de Geração (R$ por MWh)
    Hidrelétrica	         R$ 100 - R$ 300 -> 200 por 1 mWh ->  0.20 por 1 kWh
    Solar	                 R$ 120 - R$ 300 -> 210 por 1 mWh ->  0.21 por 1 kWh
    Eólica	                 R$ 120 - R$ 220 -> 170 por 1 mWh ->  0.17 por 1 kWh
    Gás Natural	             R$ 300 - R$ 600 -> 400 por 1 mWh ->  0.40  por 1 kWh

"""
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
from random import randint
import random

#faz a simulação de quantos meses o usuario quiser
# com os valores default de bandeira verde e consumo meedio de 500 kwh por mes
def simulacao(bandeira = 0, consumo_medio = 500):
    data = datetime.now() #pega a data para fazer a contagem dos meses para a simulação
    numero_simulacao = int(input("Digite o numero de simulações que deseja fazer: ")) # quantos meses o usuario quer simular
    consumo_medio_tecnologia = consumo_medio * 0.06 #calcular o consumo medio usando as 3 tecnologias apresentada nas etapas anterior
    valor_gasto = consumo_medio * 0.20 #o valor gasto por kwh
    valor_gasto_tecnologia = consumo_medio_tecnologia * 0.20 #o valor gasto do consumo medio usando as tecnologia
    bandeira_aleatoria = [0, 1.88, 4.46, 7.78] # uma lista com os valores aditivos das bandeiras
    dic = {"dia": data, "bandeira": bandeira, "consumo_medio": consumo_medio, "consumo_medio_tecnologia":consumo_medio_tecnologia,
           "valor_gasto": valor_gasto, "valor_gasto_tecnologia": valor_gasto_tecnologia} # monta um dic para ser usado como dataframe pelo pandas
    df = pd.DataFrame([dic])
    y = 1
    for x in range(numero_simulacao):
        nova_data = data + timedelta(days=x)
        y += 1
        if y%5 == 0 or y == 2:# altera o valor da bandeira a cada 5 meses
            bandeira_random = random.choice(bandeira_aleatoria)
        consumo_medio_random = randint(300, 600)#fica alterando o valor do consumo medio de forma aleatoria entre 300 e 600
        consumo_medio_tecnologia = consumo_medio_random * 0.06 #calula o consumo medio com as tecnologia
        valor_gasto = consumo_medio_random * 0.20 # valor gastro
        valor_gasto_tecnologia = consumo_medio_tecnologia * 0.20 # valor gasto com as tecnologia
        novo_dic = {"dia": nova_data , "bandeira": bandeira_random, "consumo_medio": consumo_medio_random,
        "consumo_medio_tecnologia":consumo_medio_tecnologia,
        "valor_gasto": valor_gasto, "valor_gasto_tecnologia": valor_gasto_tecnologia} # criando um novo dic
        df_novo = pd.DataFrame([novo_dic]) # monta um dataframe com o novo dic
        df = pd.concat([df, df_novo], ignore_index=True) #concatena os dois dataframe
    df.to_csv("simulacao.csv") # converte o df para csv
    grafico(df) # chama o grafico

#monta um grafico mostrando o valor gasto com e sem as tecnologia
def grafico(df):
    plt.plot(df['dia'], df['valor_gasto'], label='sem as tecnologia')
    plt.plot(df['dia'], df['valor_gasto_tecnologia'], label='com as tecnologia')
    plt.xlabel('Data')
    plt.ylabel('Consumo')
    plt.legend()
    plt.show()

#muda o consumo medio
def consumo_medio():
    return int(input("Qual o consumo medio"))

#faz a pergunta sobre cada bandeira tarifaria
def bandeira_tarifa():
    print("Escolha a bandeira Tarifaria: ")
    try:
        print("Digite a bandeira tarifaria atual:\n"
              "1) Verde  (Nenhum acréscimo)\n"
              "2) Amarela (sofre acréscimo de R$ 1,885 para cada 100 kWh)\n"
              "3) vermelha - Patamar 1 (sofre acréscimo de R$ 4,463 para cada 100 kWh)\n"
              "4) vermelha - Patamar 2 (sofre acréscimo de R$ 7,877 para cada 100 kWh)\n"
              "0) Sair do progrma\n")
        opcao2 = int(input("Digite a opção escolhida: "))
    except ValueError:
        print("Digite um valor valido\n")
    else:
        if opcao2 == 1:
            return 0
        elif opcao2 == 2:
            return 1.88
        elif opcao2 == 3:
            return 4.46
        elif opcao2 == 4:
            return 7.78
        elif opcao2 == 0:
            sair_programa()

#fecha o programa
def sair_programa():
    print("Fechando o programa...")
    exit()


# fazendo as pergunta caso queira trocar a bandeira, mudar o consumo ou fazer a simulação
while True:
    try:
        bandeira = 0
        consumo = 500
        print("----------------------\n"
              "Digite opcao desejada:\n"
              "1) Mudar bandeira tarifaria\n"
              "2) Mudar consumo medio da residencia\n"
              "3) Simular\n"
              "0) Sair do progrma\n")
        opcao1 = int(input("Digite a opção escolhida: "))
    except ValueError:
        print("Digite um valor valido")
    else:
        if opcao1 == 1:
            bandeira = bandeira_tarifa()
        elif opcao1 == 2:
            consumo = consumo_medio()
        elif opcao1 == 3:
            simulacao(bandeira, consumo)
        elif opcao1 == 0:
            sair_programa()
        else:
            print("Digite um valor valido ")
