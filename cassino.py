import nntplib
import os
import time
vermelho = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
preto = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 28, 31, 33, 35]

#Grupos
st1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
nd2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
rd3 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

# Grupo Horizontal
h1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
h2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
h3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

# Variavel contadorass
cImpar, cPar, cCorV, cCorP, cNumSort, pCentBolasV, pCentBolasP, pCentImp, pCentPar, cSorteada, nSort, cZeros = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
cSt1, cNd2, cRd3, cH1, cH2, cH3, pSt1, pNd2, pRd3, pH1, pH2, pH3, pZeros, cMenor, cMaior,pMaior, pMenor = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
segue = True

while segue:
    try:
        print( 5 * '*', f'QTD numero analisados {cNumSort}\n' )
        print(f'N° Sorteado : {nSort}, {cSorteada}')
        
        print(35 * '_')
        print('Impar = {} e {:.0f} %\nPar   = {} e {:.0f} %'.format(cImpar, pCentImp, cPar, pCentPar) )
        print('Zeros = {} e {:.0f} %'.format(cZeros, pZeros))
        
        print(35 * '_')
        print('VERMELHO = {} e {:.0f} % \nPRETO    = {} e {:.0f} % '.format(cCorV, pCentBolasV, cCorP, pCentBolasP))
        
        print(35 * '_')
        print('Grupo ST1 = {}  e  {:.0f} %'.format(cSt1, pSt1))
        print('Grupo ND2 = {}  e  {:.0f} %'.format(cNd2, pNd2))
        print('Grupo RD3 = {}  e  {:.0f} %'.format(cRd3, pRd3))
        
        print(35 * '_')
        print('Grupo H1 = {}  e  {:.0f} %'.format(cH1, pH1))
        print('Grupo H2 = {}  e  {:.0f} %'.format(cH2, pH2))
        print('Grupo H3 = {}  e  {:.0f} %'.format(cH3, pH3))
        
        print(35 * '_')
        print('N° <= 18 = {} e {:.0f} %'.format(cMenor, pMenor))
        print('N° >= 19 = {} e {:.0f} %'.format(cMaior, pMaior))
        
        print(35 * '_')

        nSort = int(input('Digite o numero Sorteado: '))

        if nSort in vermelho:
            cCorV = cCorV + 1
            cSorteada = 'Vermelha'

        elif nSort in preto:
            cCorP =cCorP + 1
            cSorteada = 'Preto'
        elif nSort == 0 :
            cSorteada = 'Verde'

        # Logicas

        # Quantidade de números Pares e Impares sorteados
        if nSort > 0 and nSort % 2 == 0 and nSort < 37 :
            cPar = cPar + 1
            cNumSort = cNumSort + 1
        elif nSort > 0 and nSort % 2 > 0 and nSort < 37:
            cImpar = cImpar + 1
            cNumSort = cNumSort + 1
        elif nSort == 0 :
            cZeros = cZeros +1
            cNumSort = cNumSort + 1

    # Quantidades por Grupos sorteado st1, nd2, rd3
        if nSort in st1:
            cSt1 = cSt1 + 1

        elif nSort in nd2:
            cNd2 = cNd2 + 1

        elif nSort in rd3:
            cRd3 = cRd3 + 1

        pSt1 = (cSt1 / cNumSort) * 100
        pNd2 = (cNd2 / cNumSort) * 100
        pRd3 = (cRd3 / cNumSort) * 100

    # Quantidades por Grupos sorteado h1 h2 h3

        if nSort in h1:
            cH1 = cH1 + 1

        elif nSort in h2:
            cH2 = cH2 + 1

        elif nSort in h3:
            cH3 = cH3 + 1

        # Porcentagem de numero impar, pares
        pCentImp = (cImpar / cNumSort) * 100
        pCentPar = (cPar / cNumSort) * 100

        # Porcentagem vermelhos e preta
        pCentBolasV = (cCorV / cNumSort) * 100
        pCentBolasP = (cCorP / cNumSort) * 100

        pH1 = (cH1 / cNumSort) * 100
        pH2 = (cH2 / cNumSort) * 100
        pH3 = (cH3 / cNumSort) * 100

        pZeros = (cZeros / cNumSort) * 100
        if nSort < 0 :
            os.system('cls')
            print(5 * '*', 'Numero invalido', 5 * '*')
            time.sleep(2)

             
        elif nSort >18 and nSort < 37:
            cMaior = cMaior+1
            
        elif nSort<=18 and nSort < 37 :
            cMenor = cMenor +1
            
        pMenor = (cMenor / cNumSort) * 100 
        pMaior = (cMaior /cNumSort) * 100   
        

        if nSort > 36:
            cSorteada = 0
            os.system('cls')
            print(5 * '*', 'ATENÇÃO', 5 * '*')
            print("Numero digitado Maior que permitido")
            time.sleep(2)



    # Troca de Sorteador

    # Quantos acertos

    # Quantos erros

    #Probabilidades
    except ZeroDivisionError:
        os.system('cls')
        print(5 * '*', 'ATENÇÃO', 5 * '*')
        print('O numero inicial digitado é maior que o permitido ')
        time.sleep(2)
    except ValueError:
        os.system('cls')
        print('Tipo de Valor invalido')
        time.sleep(2)

    os.system('cls')