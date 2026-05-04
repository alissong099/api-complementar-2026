def main():
    respondentes = qtd_respondentes()
    respostas = obter_respostas(respondentes)
    
def qtd_respondentes():
    try:
        qtd_respondentes = int(input('Informe a quantia de respondentes: '))
        return qtd_respondentes
    except ValueError:
        print('Erro! Por favor insira uma quantia valida!')
        return qtd_respondentes()
    

def verificar_resposta(p):
    try:
        resposta = int(input(p))
        if resposta != 0 and resposta != 1 and resposta != 2 and resposta != 3 and resposta != 4 and resposta != 5 and resposta != 6:
            return False
    except ValueError:
        print('Escolha inválida! Por favor escolha uma das opções disponivéis.')


def obter_respostas(qtd_resp):
    if qtd_resp < 0:
        return 'Ainda não há nenhum respondente para avaliação.'
    
    resposta = ''
    
    for i in range(qtd_resp):
        nome = input('Informe o seu nome -> ')
        informacao = 'Escolha uma resposta de acordo com o que você mais se identificar na pergunta. Escala de respostas:\n'
        print(informacao)
        
        escala_respostas = '''0 = Nunca 1 = Raramente 2 = Às vezes 3 = Regularmente 4 = Frequentemente 5 = Quase sempre 6 = Sempre \n'''
        print(escala_respostas)

        print('Dimensão 1 — Exaustão Emocional\n')
        pergunta_1 = '1. Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho. \n'
        resposta_1 = verificar_resposta(pergunta_1)
        if resposta_1 == False:
            print('Resposta inválida. Responda novamente:\n')
            pergunta_1 = '1. Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho. \n'
            resposta_1 = verificar_resposta(pergunta_1)

        pergunta_2 = '2. Sinto-me esgotado(a) ao final de um dia de estudos/trabalho. \n'
        resposta_2 = verificar_resposta(pergunta_2)
        if resposta_2 == False:
            print('Resposta inválida. Responda novamente:\n')
            pergunta_2 = '1. Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho. \n'
            resposta_2 = verificar_resposta(pergunta_2)
        
        pergunta_3 = '3. Acordar de manhã e ter que enfrentar mais um dia me causa cansaço. \n'
        resposta_3 = verificar_resposta(pergunta_3)
        if resposta_3 == False:
            print('Resposta inválida. Responda novamente:\n')
            pergunta_3 = '1. Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho. \n'
            resposta_3 = verificar_resposta(pergunta_3)
        
        escala_respostas = '''0 = Nunca 1 = Raramente 2 = Às vezes 3 = Regularmente 4 = Frequentemente 5 = Quase sempre 6 = Sempre \n'''
        print(escala_respostas)

        print('Dimensão 2 — Despersonalização\n')
        pergunta_4 = '4. Sinto que me tornei mais indiferente com as pessoas ao meu redor. \n'
        resposta_4 = verificar_resposta(pergunta_4)
        if resposta_4 == False:
            print('Resposta inválida. Responda novamente:\n')
            pergunta_4 = '1. Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho. \n'
            resposta_4 = verificar_resposta(pergunta_4)
        
        pergunta_5 = '5. Tenho me preocupado menos com o impacto do meu trabalho/estudo nas pessoas. \n'
        resposta_5 = verificar_resposta(pergunta_5)
        if resposta_5 == False:
            print('Resposta inválida. Responda novamente:\n')
            pergunta_5 = '1. Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho. \n'
            resposta_5 = verificar_resposta(pergunta_5)
        
        pergunta_6 = '6. Sinto que as pessoas ao meu redor me culpam por alguns dos seus problemas. \n'
        resposta_6 = verificar_resposta(pergunta_6)
        if resposta_6 == False:
            print('Resposta inválida. Responda novamente:\n')
            pergunta_6 = '1. Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho. \n'
            resposta_6 = verificar_resposta(pergunta_6)
        
        escala_respostas = '''0 = Nunca 1 = Raramente 2 = Às vezes 3 = Regularmente 4 = Frequentemente 5 = Quase sempre 6 = Sempre \n'''
        print(escala_respostas)

        print('Dimensão 3 — Realização Pessoal\n')
        pergunta_7 = '7. Consigo lidar eficazmente com os problemas que surgem no meu dia a dia. \n'
        resposta_7 = verificar_resposta(pergunta_7)
        if resposta_7 == False:
            print('Resposta inválida. Responda novamente:\n')
            pergunta_7 = '1. Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho. \n'
            resposta_7 = verificar_resposta(pergunta_7)
        
        pergunta_8 = '8. Sinto que estou tendo uma influência positiva na vida das pessoas. \n'
        resposta_8 = verificar_resposta(pergunta_8)
        if resposta_8 == False:
            print('Resposta inválida. Responda novamente:\n')
            pergunta_8 = '1. Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho. \n'
            resposta_8 = verificar_resposta(pergunta_8)
        
        pergunta_9 = '9. Sinto-me estimulado(a) após trabalhar ou estudar com outras pessoas. \n'
        resposta_9 = verificar_resposta(pergunta_9)
        if resposta_9 == False:
            print('Resposta inválida. Responda novamente:\n')
            pergunta_9 = '1. Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho. \n'
            resposta_9 = verificar_resposta(pergunta_9)
        
        
    return resposta_1, resposta_2, resposta_3, resposta_4, resposta_5, resposta_6, resposta_7, resposta_8, resposta_9


