import curses
import time
from miniGames import *

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
    compreensao = []

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

    #Diario(diario1,stdscr)
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
    
    #Carta(carta1, stdscr)
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

    #Diario(diario11,stdscr)
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario12 = (
        'Prezado Grupo SKT,\n\n'
        'Agradeço imensamente pelas palavras gentis e pelo convite generoso para\ncompartilhar sua realidade além das muralhas.\n\n'
        'No entanto, enquanto aprecio profundamente a oferta e admiro o que seu grupo\nrepresenta, devo confessar que minha própria realidade é bastante distante desse\npanorama tão inspirador que vocês descrevem. Em meu trabalho, cada tarefa é\nexecutada momentâneamente, com o que é preciso, não vejo como essa divisão\npossa ser benéfica.\n\n'
        'As paredes que cercam minha existência são feitas não apenas de concreto, mas\npara me proteger, não vejo elas sendo de algum malefício algum. É difícil vislumbrar\ncomo poderia contribuir para algo tão presente na sociedade quanto o que vocês\ncompartilham, dado o contexto em que estou inserida.\n\n'
        'Agradeço novamente pelo convite e pela oportunidade de conhecer um pouco mais\nsobre o que está além dessas paredes. Apesar de não conseguir participar\nativamente, guardarei com carinho as visões que vocês trouxeram para minha vida,\nmantendo viva a esperança de que um dia.\n\n'
        'Com apreço e respeito,\n'
        'Emily\n'
    )

    #Diario(diario12,stdscr)
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)
    
    diario13 = (
        'Com certa desconfiança e estranheza com as informações da carta, passo o\nrestante do meu dia refletindo sobre esse "diferente mundo" citado na mensagem\n'
        'Ao anoitecer, deito em minha cama e sigo com os vagos pensamentos. O melhor a\nse fazer é dormir…\n'
    )
    
    #Diario(diario13,stdscr)
    
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
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario2 = (
        'Querido diário,\n\n'
        'O melhor que eu poderia ter feito era dormir, mas devo dizer que não consegui ter o\nmelhor dos sonos durante a última noite, essa carta me fez pensar: de onde surgiu\nesse grupo e que raios de sociedade é essa que descreveram? Nunca vi nenhum\ncolega de trabalho meu ter autonomia, apenas recebemos ordens e seguimos,\ncomo sempre fomos ensinados que é o correto.\n\n'
        'Mas devo dizer que estaria mentindo se escrevesse que não tenho interesse nesse\ntal mundo dito para mim, “um convite para enxergar além das paredes”, eu nunca\nparei para pensar no que há além das paredes - se existe algo - sempre pensei que\nas paredes foram feitas para nos proteger da ameaça exterior.\n\n'
        'Será que estão sufocando um desejo que eu nunca sabia que tinha? Eu apenas sei\nque preciso parar de escrever isso e ir trabalhar.\n\n'
        'Então continuei minha rotina diária como normalmente. Acordo, como o que tenho\nna geladeira de café da manhã, me arrumo com minhas roupas usuais e saio de\ncasa em direção ao meu trabalho.\n\n'                                                                                                                                                 
        'As ruas passam normalmente, mesmo com essa carta em minha mente, tudo\nparece mais do usual…\n\n'
        'Ao chegar no estabelecimento de trabalho, eu tento fazer algo em relação ao que\nfalaram na carta, talvez se eu focar em fazer só a parte de organização… vamos\nver…\n'
    )

    #Diario(diario2,stdscr)
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario22 = (
        'Ao fim do expediente, comecei a guardar minhas coisas e me direcionar para casa,\nporém me senti muito mais realizada… talvez esse grupo saiba de alguma coisa…\n\n'
        'Me direcionei para casa normalmente, mas parecia mais leve… não sei como\ndescrever, peguei meu pão como de costume e segui caminho.\n\n'
        'Chegando em casa me deparei com outra carta, ansiosamente, adentrei a minha\nresidência e comecei a ler…\n'
    )

    #Diario(diario22,stdscr)
    stdscr.border()
    stdscr.refresh()

    time.sleep(0.5)

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

    #Carta(carta2, stdscr)
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario23 = (
        'Uma teia de conexões? Somos todos bichos presos por uma grande aranha agora?\n'
        'Bem, é inegável dizer que eles possuem uma boa escrita, porém o que mais me\n'
        'intrigou nessa carta é essa “divisão de trabalho” e “solidariedade” que esse grupo\n'
        'tanto fala, realmente, cada pessoa tem seu trabalho, mas como isso nos leva a essa\n'
        'tal grande “teia”?\n\n'
        'Eu provavelmente não vou dormir bem, de novo. Mas antes preciso enviar mais\n'
        'uma resposta para eles.\n'
    )

    #Diario(diario23,stdscr)
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario24 = (
        '"Prezado Grupo SKT,\n\n'
        'Agradeço pela sua carta e pela gentileza ao responder. Suas palavras me intrigam\n'
        'acerca de uma nova perspectiva sobre a sociedade, destacando estas “conexões\n'
        'invisíveis” que nos permeiam. No entanto, ainda tenho muitas dúvidas para\n'
        'compreender esse estilo de mundo que vocês mencionaram.\n\n'
        'Ao olhar ao meu redor, ainda não percebo essas contribuições silenciosas que\n'
        'formam a base da solidariedade, como elas se manifestam no meu dia a dia?\n'
        'Gostaria de pedir a vocês que elaborassem mais sobre essas interações sutis.\n\n'
        'Além disso, ao mencionar a divisão do trabalho, vocês destacaram que ela muitas\n'
        'vezes é invisível aos olhos desatentos. Eu gostaria de entender melhor como essas\n'
        'divisões se desenrolam em minha vida. Quero tentar enxergar essas dinâmicas.\n\n'
        'Continuo com receio em explorar as possibilidades que vocês sugeriram. No\n'
        'entanto, sinto que uma compreensão mais profunda é crucial para que eu possa\n'
        'conhecer um pouco mais desse mundo fora das muralhas que vocês falam.\n\n'
        'Atenciosamente,\n'
        'Emily"\n'
    )


    #Diario(diario24,stdscr)
    stdscr.border()
    stdscr.refresh()

    time.sleep(1)
    stdscr.addstr(10, 40, "             ▄▄                       ")
    stdscr.addstr(11, 40, "▀███▀▀▀██▄   ██                       ")
    stdscr.addstr(12, 40, "  ██    ▀██▄                          ")
    stdscr.addstr(13, 40, "  ██     ▀█████  ▄█▀██▄       ██▀▀█▄  ")
    stdscr.addstr(14, 40, "  ██      ██ ██ ██   ██      ███  ▀██ ")
    stdscr.addstr(15, 40, "  ██     ▄██ ██  ▄█████           ▄██ ")
    stdscr.addstr(16, 40, "  ██    ▄██▀ ██ ██   ██         ▀▀██▄ ")
    stdscr.addstr(17, 40, "▄████████▀ ▄████▄████▀██▄          ██ ")
    stdscr.addstr(18, 40, "                            ███  ▄█▀  ")
    stdscr.addstr(19, 40, "                             █████▀   ")
    stdscr.refresh()


    time.sleep(2)
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario3 = (
        'Querido diário,\n\n'
        'Estou começando a ficar com receio que minha falta de noites de sono comece a\n'
        'afetar meu trabalho, mas também, como não ficar pensando nas possibilidades?\n'
        'Essa questão de todos nós estarmos conectados por meio de “teias”, talvez tenha\n'
        'alguma verdade nisso, afinal, cada dia que eu trabalho em algo diferente, é para\n'
        'melhorar a situação daqueles que necessitam.\n\n'
        'Talvez se eu fizesse apenas uma atividade, faria um trabalho melhor, aliás, talvez\n'
        'todos fariam um trabalho melhor assim.\n'
        'Hora de ir trabalhar.\n'
    )

    #Diario(diario3,stdscr)
    stdscr.clear()
    stdscr.border()
    stdscr.refresh()

    #jogar_forca(compreensao,stdscr)

    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario31 = (
        'Depois do trabalho, organizei os cartões de todos na bancada, para tentar fazer o\n'
        'pessoal perder menos tempo na hora de pegar o seu cartão e segui o caminho para\n'
        'a minha casa com os olhos em frente, tentando apreciar e perceber o mundo a\n'
        'minha volta, um mundo cheio de pessoas assim como eu, fazendo as mesmas\n'
        'rotinas, seguindo o mesmo padrão.\n\n'
        'Voltei ao estabelecimento, dei um “boa noite” para o vendedor e pedi um pão, o\n'
        'estabelecimento possui uma abertura entre a recepção e a cozinha, para passar os\n'
        'pedidos que ficam prontos, então decidi começar a olhar o processo deles até que\n'
        'meu pão fique pronto.\n\n'
        'O que era para ser só uma perda de tempo olhando um pão sendo feito para mim\n'
        'se tornou algo que abriu minha mente, cada um dos membros na cozinha tinha sua\n'
        'função, desde aquele que preparava a carne, aquele que fatiava, aquele que\n'
        'preparava mais pães para pedidos futuros e aquele que limpava os locais e\n'
        'organizava, sem contar com a pessoa na bancada, cada um fazendo sua função\n'
        'que, ao todo, leva ao funcionamento correto do estabelecimento.\n\n'
        'O atendente ainda me deu um pão de cortesia, o agradeci, peguei meus pães e\n'
        'segui no meu caminho usual, comendo um deles até em casa, porém, um pouco\n'
        'mais feliz em ver uma certa arte em um trabalho conjunto.\n\n'
        'Em casa, recebi mais uma carta do grupo...\n'
    )

    #Diario(diario31,stdscr)
    stdscr.border()
    stdscr.refresh()

    time.sleep(0.5)

    carta3 = (
        '"Querida Emily,\n\n'
        'Agradecemos por sua carta e pelo interesse em compreender melhor as nuances da\n'
        'sociedade que mencionamos. É compreensível que as ideias que apresentamos\n'
        'possam parecer abstratas ou difíceis de identificar inicialmente. Permita-nos\n'
        'esclarecer e expandir um pouco mais sobre as conexões invisíveis e a divisão do\n'
        'trabalho.\n\n'
        'Quando falamos sobre contribuições silenciosas, referimo-nos aos gestos cotidianos\n'
        'que muitas vezes passam despercebidos. Pode ser a pessoa que cultiva os\n'
        'alimentos que você consome, o motorista que entrega os produtos que você\n'
        'compra, ou até mesmo alguém que realiza pequenos atos de gentileza para tornar o\n'
        'ambiente ao seu redor mais acolhedor. São essas ações que, quando observadas\n'
        'com atenção, revelam a interconectividade que sustenta a sociedade.\n\n'
        'Quanto à divisão do trabalho, imagine um ecossistema complexo em que cada\n'
        'indivíduo desempenha um papel específico. Cada função contribui para o\n'
        'funcionamento harmonioso do todo, mesmo que não seja imediatamente evidente.\n'
        'Seja na produção de bens, na prestação de serviços ou na criação de\n'
        'conhecimento, cada pessoa desempenha um papel que, de maneira coletiva, forma\n'
        'a teia da sociedade.\n\n'
        'Encorajamos você a começar a observar não apenas as ações grandiosas, mas\n'
        'também os detalhes e aparentemente insignificantes do seu dia a dia. Ao fazer isso,\n'
        'esperamos que você consiga enxergar a riqueza das interações que contribuem\n'
        'para a construção de uma sociedade coesa.\n\n'
        'Estamos ansiosos para continuar esse diálogo e ajudá-la a explorar as\n'
        'possibilidades que se apresentam além das muralhas que a cercam.\n\n'
        'Com esperança,\n'
        'Grupo SKT"\n'
    )

    #Carta(carta3, stdscr)
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario32 = (
        'Pela primeira vez, eu fiz antes o que o grupo me sugeriu, me sinto estranha por\n'
        'isso, mas de uma boa forma, vou escrever mais uma resposta antes de dormir, só\n'
        'que agora acredito que consiga dormir de uma melhor forma.\n'
    )

    #Diario(diario32, stdscr)
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario33 = (
        '"Prezado Grupo SKT,\n\n'
        'Agradeço por sua resposta esclarecedora e pelas orientações sobre observar as\n'
        'contribuições silenciosas que permeiam nosso cotidiano. Inspirada por suas\n'
        'palavras, resolvi ser mais proativa em explorar essas interconexões e entender\n'
        'melhor a divisão do trabalho.\n\n'
        'Hoje, voltei ao estabelecimento no caminho de casa e observei o processo de\n'
        'produção de um simples pão. Fiquei fascinada ao perceber como cada indivíduo\n'
        'desempenha um papel crucial, contribuindo para o funcionamento harmonioso do\n'
        'estabelecimento. Permitam-me compartilhar minha experiência.\n\n'
        'Ao entrar no local, deparei-me com um cenário movimentado e organizado. O\n'
        'padeiro, com suas habilidades, preparava a massa com dedicação e destreza. Uma\n'
        'assistente organizava os ingredientes e mantinha o ambiente limpo, contribuindo\n'
        'para a eficiência do processo. O atendente, com um sorriso caloroso, cuidava dos\n'
        'clientes e garantia que suas necessidades fossem atendidas.\n\n'
        'Enquanto observava, percebi que cada ação, por mais simples que parecesse,\n'
        'desempenhava um papel fundamental no resultado – um pão fresco e delicioso.\n'
        'Desde o agricultor que cultiva o trigo até o entregador que transporta o produto final,\n'
        'cada elo na cadeia de produção contribui para a satisfação do cliente.\n\n'
        'Essa experiência prática me fez apreciar ainda mais a complexidade e a beleza das\n'
        'interações cotidianas. Estou começando a entender como as divisões de trabalho,\n'
        'muitas vezes invisíveis, estão presentes em diversos aspectos da nossa vida.\n\n'
        'Agradeço por me incentivarem a explorar esse aspecto da sociedade. Estou ansiosa\n'
        'para continuar aprendendo e descobrindo mais sobre essas conexões invisíveis que\n'
        'moldam nosso mundo.\n\n'
        'Com gratidão,\n'
        'Emily"\n'
    )

    #Diario(diario33, stdscr)
    stdscr.border()
    stdscr.refresh()

    time.sleep(1)
    stdscr.addstr(10, 40, "             ▄▄                       ")
    stdscr.addstr(11, 40, "▀███▀▀▀██▄   ██                       ")
    stdscr.addstr(12, 40, "  ██    ▀██▄                          ")
    stdscr.addstr(13, 40, "  ██     ▀█████  ▄█▀██▄          ▄██  ")
    stdscr.addstr(14, 40, "  ██      ██ ██ ██   ██         ████  ")
    stdscr.addstr(15, 40, "  ██     ▄██ ██  ▄█████       ▄█▀ ██  ")
    stdscr.addstr(16, 40, "  ██    ▄██▀ ██ ██   ██     ▄█▀   ██  ")
    stdscr.addstr(17, 40, "▄████████▀ ▄████▄████▀██▄   ██████████")
    stdscr.addstr(18, 40, "                                 ██   ")
    stdscr.addstr(19, 40, "                                 ██   ")
    stdscr.refresh()


    time.sleep(2)
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario4 = (
        'Querido diário,\n\n'
        'Apesar dos últimos dias sobrecarregados, esta noite consegui descansar\n'
        'decentemente, comi o outro pão que ganhei ontem, estava excepcionalmente bom,\n'
        'continuei minha rotina ao escovar meus dentes e me arrumar para sair.\n\n'
        'Andei pela rua agora de cabeça erguida, mesmo com alguns olhares de\n'
        'estranhamento, segui confiante, a cada passo aquelas cartas faziam cada vez mais\n'
        'sentido na minha cabeça…\n\n'
        'Quando chego ao trabalho, os olhares não param, mesmo quando comecei a\n'
        'trabalhar, acho que essas coisas vão ficar frequentes no meu dia a dia, mas\n'
        'confesso que era o esperado…\n\n'
    )

    #Diario(diario4, stdscr)
    stdscr.border()
    stdscr.refresh()

    jogo_verdadeiro_falso()
    stdscr.clear()
    
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario41 = (
        'Ao fim do meu expediente, organizei os cartões como tinha feito, parece que foi\n'
        'efetivo da última vez, então acho legal continuar. Segui para o estabelecimento, que\n'
        'agora com minha cabeça levantada, percebi que a frente estava escrito “Padaria”,\n'
        'parece o nome do local… nunca havia percebido. Conversei um pouco com o\n'
        'atendente, peguei meu pão de costume e segui para a casa, hoje sem carta nova,\n'
        'tirei a noite para pensar sobre tudo que estava acontecendo, logo fui descansar,\n'
        'tinha mais outro dia a frente.\n'
    )

    #Diario(diario41, stdscr)
    stdscr.border()
    stdscr.refresh()

    time.sleep(1)
    stdscr.addstr(10, 40, "             ▄▄                       ")
    stdscr.addstr(11, 40, "▀███▀▀▀██▄   ██                       ")
    stdscr.addstr(12, 40, "  ██    ▀██▄                          ")
    stdscr.addstr(13, 40, "  ██     ▀█████  ▄█▀██▄       █▄▄▄▄▄▄ ")
    stdscr.addstr(14, 40, "  ██      ██ ██ ██   ██      ▄█       ")
    stdscr.addstr(15, 40, "  ██     ▄██ ██  ▄█████      █████▄▄  ")
    stdscr.addstr(16, 40, "  ██    ▄██▀ ██ ██   ██           ▀██ ")
    stdscr.addstr(17, 40, "▄████████▀ ▄████▄████▀██▄    █     ██ ")
    stdscr.addstr(18, 40, "                            ███  ▄██  ")
    stdscr.addstr(19, 40, "                             █████    ")
    stdscr.refresh()

    time.sleep(2)
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario5 = (
        'Querido diário,\n\n'
        'Mais uma boa noite de sono, mais um dia de trabalho, havia esquecido de escrever ontem,\n'
        'mas alguns dos meus colegas de trabalho começaram a perceber a diferença minha e\n'
        'perguntaram qual foi a “boa notícia” que recebi, conversei rapidamente com eles e disse\n'
        'que hoje explicaria melhor as coisas que descobri, acredito que se eu fizer o mesmo\n'
        'processo que a carta me fez, possa fazer com que eles entendam o que eu estou\n'
        'compreendendo, mesmo que eu ainda não saiba tudo.\n\n'
        'Faz algum tempo que não recebo mais cartas… Bem, hora de se arrumar e ir trabalhar.\n'
    )

    #Diario(diario5, stdscr)
    stdscr.border()
    stdscr.refresh()

    jogo_adivinhar()
    stdscr.clear()

    time.sleep(2)
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario51 = (
        'Mais um dia de trabalho concluído, conversei com meus colegas de trabalho e explicar os\n'
        'conceitos que aprendi, eles tiveram a mesma reação que tive: confusão e dúvidas, afinal,\n'
        'não é todo dia que você escuta uma ideia que nunca pensou, conforme os próximos dias\n'
        'vou começando a explicar melhor sobre tudo para eles.\n\n'
        'Voltei para a padaria (agora que descobri o nome) e cumprimentei o atendente, pedi o\n'
        'mesmo pão de sempre e jogamos conversa fora enquanto esperava o pedido.\n\n'
        'Hoje, focando mais em apenas uma função no trabalho, me sinto mais produtivo e, ao\n'
        'mesmo tempo… menos cansado? Sei que parece alguma loucura dizer isso, mas é o que\n'
        'eu sinto.\n\n'
        'Agora é descansar e se preparar para amanhã.\n'
    )

    #Diario(diario51, stdscr)
    stdscr.border()
    stdscr.refresh()

    time.sleep(1)
    stdscr.addstr(10, 40, "             ▄▄                      ")
    stdscr.addstr(11, 40, "▀███▀▀▀██▄   ██                ▄█▄▀  ")
    stdscr.addstr(12, 40, "  ██    ▀██▄                 ▄█▀     ")
    stdscr.addstr(13, 40, "  ██     ▀█████  ▄█▀██▄     ▄█████▄  ")
    stdscr.addstr(14, 40, "  ██      ██ ██ ██   ██     ██▀  ▀██▄")
    stdscr.addstr(15, 40, "  ██     ▄██ ██  ▄█████     ██     ██")
    stdscr.addstr(16, 40, "  ██    ▄██▀ ██ ██   ██     ██▄   ▄██")
    stdscr.addstr(17, 40, "▄████████▀ ▄████▄████▀██▄    ███████ ")
    stdscr.refresh()

    time.sleep(2)
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario6 = (
        'Querido diário,\n\n'
        'Durante o meu sono, recebi mais uma carta, que pelo visto parece ser a última..\n'
    )

    #Diario(diario6,stdscr)
    stdscr.border()
    stdscr.refresh()

    time.sleep(0.5)

    carta6 = (
        '“Prezada Emily,\n\n'
        'Ficamos imensamente gratos por compartilhar sua experiência conosco e por sua'
        'dedicação em explorar as intricadas conexões que moldam nosso cotidiano. Suas reflexões'
        'e observações revelam um profundo entendimento da complexidade e beleza que muitas'
        'vezes passam despercebidas.\n\n'
        'Entretanto, gostaríamos de informar que, por razões de segurança, nosso contato será'
        'finalizado. Entendemos que você já possui o conhecimento suficiente para proliferar as'
        'ideias que você agora acredita, sendo nosso apoio não mais necessário.\n\n'
        'Entendemos que sua jornada de exploração está apenas começando, e encorajamos'
        'veementemente que continue a buscar novas experiências e percepções. Seu interesse em'
        'compreender as divisões do trabalho e as contribuições silenciosas é inspirador,'
        'acreditamos que sua jornada de descoberta está apenas começando.\n\n'
        'Por favor, sinta-se à vontade para permanecer ativa em sua busca e compartilhar suas'
        'descobertas com aqueles ao seu redor. Há um vasto mundo de aprendizado à sua espera,'
        'e mal podemos esperar para ouvir mais sobre suas futuras explorações.\n\n'
        'Agradecemos por sua compreensão e colaboração. Que seus caminhos de descoberta'
        'sejam repletos de enriquecimento e aprendizado contínuo.\n\n'
        'Seja a diferença no seu mundo.\n\n'
        'Com estima,\n\n'
        'Grupo SKT”\n'
    )

    #Carta(carta6, stdscr)

    time.sleep(2)
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario61 = (
        'Bem, devo dizer que é uma pena o meu contato com o Grupo SKT ter se encerrado,'
        'minha visão do meu mundo nunca mais foi a mesma desde o momento que recebi a'
        'carta, agora meu trabalho é proliferar essa visão, em busca de uma melhor'
        'sociedade. Talvez sozinha não tenha a força para isso, mas com a união de uma'
        'classe no futuro, teremos a força para tal.\n\n'
        'Mas, enquanto essa força não chega, hora de me arrumar e ir trabalhar.\n'
    )

    #Diario(diario61, stdscr)
    stdscr.border()
    stdscr.refresh()

    jogo_associar_conceitos()
    stdscr.clear()

    time.sleep(2)
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario62 = (
        'Mais um dia de trabalho concluído, porém, devo dizer que vi todos meus companheiros de\n'
        'trabalho com aquela mesma sensação que tive ontem: mais produtivos, menos cansados.\n'
        'Claro, nós não vamos receber os benefícios desse aumento de produção, mas ao menos\n'
        'estaremos um pouco melhores no final do dia.\n\n'
        'Sinto que amanhã será o dia que algo grande irá acontecer, ainda não sei o que é, apenas\n'
        'sei que irá.\n\n'
        'Espero que o Grupo SKT consiga ver a nossa evolução.\n\n'
        'Hora de descansar.\n'
    )

    #Diario(diario62, stdscr)
    stdscr.border()
    stdscr.refresh()

    time.sleep(1)
    stdscr.addstr(10, 40, "             ▄▄                      ")
    stdscr.addstr(11, 40, "▀███▀▀▀██▄   ██                      ")
    stdscr.addstr(12, 40, "  ██    ▀██▄                         ")
    stdscr.addstr(13, 40, "  ██     ▀█████  ▄█▀██▄     █▄▄▄▄▄▄█▀")
    stdscr.addstr(14, 40, "  ██      ██ ██ ██   ██     █     █▀ ")
    stdscr.addstr(15, 40, "  ██     ▄██ ██  ▄█████          █▀  ")
    stdscr.addstr(16, 40, "  ██    ▄██▀ ██ ██   ██         █▀   ")
    stdscr.addstr(17, 40, "▄████████▀ ▄████▄████▀██▄      █▀    ")
    stdscr.addstr(18, 40, "                             █▀      ")
    stdscr.addstr(19, 40, "                            █▀       ")
    stdscr.refresh()

    time.sleep(2)
    stdscr.border()
    mensagem = curses.newwin(1, 15, 14, 50)
    stdscr.refresh()

    mensagem.clear()
    mensagem.addstr("[Digite... ]")
    mensagem.refresh()
    
    mensagem.clear()

    time.sleep(0.5)

    diario7 = (
        'Querido diário,\n\n'
        'Hoje, ao encerrar mais um dia na fábrica, me vejo compelido a registrar o turbilhão\n'
        'de pensamentos que tem invadido minha mente. Os últimos dias foram intensos,\n'
        'cheios de desafios, reflexões e, acima de tudo, uma busca incansável por\n'
        'compreensão.\n\n'
        'Durante as horas de trabalho, algo extraordinário aconteceu. Ao observar\n'
        'atentamente as engrenagens da produção, percebi que cada operário é como uma\n'
        'peça única, fundamental para o funcionamento harmonioso da máquina social.\n'
        'Cada movimento, cada ação, é uma contribuição indispensável para o equilíbrio que\n'
        'sustenta a estrutura da nossa sociedade.\n\n'
        'A divisão do trabalho, que antes parecia apenas uma rotina mecânica, agora\n'
        'revela-se como uma linha de produção complexa de habilidades interligadas. Cada\n'
        'função desempenhada por meus colegas se entrelaça em uma cena de\n'
        'interdependência, criando uma teia que sustenta não apenas o sistema de\n'
        'produção, mas toda a ordem social.\n\n'
        'Espero que eu possa continuar a ver as coisas sob essa nova ótica, ainda que me\n'
        'restem certos conceitos a explorar. Há momentos que ainda percebo um\n'
        'desequilíbrio  na divisão das tarefas.\n'
    )

    #Diario(diario7, stdscr)
    stdscr.border()
    stdscr.refresh()

    #Carta(decididor_final(), stdscr)
    stdscr.border()
    stdscr.refresh()

    time.sleep(1)
    stdscr.addstr(11, 40, "   ▀███▀▀▀███████▀████▄     ▄███▀   ")
    stdscr.addstr(12, 40, "     ██    ▀█ ██   ████    ████     ")
    stdscr.addstr(13, 40, "     ██   █   ██   █ ██   ▄█ ██     ")
    stdscr.addstr(14, 40, "     ██▀▀██   ██   █  ██  █▀ ██     ")
    stdscr.addstr(15, 40, "     ██   █   ██   █  ██▄█▀  ██     ")
    stdscr.addstr(16, 40, "     ██       ██   █  ▀██▀   ██     ")
    stdscr.addstr(17, 40, "   ▄████▄   ▄████▄███▄ ▀▀  ▄████▄   ")
    stdscr.refresh()

    botao = curses.newwin(1, 15, 24, 85)
    botao.addstr("[E]Próximo")
    botao.refresh()
    while True:
        key = stdscr.getkey()

        match key.upper():
            case "E":
                break
