# Esse projeto foi pelo pelo grupo formado por Caio Cavalcanti Miranda e João Marcelo Alves. 
# Ambos os integrantes trabalharam juntos no desenvolvimento criativo do código e em pesquisas para melhor entender o funcionamento do algortimo a*. 
# A versão inicial do código foi escrita por João Marcelo e a versão final polida por Caio Miranda.


Origem = [input('Origem (E1, ..., E14): ')]
Destino = input('Destino (E1, ..., E14): ')
Horario = [int(i) for i in input('Horário (HH:MM): ').split(':')]
Horario = (Horario[0]-4)*60+Horario[1]

DistanciaReta = [
    [10, 18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1, 16.7, 27.3, 27.6, 29.8],
    [8.5, 14.8, 26.6, 29.1, 26.1, 17.3, 10, 3.5, 15.5, 20.9, 19.1, 21.8],
    [6.3, 18.2, 20.6, 17.6, 13.6, 9.4, 10.3, 19.5, 19.1, 12.1, 16.6],
    [12, 14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4],
    [3, 2.4, 19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9],
    [3.3, 22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2],
    [20, 23, 27.3, 34.2, 25.7, 12.4, 15.6],
    [8.2, 20.3, 16.1, 6.4, 22.7, 27.6],
    [13.5, 11.2, 10.9, 21.2, 26.6],
    [17.6, 24.2, 18.7, 21.2],
    [14.2, 31.5, 35.5],
    [28.8, 33.6],
    [5.1]
]

Linhas = {
    'AZUL': 15,
    'AMARELA': 7,
    'VERMELHA': 10,
    'VERDE': 20
}

DistanciaAdj = {
    'E1': [['E2', 10, 'AZUL']],
    'E2': [['E1', 10, 'AZUL'], ['E3', 8.5, 'AZUL'], ['E9', 10, 'AMARELA'], ['E10', 3.5, 'AMARELA']],
    'E3': [['E2', 8.5, 'AZUL'], ['E4', 6.3, 'AZUL'], ['E9', 9.4, 'VERMELHA'], ['E13', 18.7, 'VERMELHA']],
    'E4': [['E3', 6.3, 'AZUL'], ['E5', 13, 'AZUL'], ['E8', 15.3, 'VERDE'], ['E13', 12.8, 'VERDE']],
    'E5': [['E4', 13, 'AZUL'], ['E6', 3, 'AZUL'], ['E7', 2.4, 'AMARELA'], ['E8', 30, 'AMARELA']],
    'E6': [['E5', 3, 'AZUL']],
    'E7': [['E5', 2.4, 'AMARELA']],
    'E8': [['E4', 15.3, 'VERDE'], ['E5', 30, 'AMARELA'], ['E9', 9.6, 'AMARELA'], ['E12', 6.4, 'VERDE']],
    'E9': [['E2', 10, 'AMARELA'], ['E3', 9.4, 'VERMELHA'], ['E8', 9.6, 'AMARELA'], ['E11', 12.2, 'VERMELHA']],
    'E10': [['E2', 3.5, 'AMARELA']],
    'E11': [['E9', 12.2, 'VERMELHA']],
    'E12': [['E8', 6.4, 'VERDE']],
    'E13': [['E3', 18.7, 'VERMELHA'], ['E4', 12.8, 'VERDE'], ['E14', 5.1, 'VERDE']],
    'E14': [['E13', 5.1, 'VERDE']]
}

def Ordem(Nodo):
    return Nodo[-1]

Caminho = []
EstacoesVisitadas = []
def a_star(EstacaoAtual, EstacaoDestino, HorarioAtual, LinhaAtual):
    if EstacaoAtual[-1] not in EstacoesVisitadas:
        EstacoesVisitadas.append(EstacaoAtual[-1])
        if EstacaoAtual[-1] == EstacaoDestino:
            return [HorarioAtual, EstacaoAtual]
        if HorarioAtual < 0:
            HorarioAtual = 0
        elif HorarioAtual > 1200 and HorarioAtual < 1440:
            HorarioAtual = 1440
            LinhaAtual = 0

        for EstacaoAdj in DistanciaAdj[EstacaoAtual[-1]]:
            if EstacaoAdj[0] not in EstacoesVisitadas:
                CaminhoAtual = [i for i in EstacaoAtual]
                CaminhoAtual.append(EstacaoAdj[0])
                CaminhoTeste = EstacaoAdj[1]*3/2
                if LinhaAtual and LinhaAtual != EstacaoAdj[2]:
                    CaminhoTeste += 4
                    if (HorarioAtual+4)%Linhas[EstacaoAdj[2]] != 0:
                        CaminhoTeste += Linhas[EstacaoAdj[2]]-(HorarioAtual+4)%Linhas[EstacaoAdj[2]]
                elif HorarioAtual%Linhas[EstacaoAdj[2]] != 0:
                    CaminhoTeste += Linhas[EstacaoAdj[2]]-HorarioAtual%Linhas[EstacaoAdj[2]]
                HorarioCaminho = CaminhoTeste + HorarioAtual
                if EstacaoAdj[0] != EstacaoDestino:
                    CaminhoTeste += (DistanciaReta[int(EstacaoAdj[0][1:])-1][int(EstacaoDestino[1:])-int(EstacaoAdj[0][1:])-1])*3/2 if int(EstacaoAdj[0][1:]) < int(EstacaoDestino[1:]) else (DistanciaReta[int(EstacaoDestino[1:])-1][int(EstacaoAdj[0][1:])-int(EstacaoDestino[1:])-1])*3/2
                Caminho.append([CaminhoAtual, HorarioCaminho, EstacaoAdj[2], CaminhoTeste+HorarioAtual])
        Caminho.sort(key=Ordem)

        for ProxEstacao in Caminho:
            Chegada = a_star(ProxEstacao[0], EstacaoDestino, ProxEstacao[1], ProxEstacao[2])
            if Chegada:
                return Chegada
                
Goal = a_star(Origem, Destino, Horario, 0)
Goal[0] -= 1440 if Goal[0] >= 1200 else 0
print('Seu ETA é {}:{}, seu caminho é {}'.format(str(int(Goal[0]//60)+4).zfill(2), str(round(Goal[0]%60)).zfill(2), ' '.join(Goal[1])))