def calcular_escores(r1, r2, r3, r4, r5, r6, r7, r8, r9):
    media_dimensao_1 = r1 + r2 + r3 / 3
    media_dimensao_2 = r4 + r5 + r6 / 3
    media_dimensao_3 = r7 + r8 + r9 / 3

    return media_dimensao_1, media_dimensao_2, media_dimensao_3


def classificar_dimensao(m1, m2, m3):
    exaustao_emocional = ''
    despersonalizacao = ''
    realizacao = ''
    
    moderado = 0
    alto = 0
    baixo = 0
    
    total_baixo = 0
    total_moderado = 0
    total_alto = 0
    
    if m1 <= 2.0:
        exaustao_emocional = 'Baixo ✅'
    elif m1 <= 3.9:
        exaustao_emocional = 'Moderado ⚠️'
        total_moderado += 1
    elif m1 <= 6.0:
        exaustao_emocional = 'Alto 🔴'
        total_alto += 1
    
    if m2 <= 2.0:
        despersonalizacao = 'Baixo ✅'
    elif m2 <= 3.9:
        despersonalizacao = 'Moderado ⚠️'
        total_moderado += 1
    elif m2 <= 6.0:
        despersonalizacao = 'Alto 🔴'
        total_alto += 1
    
    if m3 <= 2.0:
        realizacao = 'Alta ✅'
    elif m3 <= 3.9:
        realizacao = 'Moderada ⚠️'
        total_moderado += 1
    elif m3 <= 6.0:
        realizacao = 'Baixa 🔴'
        total_alto += 1

    return exaustao_emocional, despersonalizacao, realizacao, alto, moderado, baixo, total_alto, total_moderado


def exibir_laudo(m1, m2, m3, ex, des, real, nome, total_al, total_mod, res):
    laudo_individual = f'''========== LAUDO: {nome} ==========
    Exaustão Emocional : {m1} → {ex}
    Despersonalização  : {m2} → {des}
    Realização Pessoal : {m3} → {real}'''

    if total_al > 0:
        laudo_individual += f'''\n ⚠️ Atenção: {total_al} dimensão(ões) em nível crítico.\n Recomenda-se acompanhamento profissional.'''
    elif total_mod > 0:
        laudo_individual += f'''\n ⚠️ Atenção: {total_mod} dimensão(ões) em nível crítico.\n Recomenda-se acompanhamento profissional.'''
    else:
        laudo_individual += f'''\n Parabéns: {total_al} dimensão(ões) em nível crítico.'''
    
    resumo = f'''======= RESUMO DO ESTUDO =======
    Respondentes        : {res}
    Maior Exaustão      : {}
    Menor Realização    : {}
    Média Geral Burnout : {}'''

main()