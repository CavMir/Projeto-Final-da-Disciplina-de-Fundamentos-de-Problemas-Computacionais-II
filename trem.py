EstacaoInicio = int(input("digite o numero da estação inicial: "))
EstacaoFinal = int(input("digite o numero da estação final: "))

######################### MATRIZES COM AS INFORMAÇÕES DO METRO ################################################
DistanciaReta = [
    [0, 10, 18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1, 16.7, 27.3, 27.6, 29],
    [10, 0, 8.5, 14.8, 26.6, 29.1, 26.1, 17.3, 10, 3.5, 15.5, 20.9, 19.1, 21.8],
    [18.5, 8.5, 0,6.3, 18.2, 20.6, 17.6, 13.6, 9.4, 10.3, 19.5, 19.1, 12.1, 16.6],
    [24.8, 14.8, 6.3, 0, 12, 14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4],
    [36.4, 26.6, 18.2, 12, 0, 3, 2.4, 19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9],
    [38.8, 29.1, 20.6, 14.4, 3, 0, 3.3, 22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2],
    [35.8, 26.1, 17.6, 11.5, 2.4, 3.3, 0, 20, 23, 27.3, 34.2, 25.7, 12.4, 15.6],
    [25.4, 17.3, 13.6, 12.4, 19.4, 22.3, 20, 0, 8.2, 20.3, 16.1, 6.4, 22.7, 27.6],
    [17.6, 10, 9.4, 12.6, 23.3, 25.7, 23, 20, 0, 13.5, 11.2, 10.9, 21.2, 26.6],
    [9.1, 3.5, 10.3, 16.7, 28.2, 30.3, 27.3, 20.3, 13.5, 0, 17.6, 24.2, 18.7, 21.2],
    [16.7, 15.5, 19.5, 23.6, 34.2, 36.7, 34.2, 16.1, 11.2, 17.6, 0, 14.2, 31.5, 35.5],
    [27.3, 20.9, 19.1, 18.6, 24.8, 27.6, 25.7, 6.4, 10.9, 24.2, 14.2, 0, 28.8, 33.6],
    [27.6, 19.1, 12.1, 10.6, 14.5, 15.2, 12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0, 5.1],
    [29.8, 21.8, 16.6, 15.4, 17.9, 18.2, 15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1, 0]
]


Linhas = {
    'AZUL': 15,
    'AMARELA': 7,
    'VERMELHA': 10,
    'VERDE': 20
}

DistanciaAdj = {
    1: [[2, 10, 'AZUL']],
    2: [[1, 10, 'AZUL'], [3, 8.5, 'AZUL'], [9, 10, 'AMARELA'], [10, 3.5, 'AMARELA']],
    3: [[2, 8.5, 'AZUL'], [4, 6.3, 'AZUL'], [9, 9.4, 'VERMELHA'], [13, 18.7, 'VERMELHA']],
    4: [[3, 6.3, 'AZUL'], [5, 13, 'AZUL'], [8, 15.3, 'VERDE'], [13, 12.8, 'VERDE']],
    5: [[4, 13, 'AZUL'], [6, 3, 'AZUL'], [7, 2.4, 'AMARELA'], [8, 30, 'AMARELA']],
    6: [[5, 3, 'AZUL']],
    7: [[5, 2.4, 'AMARELA']],
    8: [[4, 15.3, 'VERDE'], [5, 30, 'AMARELA'], [9, 9.6, 'AMARELA'], [12, 6.4, 'VERDE']],
    9: [[2, 10, 'AMARELA'], [3, 9.4, 'VERMELHA'], [8, 9.6, 'AMARELA'], [11, 12.2, 'VERMELHA']],
    10: [[2, 3.5, 'AMARELA']],
    11: [[9, 12.2, 'VERMELHA']],
    12: [[8, 6.4, 'VERDE']],
    13: [[3, 18.7, 'VERMELHA'], [14, 5.1, 'VERDE']],
    14: [[13, 5.1, 'VERDE']]
}

