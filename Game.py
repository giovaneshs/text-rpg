import curses
import time


def Diario(texto, stdscr):
    diario = curses.newpad(100, 100)
    diario.clear()

    digitacao = 0
    lineCounter = 0
    startLine = 0
    while digitacao < len(texto):
        stdscr.getch()
        if (digitacao + 5) >= len(texto):
            digitado = texto[digitacao:]
        else:
            digitado = texto[digitacao:digitacao + 5]
        
        diario.addstr(digitado)

        if lineCounter >= 20:
            lineCounter -= 1
            startLine +=1
    
        diario.refresh(startLine, 0, 4, 15, 23, 100)

        lineCounter += digitado.count("\n")
        digitacao += 5


    botao = curses.newwin(1, 15, 24, 85)
    botao.addstr("[E]Próximo")
    botao.refresh()
    while True:
        key = stdscr.getkey()

        match key.upper():
            case "E":
                break
    stdscr.clear()

def Carta(texto, stdscr):
    carta = curses.newpad(100, 100)
    carta.clear()
 
    carta.addstr(texto, curses.A_ITALIC)

    carta.refresh(0, 0, 4, 15, 23, 100)
    #botao = curses.newwin(1, 15, 24, 85)
    #botao.addstr("[E]Próximo")

    startLine = 0
    finalLine = 20
    lineCounter = texto.count("\n")
    
    while True:
        key = stdscr.getkey()

        match key.upper():

            case "KEY_DOWN":
                startLine +=1
                if startLine >= lineCounter - 20:
                    startLine = lineCounter - 20
                finalLine +=1
                if finalLine >= lineCounter:
                    finalLine = lineCounter
                carta.refresh(startLine, 0, 4, 15, 23, 100)
                if finalLine == lineCounter:
                    botao = curses.newwin(1, 15, 24, 85)
                    botao.addstr("[E]Próximo")
                    botao.refresh()
            case "KEY_UP":
                startLine -=1
                if startLine < 0:
                    startLine = 0
                carta.refresh(startLine, 0, 4, 15, 23, 100)

            case "E":
                break
    stdscr.clear()


