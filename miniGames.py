import curses
import random
import time

def getForca(tentativas):
    forca = [
        [
        '   ------',
        '   |    |',
        '   |     ',
        '   |     ',
        '   |     ',
        '   |     ',
        '---|---  '
        ],
        [
        '   ------  ',
        '   |    |  ',
        '   |    O  ',
        '   |       ',
        '   |       ',
        '   |       ',
        '---|---    '
        ],
        [
        '   ------  ',
        '   |    |  ',
        '   |    O  ',
        '   |    |  ',
        '   |       ',
        '   |       ',
        '---|---    '
        ]
        ,
        [
        '   ------  ',
        '   |    |  ',
        '   |    O  ',
        '   |   /|  ',
        '   |       ',
        '   |       ',
        '---|---    '
        ]
        ,
        [
        '   ------  ',
        '   |    |  ',
        '   |    O  ',
        '   |   /|\\',
        '   |       ',
        '   |       ',
        '---|---    '
        ]
        ,
        [
        '   ------  ',
        '   |    |  ',
        '   |    O  ',
        '   |   /|\\',
        '   |   /   ',
        '   |       ',
        '---|---    '
        ]
        ,
        [
        '   ------  ',
        '   |    |  ',
        '   |    O  ',
        '   |   /|\\',
        '   |   / \\',
        '   |       ',
        '---|---    '
        ]
    ]
    return forca[tentativas]


def jogar_forca(compreensao,stdscr):
    palavra = "anomia"
    palavra_oculta = ['_'] * len(palavra)
    letras_erradas = []
    tentativas = 0
    max_tentativas = 6

    forca_win = curses.newwin(10, 15, 8, 50)
    dica_win = curses.newwin(2, 90 ,2, 20)
    input_win = curses.newwin(2,20,18,30)
    mensagem_win = curses.newwin(2,80,4,35)
    palavra_oculta_win = curses.newwin(2,15,18,60)
    letras_erradas_win = curses.newwin(4,70, 23, 30)


    while True:

        dica_win.clear()
        dica_win.addstr('"Uma condição de desordem social resultante da falta de normas ou regras claras."')
        dica_win.refresh()

        desenho = getForca(tentativas)
        forca_win.clear()
        forca_win.addstr(1,1, desenho[0])
        forca_win.addstr(2,1, desenho[1])
        forca_win.addstr(3,1, desenho[2])
        forca_win.addstr(4,1, desenho[3])
        forca_win.addstr(5,1, desenho[4])
        forca_win.addstr(6,1, desenho[5])
        forca_win.addstr(7,1, desenho[6])
        forca_win.refresh()

        palavra_oculta_win.clear()
        palavra_oculta_win.addstr(" ".join(palavra_oculta))
        palavra_oculta_win.refresh()

        letras_erradas_win.clear()
        letras_erradas_win.addstr("Letras erradas: " + ", ".join(letras_erradas))
        letras_erradas_win.refresh()

        input_win.clear()
        input_win.addstr("Digite uma letra:")
        input_win.refresh()

        if tentativas == max_tentativas:
            time.sleep(0.5)
            stdscr.clear()
            stdscr.border()
            stdscr.addstr(14, 35, "Você perdeu! A palavra correta era: {}".format(palavra))
            stdscr.refresh()
            botao = curses.newwin(1, 15, 24, 85)
            botao.addstr("[E]Próximo")
            botao.refresh()
            while True:
                key = stdscr.getkey()

                match key.upper():
                    case "E":
                        break
            stdscr.clear()
            break
        
        
        letra = stdscr.getkey().lower()
    

        if letra.lower() in letras_erradas or letra.lower() in palavra_oculta:
            mensagem_win.clear()
            mensagem_win.addstr("Você já tentou essa letra. Tente novamente.")
            mensagem_win.refresh()
            continue


        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
                    palavra_oculta_win.clear()
                    palavra_oculta_win.addstr(" ".join(palavra_oculta))
                    palavra_oculta_win.refresh()
        else:
            letras_erradas.append(letra)
            letras_erradas_win.clear()
            letras_erradas_win.addstr("Letras erradas: " + ", ".join(letras_erradas))
            letras_erradas_win.refresh()
            tentativas += 1


        if "_" not in palavra_oculta:
            time.sleep(0.5)
            stdscr.clear()
            stdscr.border()
            stdscr.addstr(14, 35, "Parabéns! Você acertou a palavra: {}".format(palavra))
            stdscr.refresh()

            compreensao.append(1)
            compreensao.append(1)
            compreensao.append(1)
            compreensao.append(1)

            botao = curses.newwin(1, 15, 24, 85)
            botao.addstr("[E]Próximo")
            botao.refresh()
            while True:
                key = stdscr.getkey()

                match key.upper():
                    case "E":
                        break
            stdscr.clear()
            break

