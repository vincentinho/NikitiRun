from PPlay.sprite import *
from random import randint

# função que move os inimigos na tela, deve ser recvisado para aumentar a variação dos inimigos e/ou
# evitar sobreposição nas faixas.

def chack_recorde(dist_percorrida):
    arquivo = open('records.txt', 'r')
    lines = arquivo.readlines(-1)
    recorde = lines[0]
    arquivo.close()
    if dist_percorrida >= float(recorde):
        registra_recorde(dist_percorrida)

def registra_recorde(recorde):
    arquivo = open('records.txt', 'w')
    arquivo.write(f'{recorde}')
    arquivo.close()


def roleta_inimigo():
    i = randint(1, 5)
    if i == 1:
        return Sprite('assets/inimigos/ambulancia.png')
    elif i == 2:
        return Sprite('assets/inimigos/wagon.png')
    elif i == 3:
        return Sprite('assets/inimigos/busuff.png')
    elif i == 4:
        return Sprite('assets/inimigos/limo.png')
    elif i == 5:
        return Sprite('assets/inimigos/taxi.png')


def mover_inimigo(inimigo, vel_bonus, janela, rua_i, faixa):
    # definindo a velociade que o inimigo ira se mover na tela.
    # possivelmente se tornara um parametro a ser recebido.

    # comportamento na tela
    inimigo.move_y(200 * janela.delta_time() + vel_bonus/2)

    # comportamento fora da tela
    if inimigo.y >= janela.height:
        inimigoy = inimigo.y
        inimigox = inimigo.x
        inimigo = roleta_inimigo()
        inimigo.set_position(inimigox, inimigoy)
        inimigo.y = -inimigo.height
        # seleção aleatria de uma faixag
        faixa = randint(1, 4)
        if faixa == 1:
            inimigo.x = rua_i + janela.width / 8 - inimigo.width
        elif faixa == 2:
            inimigo.x = rua_i + janela.width / 4
        elif faixa == 3:
            inimigo.x = rua_i + janela.width / 2 - inimigo.width / 2
        elif faixa == 4:
            inimigo.x = rua_i + janela.width / 1.5
    return inimigo, faixa

def mover_moedas(moedas, janela, vel, rua_i):
    for mod in moedas:
        mod[0].move_y(vel * janela.delta_time())
        if mod[0].y > janela.height:
            mod[0].y = -mod[0].height
            modx = mod[0].x
            mody = mod[0].y
            if mod[1] == 1:
                mod[0] = Sprite("assets/coletaveis/moeda.png", 9)
                mod[0].set_position(modx, mody)
                mod[0].set_sequence_time(0, 8, 300, True)
                mod[1] = 0
            if mod == moedas[-1]:
                faixa = randint(1, 4)
                if faixa == 1:
                    mod[0].x = rua_i + janela.width / 8 - mod[0].width
                elif faixa == 2:
                    mod[0].x = rua_i + janela.width / 4
                elif faixa == 3:
                    mod[0].x = rua_i + janela.width / 2 - mod[0].width / 2
                elif faixa == 4:
                    mod[0].x = rua_i + janela.width / 1.5
            else:
                mod[0].x = moedas[-1][0].x


def gameOver(teclado, janela, tot_moedas, tot_distancia):
    # salvando o progresso
    chack_recorde(tot_distancia)
    arq = open('registro.txt', 'r')
    lines = arq.readlines(-1)
    a = lines[0]
    tot_moedas += int(a)
    arq.close()
    arq = open('registro.txt', 'w')
    arq.write(f'{tot_moedas}')
    arq.close()

    gameover = Sprite("assets/background/game_over.png")
    gameover.set_position(janela.width / 2 - gameover.width / 2, janela.height / 2 - gameover.height / 2)
    while True:
        gameover.draw()
        janela.draw_text("aperte ESC para voltar ao menu!", janela.width/2 - 200, janela.height/2 + 120, 25, (200,200,0), "Arial", True, True)
        if teclado.key_pressed("ESC"):
            running = False
            return running
        janela.update()

def tem_sobrepos(inimigo1, faixa1, inimigo2, faixa2):
    if faixa1 != faixa2 or not inimigo1.collided(inimigo2):
        return inimigo1.x, inimigo1.y
    return inimigo1.x, -inimigo1.height

def decide_sprite_ret(flag):
    if flag == 1:
        return Sprite('assets/PLAYER/carro1_ret.png')
    elif flag == 2:
        return Sprite('assets/PLAYER/carro2_ret.png')
    elif flag == 3:
        return Sprite('assets/PLAYER/carro3_ret.png')
    elif flag == 4:
        return Sprite('assets/PLAYER/carro4_ret.png')

def decide_sprite_esq(flag):
    if flag == 1:
        return Sprite('assets/PLAYER/carro1_esq.png')
    elif flag == 2:
        return Sprite('assets/PLAYER/carro2_esq.png')
    elif flag == 3:
        return Sprite('assets/PLAYER/carro3_esq.png')
    elif flag == 4:
        return Sprite('assets/PLAYER/carro4_esq.png')

def decide_sprite_dir(flag):
    if flag == 1:
        return Sprite('assets/PLAYER/carro1_dir.png')
    elif flag == 2:
        return Sprite('assets/PLAYER/carro2_dir.png')
    elif flag == 3:
        return Sprite('assets/PLAYER/carro3_dir.png')
    elif flag == 4:
        return Sprite('assets/PLAYER/carro4_dir.png')

