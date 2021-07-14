Origem = input('Origem ')
Destino = input('Destino ')
# # Horario = [int(i) for i in input('Horario (HH:MM) ').split(':')]
# # Horario = (Horario[0]-4)*60+Horario[1]
for i in range(int(input())):
    Horario = i
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

    Caminho = []
    def a_star(EstacaoAtual, EstacaoDestino, HorarioAtual, LinhaAtual):
        if HorarioAtual < 0:
            HorarioAtual = 0
        elif HorarioAtual > 1200:
            HorarioAtual = 0
            LinhaAtual = 0
        Caminho.append(EstacaoAtual)
        MenorCaminho = float('inf')
        for EstacaoAdj in DistanciaAdj[EstacaoAtual]:
            if EstacaoAdj[0] not in Caminho:
                CaminhoTeste = EstacaoAdj[1]*3/2
                if LinhaAtual and LinhaAtual != EstacaoAdj[2]:
                    CaminhoTeste += 4
                    if (HorarioAtual+4)%Linhas[EstacaoAdj[2]] != 0:
                        CaminhoTeste += Linhas[EstacaoAdj[2]]-(HorarioAtual+4)%Linhas[EstacaoAdj[2]]
                elif HorarioAtual%Linhas[EstacaoAdj[2]] != 0:
                    CaminhoTeste += Linhas[EstacaoAdj[2]]-HorarioAtual%Linhas[EstacaoAdj[2]]
                HorarioTeste = CaminhoTeste
                if EstacaoAdj[0] == EstacaoDestino:
                    Caminho.append(EstacaoAdj[0])
                    return HorarioAtual + HorarioTeste
                CaminhoTeste += (DistanciaReta[int(EstacaoAdj[0][1:])-1][int(EstacaoDestino[1:])-int(EstacaoAdj[0][1:])-1])*3/2 if int(EstacaoAdj[0][1:]) < int(EstacaoDestino[1:]) else (DistanciaReta[int(EstacaoDestino[1:])-1][int(EstacaoAdj[0][1:])-int(EstacaoDestino[1:])-1])*3/2
                if CaminhoTeste < MenorCaminho:
                    MenorCaminho = CaminhoTeste
                    MelhorHorario = HorarioAtual + HorarioTeste
                    ProxEstacao = EstacaoAdj[0]
                    LinhaEstacao = EstacaoAdj[2]
        # print('Trajeto {} - {} // Entrada {}:{} - Chegada {}:{}'.format(EstacaoAtual, ProxEstacao, str(int(HorarioAtual//60)+4).zfill(2), str(round(HorarioAtual%60)).zfill(2), str(int(MelhorHorario//60)+4).zfill(2), str(round(MelhorHorario%60)).zfill(2)))
        return a_star(ProxEstacao, EstacaoDestino, MelhorHorario, LinhaEstacao)

    ETA = a_star(Origem, Destino, Horario, 0)
    ETA -= 1440 if ETA >= 1200 else 0
    print('Seu ETA e {}:{}, seu caminho e {}'.format(str(int(ETA//60)+4).zfill(2), str(round(ETA%60)).zfill(2), ' '.join(Caminho)))