def jogo_verdadeiro_falso(afirmacoes, compreensao,stdscr):
    respostas_corretas = [False, True, True, False]  # Respostas corretas para cada afirmação

    for i, afirmacao in enumerate(afirmacoes):
        title_win = curses.newwin(1,40,2,48)
        afirmacao_win = curses.newwin(3,95, 8,24)
        verdadeiro_win = curses.newwin(3,14, 15,40)
        falso_win = curses.newwin(3,11, 15, 65)
        legenda = curses.newwin(1, 35, 25, 70)
    
        title_win.addstr('[Verdadeiro ou Falso]')
        title_win.refresh()
    
        verdadeiro_win.addstr(1, 1, " Verdadeiro ", curses.A_STANDOUT)
    
        falso_win.addstr(1, 2, " Falso ", curses.A_BOLD)

        verdadeiro_win.refresh()
        falso_win.refresh()

        afirmacao_win.clear()
        afirmacao_win.addstr(1,0,f"Afirmação {i + 1}: {afirmacao}")
        afirmacao_win.refresh()

        legenda.addstr("[SETAS]Mover   [E]Selecionar")
        legenda.refresh()
        
        resposta_usuario = 'v'

        while True:
            key = stdscr.getkey().lower()
            match key.upper():
                case "KEY_RIGHT":
                    resposta_usuario = 'f'
                    verdadeiro_win.clear()
                    verdadeiro_win.addstr(1, 1, " Verdadeiro ", curses.A_BOLD)
                    falso_win.clear()
                    falso_win.addstr(1, 2, " Falso ", curses.A_STANDOUT)
                    verdadeiro_win.refresh()
                    falso_win.refresh()

                case "KEY_LEFT":
                    resposta_usuario = 'v'
                    verdadeiro_win.clear()
                    verdadeiro_win.addstr(1, 1, " Verdadeiro ", curses.A_STANDOUT)
                    falso_win.clear()
                    falso_win.addstr(1, 2, " Falso ", curses.A_BOLD)
                    verdadeiro_win.refresh()
                    falso_win.refresh()

                case "E":
                    break
        
        if (resposta_usuario == 'v' and respostas_corretas[i]) or (resposta_usuario == 'f' and not respostas_corretas[i]):
            stdscr.clear()
            stdscr.border()
            stdscr.refresh()
            stdscr.addstr(13,48,"Resposta correta!")
            stdscr.refresh()
            time.sleep(2)
            compreensao.append(1)
            stdscr.clear()
            stdscr.border()
            stdscr.refresh()
        else:
            stdscr.clear()
            stdscr.border()
            stdscr.refresh()
            if resposta_usuario == "v":
                stdscr.addstr(13,30,"Resposta incorreta. A resposta correta é: Falso")
                stdscr.refresh()
            else:
                stdscr.addstr(13,30,"Resposta incorreta. A resposta correta é: Verdadeiro")
                stdscr.refresh()
            time.sleep(2)
            stdscr.clear()
            stdscr.border()
            stdscr.refresh()

def escolher_conceito(conceitos):
    return random.choice(conceitos)

def dar_dica(conceito):
    # Gera uma dica com base no conceito escolhido
    if conceito[0] == "Solidariedade Mecânica":
        return  ('Neste tipo de solidariedade, os membros da sociedade têm valores e crenças\n'
                'muito semelhantes.')
    elif conceito[0] == "Consciência Coletiva":
        return ('Refere-se ao conjunto de crenças, valores e normas que são compartilhados\n'
               'por uma sociedade.')
    elif conceito[0] == "Fato Social":
        return ('Para Durkheim, são maneiras de agir, pensar e sentir que exercem controle\n'
                'sobre os indivíduos.')
    elif conceito[0] == "Anomia":
        return ('É uma condição de desordem social resultante da falta de normas ou regras\n'
                'claras.')