DistanciaReal = [
['*', [10,'AZUL'], '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
[[10,'AZUL'], 0, [8.5, 'AZUL'], '*', '*', '*', '*', '*', [10, 'AMARELA'], [3.5, 'AMARELA'], '*', '*', '*', '*'],
['*',[8.5, 'AZUL'], 0, [6.3, 'AZUL'], '*', '*', '*', '*', [9.4, 'VERMELHA'], '*', '*', '*', [18.7, 'VERMELHA'], '*'],
['*','*',[6.3, 'AZUL'], 0,[13, 'AZUL'], '*', '*', [15.3, 'VERDE'], '*', '*', '*', '*', [12.8, 'VERDE'], '*'],
['*','*','*',[13, 'AZUL'], 0 ,[3, 'AZUL'], [2.4, 'AMARELA'], [30, 'AMARELA'], '*', '*', '*', '*', '*', '*'],
['*','*','*','*',[3, 'AZUL'],0, '*', '*', '*', '*', '*', '*', '*'],
['*','*','*','*',[2.4, 'AMARELA'],'*',0,'*', '*', '*', '*', '*', '*', '*'],
['*','*','*','*',[15.3, 'VERDE'],[30, 'AMARELA'],'*','*',0,[9.6, 'AMARELA'], '*', '*', [6.4, 'VERDE'], '*', '*'],
['*',[10, 'AMARELA'],[9.4, 'VERMELHA'],'*','*','*','*',[9.6, 'AMARELA'],0,'*', [12.2, 'VERMELHA'], '*', '*', '*','*','*','*','*','*','*','*',],
['*',[3.5, 'AMARELA'],'*', '*', '*', '*', '*','*','*',0,'*','*','*','*',],
['*', '*', '*', '*','*','*','*','*',[12.2, 'VERMELHA'],'*',0,'*','*','*',],
['*', '*', '*','*','*','*',[6.4, 'VERDE'],'*','*','*',0,'*','*',],
['*', '*', [18.7, 'VERMELHA'], [12.8, 'VERDE'],'*','*','*','*','*','*',0,[5.1, 'VERDE']],
['*','*','*','*','*','*','*','*','*','*','*','*',[5.1, 'VERDE'],0]
]

#hora de entrada na estacao
Minutos = int(input('Hora de entrada na estação: '))

#ultima linha q o trem esteve
LinhaOriginal = 0
#menor caminho final
CaminhoFinal = []

#FUNÇÃO QUE CALCULA O TEMPO TOTAL ENTRE DUAS ESTAÇOES
def Tempo(inicio, fim, linha=None):
    Distancia = 0
    TempoFinal = 0
    LinhaTrem = 0
    if inicio == fim:
        return Distancia  , TempoFinal , LinhaTrem 
    
    # Tempo final é so o tempo de uma estaçao pra outra, Distancia é o tempo final + distancia em linha reta
    print()
    print('inicio: {} fim: {}'.format(inicio, fim))
    TempoFinal = DistanciaReal[inicio-1][fim-1][0] *40/60
    print('ESSE É O TEMPO FINAL: {}'.format(TempoFinal))
    print('Estacao final {}'.format(EstacaoFinal))
    Distancia = (DistanciaReta[EstacaoFinal-1][fim-1]) * 40/60
    print('distancia {}'.format(Distancia))
    Distancia += TempoFinal
    print('essa eh a distancia + tempo real {}'.format(Distancia))
    LinhaTrem = DistanciaReal[inicio-1][fim-1][1]
    print('essa eh a linha {}'.format(linha))
    
    
    if linha != LinhaTrem:
        #ESPERAR TREM + BALDEAMENTO
        print('trocou de linha')
        Distancia += 4 
        Distancia += (TempoFinal+4+Minutos) % Linhas[DistanciaReal[inicio-1][fim-1][1]]
        TempoFinal += (TempoFinal+4+Minutos) % Linhas[DistanciaReal[inicio-1][fim-1][1]] + 4
        print('tempofinal com baldeamento e espera: {}'.format(TempoFinal))
        print('distancia com baldeamento e espera: {}'.format(Distancia))
    print()   
    return Distancia, TempoFinal, LinhaTrem



def a_star(estacao, estacao_final, LinhaAtual):
    if estacao == estacao_final:
        CaminhoFinal.append(estacao)
        return
    else:
        print('ESSA É A ESTAcao {}'.format(estacao))
        print('')
        menorDistancia = 1000000000000000000000000000
        menortempo= 1000000000000000000000000000
        caminho = ''
        for ligacao in DistanciaAdj[estacao]:
            if ligacao[0] not in CaminhoFinal:
                DistanciaEntreEstacoes ,TempoEntreEstacoes, LinhaFinal = Tempo(estacao, ligacao[0], LinhaAtual)
                if DistanciaEntreEstacoes < menorDistancia:
                    menorDistancia = DistanciaEntreEstacoes
                    menortempo=TempoEntreEstacoes
                    LinhaTemporaria = LinhaFinal
                    caminho= ligacao[0]

        CaminhoFinal.append(caminho)
        LinhaOriginal = LinhaTemporaria
        print('caminho: {}| estacao_final: {}| linhaoriginal: {}'.format(caminho,estacao_final,LinhaOriginal))
        a_star(caminho, estacao_final, LinhaOriginal)


#Tempo(4, 3)
#print('')
#Tempo(4, 5) 

#print()
#Tempo(3,2)
#print()
#Tempo(3,4)
CaminhoFinal.append(EstacaoInicio)
a_star(EstacaoInicio,EstacaoFinal,LinhaOriginal)
print(CaminhoFinal)