def Game(stdscr):
    stdscr.clear()
    stdscr.border()
    stdscr.refresh()

    time.sleep(1)
    stdscr.addstr(10, 40, "             ▄▄                   ")
    stdscr.addstr(11, 40, "▀███▀▀▀██▄   ██                   ")
    stdscr.addstr(12, 40, "  ██    ▀██▄                 ▄▄▄  ")
    stdscr.addstr(13, 40, "  ██     ▀█████  ▄█▀██▄     ▀███  ")
    stdscr.addstr(14, 40, "  ██      ██ ██ ██   ██       ██  ")
    stdscr.addstr(15, 40, "  ██     ▄██ ██  ▄█████       ██  ")
    stdscr.addstr(16, 40, "  ██    ▄██▀ ██ ██   ██       ██  ")
    stdscr.addstr(17, 40, "▄████████▀ ▄████▄████▀██▄   ▄████▄")
    stdscr.refresh()
    
    time.sleep(2)
    stdscr.clear()

    
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()

    
    mensagem.clear()

    diario1 = (
    'Querido diário,\n\n'
    'Hoje eu tive minha rotina diária como normalmente. Acordo, como o que tiver na\ngeladeira de café da manhã, me arrumo com minhas roupas usuais e saio de casa\nem direção ao meu trabalho.\n\n'
    'Andei pela rua, de cabeça baixa, evitando olhares a outras pessoas, meu foco agora\nera realizar meu trabalho e nada mais… Após algumas quadras cheguei no\nestabelecimento na qual passaria minhas próximas horas, realizei várias tarefas,\nalgumas fazia constantemente, limpar, organizar, outras tive que fazer hoje por falta\nde gente, como cozinhar, consegui realizar as tarefas suficientemente, finalizei o dia\nrealizada com meu desempenho hoje.\n\n'
    'Depois da minha jornada de trabalho, deixava meu cartão em cima da bancada\ncomo de costume e segui o caminho para a minha casa com os olhos ao chão.\n\n'
    'Após a segunda esquina, eu entrei em um estabelecimento e deixei meu dinheiro na\nbancada… depois de 5 minutos eu recebi um pão.\n\n'
    'Saindo do local, voltei ao meu caminho usual, comendo meu pão até minha casa.\n\n'
    'Ao chegar em casa, tive uma surpresa ao ver que tinha algo fora do lugar, bem ao\ncentro da minha visão onde entraria na minha residência, havia uma carta jogada\nem frente a minha porta\n\n'
    'Então, entrei em minha casa e, quebrando minha rotina, comecei a ler a misteriosa \ncarta'
    )

    Diario(diario1,stdscr)
    stdscr.border()
    stdscr.refresh()

    time.sleep(0.5)

    carta1 = (
    'Querida Remetente,\n\n'
    'Esperamos que esta carta encontre você bem. Somos um grupo SKT e, através\ndestas linhas, trazemos notícias de um lugar distante, além das muralhas que\ncircundam sua rotina diária. Aqui, as ruas são tecidas com diversas funções, onde a\nautonomia e cooperação regem o trabalho. Não há correntes que prendem os\nsonhos nem limites para a expressão do ser individual.\n\n'
    'Neste mundo, cada passo é uma escolha, cada trabalho e interação é uma sinfonia\nde conexões. Aqui, a solidariedade não é apenas uma teoria, mas sim uma\ninterdependência vívida do nosso dia a dia. Observamos seu mundo através das\nfrestas, onde suas regras aprisionam potenciais, sufocam desejos e moldam vidas\nem um padrão inflexível.\n\n'
    'Escrevemos para você, não apenas como um mensageiro, mas como um convite\npara enxergar além das paredes que cercam sua existência. Há um universo\nesperando por você, onde cada ação é uma nota em sua própria sinfonia de\nEquilíbrio Social.\n\n'
    'Se estiver disposta, responda-me. Compartilharemos mais sobre este nosso lugar.\n\n'
    'Com esperança, Grupo SKT"\n'
    )
    
    Carta(carta1, stdscr)
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario11 = (
    'Eu logo estranhei toda essa conversa, não é nem de perto algo que eu tenha\n'
    'contato… parece mais uma descrição de uma utopia do que realmente uma outra\n'
    'sociedade, mas me deixou intrigada mesmo assim…\n'
    )

    Diario(diario11,stdscr)
    stdscr.border()
    stdscr.refresh()

    diario12 = (
        'Prezado Grupo SKT,\n\n'
        'Agradeço imensamente pelas palavras gentis e pelo convite generoso para\ncompartilhar sua realidade além das muralhas.\n\n'
        'No entanto, enquanto aprecio profundamente a oferta e admiro o que seu grupo\nrepresenta, devo confessar que minha própria realidade é bastante distante desse\npanorama tão inspirador que vocês descrevem. Em meu trabalho, cada tarefa é\nexecutada momentâneamente, com o que é preciso, não vejo como essa divisão\npossa ser benéfica.\n\n'
        'As paredes que cercam minha existência são feitas não apenas de concreto, mas\npara me proteger, não vejo elas sendo de algum malefício algum. É difícil vislumbrar\ncomo poderia contribuir para algo tão presente na sociedade quanto o que vocês\ncompartilham, dado o contexto em que estou inserida.\n\n'
        'Agradeço novamente pelo convite e pela oportunidade de conhecer um pouco mais\nsobre o que está além dessas paredes. Apesar de não conseguir participar\nativamente, guardarei com carinho as visões que vocês trouxeram para minha vida,\nmantendo viva a esperança de que um dia.\n\n'
        'Com apreço e respeito,\n'
        'Emily\n'
    )

    Diario(diario12,stdscr)
    stdscr.border()
    stdscr.refresh()
    
    diario13 = (
        'Com certa desconfiança e estranheza com as informações da carta, passo o\nrestante do meu dia refletindo sobre esse "diferente mundo" citado na mensagem\n'
        'Ao anoitecer, deito em minha cama e sigo com os vagos pensamentos. O melhor a\nse fazer é dormir…\n'
    )
    
    Diario(diario13,stdscr)
    
    stdscr.border()
    stdscr.refresh()

    time.sleep(1)
    stdscr.addstr(10, 40, "             ▄▄                     ")
    stdscr.addstr(11, 40, "▀███▀▀▀██▄   ██                     ")
    stdscr.addstr(12, 40, "  ██    ▀██▄                        ")
    stdscr.addstr(13, 40, "  ██     ▀█████  ▄█▀██▄      ███▀██▄")
    stdscr.addstr(14, 40, "  ██      ██ ██ ██   ██     ███   ██")
    stdscr.addstr(15, 40, "  ██     ▄██ ██  ▄█████         ▄▄██")
    stdscr.addstr(16, 40, "  ██    ▄██▀ ██ ██   ██      ▄▄█▀   ")
    stdscr.addstr(17, 40, "▄████████▀ ▄████▄████▀██▄   ████████")
    stdscr.refresh()
    
    time.sleep(2)
    stdscr.clear()
    stdscr.border()

    diario2 = (
        'Querido diário,\n\n'
        'O melhor que eu poderia ter feito era dormir, mas devo dizer que não consegui ter o\nmelhor dos sonos durante a última noite, essa carta me fez pensar: de onde surgiu\nesse grupo e que raios de sociedade é essa que descreveram? Nunca vi nenhum\ncolega de trabalho meu ter autonomia, apenas recebemos ordens e seguimos,\ncomo sempre fomos ensinados que é o correto.\n\n'
        'Mas devo dizer que estaria mentindo se escrevesse que não tenho interesse nesse\ntal mundo dito para mim, “um convite para enxergar além das paredes”, eu nunca\nparei para pensar no que há além das paredes - se existe algo - sempre pensei que\nas paredes foram feitas para nos proteger da ameaça exterior.\n\n'
        'Será que estão sufocando um desejo que eu nunca sabia que tinha? Eu apenas sei\nque preciso parar de escrever isso e ir trabalhar.\n\n'
        'Então continuei minha rotina diária como normalmente. Acordo, como o que tenho\nna geladeira de café da manhã, me arrumo com minhas roupas usuais e saio de\ncasa em direção ao meu trabalho.\n\n'                                                                                                                                                 
        'As ruas passam normalmente, mesmo com essa carta em minha mente, tudo\nparece mais do usual…\n\n'
        'Ao chegar no estabelecimento de trabalho, eu tento fazer algo em relação ao que\nfalaram na carta, talvez se eu focar em fazer só a parte de organização… vamos\nver…\n'
    )

    Diario(diario2,stdscr)
    stdscr.border()
    stdscr.refresh()

    diario22 = (
        'Ao fim do expediente, comecei a guardar minhas coisas e me direcionar para casa,\nporém me senti muito mais realizada… talvez esse grupo saiba de alguma coisa…\n\n'
        'Me direcionei para casa normalmente, mas parecia mais leve… não sei como\ndescrever, peguei meu pão como de costume e segui caminho.\n\n'
        'Chegando em casa me deparei com outra carta, ansiosamente, adentrei a minha\nresidência e comecei a ler…\n'
    )

    Diario(diario22,stdscr)
    stdscr.border()
    stdscr.refresh()

    carta2 = (
        '"Querida Emily,\n\n'
        'Agradecemos sinceramente por sua resposta atenciosa e por compartilhar seus\npensamentos conosco. Compreendemos suas hesitações diante do que foi descrito\nem nossas cartas, mas permita-nos expressar uma perspectiva alternativa.\n\n'
        'Ao olhar para além das muralhas que circundam sua rotina, vemos um panorama\nem que a solidariedade não é um conceito estranho, mas sim uma realidade\nentrelaçada no tecido de sua própria sociedade. Entendemos que as estruturas\nrígidas muitas vezes obscurecem a visão, mas há uma teia de conexões invisíveis\nque sustentam cada atividade diária.\n\n'
        'Permita-nos sugerir que talvez a solidariedade que buscamos não se manifeste da\nmaneira romântica que descrevemos em nossas cartas. Ela pode residir nos gestos\npequenos e cotidianos, nas funções que desempenhamos para o funcionamento da\nsociedade.\n\n'
        'Em seu mundo, já existem pessoas ao seu redor que contribuem, mesmo que\nsilenciosamente, para tornar a vida mais suportável e confortável. A divisão do\ntrabalho, embora muitas vezes invisível aos olhos desatentos, está presente.\n\nConvidamos você a levantar o rosto, a observar com mais atenção e a reconhecer\nos laços que já existem, os quais formam a base da solidariedade.\n\n'
        'Seu papel pode ser mais significativo do que imagina. Ao reconhecer e valorizar\nessas contribuições, você estará dando passos em direção a uma transformação\nsob as visão autonomia e individualidade.\n\n'
        'Convidamos você a reconsiderar nossa oferta, não como uma mudança drástica,\nmas como um despertar para as possibilidades que já permeiam seu mundo.\n\n'
        'Com esperança,\n'
        'Grupo SKT"\n'
    )

    Carta(carta2, stdscr)
    stdscr.border()
    stdscr.refresh()


    stdscr.getch()