def jogo_adivinhar(compreensao, conceitos, stdscr):
    conceito_atual = escolher_conceito(conceitos)
    dica_atual = dar_dica(conceito_atual)

    legenda = curses.newwin(1, 35, 25, 70)
    

    tentativas = 3
    while True:
        legenda = curses.newwin(1, 35, 25, 70)
        title_win = curses.newwin(1,40,2,48)
        dica_win = curses.newwin(3,90, 8,16)
        enunciado_win = curses.newwin(1,45, 12,16)
        opcao1_win = curses.newwin(1,24, 14, 45)
        opcao2_win = curses.newwin(1, 22, 16, 46)
        opcao3_win = curses.newwin(1, 13, 18, 50)
        opcao4_win = curses.newwin(1, 8, 20, 52)
        contador_win = curses.newwin(1,25,24,16)

        legenda.addstr("[SETAS]Mover   [E]Selecionar")
        legenda.refresh()

        title_win.addstr("[Jogo do Conceito]")
        title_win.refresh()

        dica_win.addstr(f"Dica: {dica_atual}")
        dica_win.refresh()

        enunciado_win.addstr("Qual conceito Durkheim está sendo descrito?")
        enunciado_win.refresh()

        contador_win.clear()
        contador_win.addstr(f"Tentativas restantes: {tentativas}")
        contador_win.refresh()

        opcao1_win.addstr("Solidariedade Mecânica", curses.A_STANDOUT)
        opcao1_win.refresh()
        opcao2_win.addstr("Consciência Coletiva", curses.A_BOLD)
        opcao2_win.refresh()
        opcao3_win.addstr("Fato Social", curses.A_BOLD)
        opcao3_win.refresh()
        opcao4_win.addstr("Anomia", curses.A_BOLD)
        opcao4_win.refresh()             

        resposta = ""
        option = 1
        while True:
            match option:
                case 1:
                    opcao1_win.clear()
                    opcao1_win.addstr("Solidariedade Mecânica", curses.A_STANDOUT)
                    opcao1_win.refresh()

                    opcao2_win.clear()
                    opcao2_win.addstr("Consciência Coletiva", curses.A_BOLD)
                    opcao2_win.refresh()
                    
                    opcao3_win.clear()
                    opcao3_win.addstr("Fato Social", curses.A_BOLD)
                    opcao3_win.refresh()
                    
                    opcao4_win.clear()
                    opcao4_win.addstr("Anomia", curses.A_BOLD)
                    opcao4_win.refresh()
                case 2:
                    opcao1_win.clear()
                    opcao1_win.addstr("Solidariedade Mecânica", curses.A_BOLD)
                    opcao1_win.refresh()
                    
                    opcao2_win.clear()
                    opcao2_win.addstr("Consciência Coletiva", curses.A_STANDOUT)
                    opcao2_win.refresh()
                    
                    opcao3_win.clear()
                    opcao3_win.addstr("Fato Social", curses.A_BOLD)
                    opcao3_win.refresh()
                    
                    opcao4_win.clear()
                    opcao4_win.addstr("Anomia", curses.A_BOLD)
                    opcao4_win.refresh()
                
                case 3:
                    opcao1_win.clear()
                    opcao1_win.addstr("Solidariedade Mecânica", curses.A_BOLD)
                    opcao1_win.refresh()
                    
                    opcao2_win.clear()
                    opcao2_win.addstr("Consciência Coletiva",curses.A_BOLD)
                    opcao2_win.refresh()
                    
                    opcao3_win.clear()
                    opcao3_win.addstr("Fato Social", curses.A_STANDOUT)
                    opcao3_win.refresh()
                    
                    opcao4_win.clear()
                    opcao4_win.addstr("Anomia", curses.A_BOLD)
                    opcao4_win.refresh()

                case 4:
                    opcao1_win.clear()
                    opcao1_win.addstr("Solidariedade Mecânica", curses.A_BOLD)
                    opcao1_win.refresh()
                    
                    opcao2_win.clear()
                    opcao2_win.addstr("Consciência Coletiva", curses.A_BOLD)
                    opcao2_win.refresh()
                    
                    opcao3_win.clear()
                    opcao3_win.addstr("Fato Social", curses.A_BOLD)
                    opcao3_win.refresh()
                    
                    opcao4_win.clear()
                    opcao4_win.addstr("Anomia", curses.A_STANDOUT)
                    opcao4_win.refresh()

            key = stdscr.getkey()
            match key.upper():
                case "KEY_DOWN":
                    option += 1
                    if option >= 4:
                        option = 4

                case "KEY_UP":
                    option -= 1
                    if option <= 1:
                        option = 1

                case "E":
                    if option == 1:
                        resposta = "Solidariedade Mecânica"
                        break
                    elif option == 2:
                        resposta = "Consciência Coletiva"
                        break
                    elif option == 3:
                        resposta = "Fato Social"
                        break
                    elif option == 4:
                        resposta = "Anomia"
                        break

        if resposta == conceito_atual[0]:
            stdscr.clear()
            stdscr.border()
            stdscr.refresh()
            stdscr.addstr(14, 30,f"Parabéns! Você acertou! O conceito era:{conceito_atual[0]}")
            stdscr.refresh()
            compreensao.append(1)
            compreensao.append(1)
            compreensao.append(1)
            compreensao.append(1)
            break
        else:
            tentativas -= 1
            if tentativas == 0:
                stdscr.clear()
                stdscr.border()
                stdscr.refresh()
                stdscr.addstr(14, 25,f"Você excedeu o número máximo de tentativas. O conceito era: {conceito_atual[0]}")
                stdscr.refresh()
                break
            else:
                stdscr.clear()
                stdscr.border()
                stdscr.refresh()
                stdscr.addstr(14, 48,"Tente novamente!")
                stdscr.refresh()
    
    stdscr.clear()
    

