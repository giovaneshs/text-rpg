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
        print()

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

def jogo_verdadeiro_falso():
    pass

def jogo_adivinhar():
    pass

def jogo_associar_conceitos():
    pass

def decididor_final(compreensao):
    if len(compreensao) <= 7:
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

    if len(compreensao) > 7 and len(compreensao) <= 14:
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

    if len(compreensao) > 14 and len(compreensao) <=22:
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