def jogo_associar_conceitos():
    pass

def decididor_final(compreensao):
    if len(compreensao) <= 6:
        texto = (
            'Diante das ideias de Durkheim, sua compreensão é limitada, resultando em ações\n'
            'isoladas e esforços superficiais para aliviar a anomia no trabalho. Você tenta, mas a\n'
            'verdadeira natureza do problema permanece obscurecida. Suas ações têm impacto\n'
            'mínimo, e a sociedade continua a enfrentar desafios significativos na coesão social.\n\n'
            'Compreendendo apenas superficialmente o poder da solidariedade, você realiza\n'
            'ações isoladas para abordar problemas no trabalho. Seus esforços são limitados em\n'
            'escopo, e embora haja algumas melhorias percebidas, a anomia persiste. A\n'
            'compreensão limitada resulta em transformações mínimas, e a coesão social\n'
            'continua a ser um desafio não resolvido.\n'
        )
        return texto

    if len(compreensao) > 6 and len(compreensao) <= 12:
        texto2 = (
            'Ao compreender parcialmente as ideias de Durkheim, você sente a urgência de\n'
            'mudança, mas suas ações são mais moderadas. Colabora com alguns colegas na\n'
            'busca por melhorias nas condições de trabalho, embora a compreensão total das\n'
            'causas subjacentes da anomia escape. Enquanto algumas melhorias são notadas, o\n'
            'impacto transformador é limitado, e a sociedade continua a enfrentar desafios na\n'
            'coesão social.\n\n'
            'Compreendendo em parte o poder da solidariedade, você se une a alguns colegas\n'
            'para abordar os problemas no ambiente de trabalho. Juntos, fazem progressos\n'
            'modestos na melhoria das condições, mas a verdadeira raiz da anomia ainda não é\n'
            'totalmente compreendida. Embora haja melhorias, a transformação social é apenas\n'
            'parcialmente alcançada, deixando desafios persistentes.\n'
        )
        return texto2

    if len(compreensao) > 12 and len(compreensao) <=22:
        texto3 = (
            'Inspirado por essa nova perspectiva, você se une a outros operários para romper as\n'
            'correntes da anomia no trabalho. Juntos, buscam melhorar as condições laborais,\n'
            'fortalecendo o tecido social e propagando a importância de cada indivíduo na\n'
            'sociedade. A transformação é palpável, e uma nova era de coesão social começa a\n'
            'se desenhar.\n\n'
            'Compreendendo o poder da solidariedade, você se une a seus colegas para\n'
            'transcender os limites da anomia no trabalho. Juntos, iniciam uma jornada de\n'
            'transformação, fortalecendo os laços sociais e promovendo uma nova consciência.\n'
            'A sociedade, antes marcada pela desconexão, floresce em uma nova era de coesão\n'
            'e propósito compartilhado.\n'
        )
        return texto3