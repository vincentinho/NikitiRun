from PPlay.sprite import *
from PPlay.window import *
from pygame.time import Clock
import gamefunctions as GF
from pygame import mixer


def jogar_def(janela, teclado, efeitos_vol, carro):
    clock = Clock()
    motor_sound = mixer.Sound("sons/car.mp3")
    motor_sound.set_volume(efeitos_vol)
    buzina_sound = mixer.Sound("sons/buzina.mp3")
    moeda_sound = mixer.Sound("sons/moeda.mp3")
    moeda_sound.set_volume(efeitos_vol)

    # definindo as imagens que compoem o fundo do jogo (chão/rua)
    # são usadas as variaveis fundo e fundo2 pois precisamos que o fundo2 complete o gap deixado pelo fundo e vice
    # versa.
    fundo = Sprite('assets/background/fundo.png')
    fundo.set_position(0, -fundo.height + janela.height)
    # sobra é calculado para evitar que caso a imagem ser maior que a tela elas se sobreponham
    sobra = janela.height - fundo.height
    fundo2 = Sprite('assets/background/fundo.png')
    fundo2.set_position(0, -fundo2.height - fundo.height + janela.height)
    # velocidade de rolagem de fundo
    fundo_vel = 200
    # margem da imagem de fundo que é ocupada pela calçada
    rua_i = 50
    rua_f = fundo.width - 50

    hud = Sprite('assets/background/hud.png')
    hud.set_position(0,0)

    # definindo o player(revisar/estudar conceitos de animação e frames)
    carro_ret = GF.decide_sprite_ret(carro)
    carro_dir = GF.decide_sprite_dir(carro)
    carro_esq = GF.decide_sprite_esq(carro)
    player = carro_ret
    player.set_position(rua_i + janela.width / 2 - player.width / 2, janela.height - player.height - 30)
    player_vel = 200

    # definindo os inimigos
    # deve ser revisado para aumentar a variação dos inimigos
    inimigo1 = Sprite('assets/inimigos/taxi.png')
    inimigo1.set_position(rua_i + janela.width / 2 - inimigo1.width / 2, 0)

    inimigo2 = Sprite('assets/inimigos/busuff.png')
    inimigo2.set_position(rua_i + janela.width / 4, 0)

    inimigo3 = Sprite('assets/inimigos/wagon.png')
    inimigo3.set_position(rua_i + janela.width / 2 - inimigo3.width / 2, 300)

    inimigos_loc = [2, 3, 3]

    # coletaveis
    margem_coletaveis = 30
    m1 = Sprite("assets/coletaveis/moeda.png", 9)
    m2 = Sprite("assets/coletaveis/moeda.png", 9)
    m3 = Sprite("assets/coletaveis/moeda.png", 9)
    m1.set_sequence_time(0, 8, 300, True)
    m2.set_sequence_time(0, 8, 300, True)
    m3.set_sequence_time(0, 8, 300, True)
    pos_moedas = rua_i + janela.width / 8 - m1.width
    m1.set_position(pos_moedas, 0)
    m2.set_position(pos_moedas, m1.y + margem_coletaveis)
    m3.set_position(pos_moedas, m2.y + margem_coletaveis)
    Moedas = [[m1, 0], [m2,0], [m3,0]]

    # bonus de velocidade com o tempo
    vel_bonus = 0
    cont_tick = 0

    # carregar fonfon
    carrega_fofon = 1

    # contadores:
    cont_moedas = 0
    cont_distancia = 0

    # loop principal de jogo:
    inGame = True
    while inGame:
        if cont_distancia == 0:
            motor_sound.play(False)

        # desenhando as imagens de fundo:
        fundo2.draw()
        fundo.draw()

        # opção para voltar ao menu/ futuramente substituida por um pause/configurações.
        if teclado.key_pressed("ESC"):
            inGame = False

        # movimentando o player para a direita:
        if teclado.key_pressed("right") and player.x < rua_f - player.width:
            x = player.x
            y = player.y
            # definindo novo sprite para o carro fazendo a curva.
            player = carro_dir
            player.set_position(x, y)
            # definição da velocidade do player.
            player.move_x(player_vel * janela.delta_time())

        # movimentando o player para a esquerda:
        elif teclado.key_pressed("left") and player.x > rua_i:
            x = player.x
            y = player.y
            # definindo novo sprite para o carro fazendo a curva.
            player = carro_esq
            player.set_position(x, y)
            # definição da velocidade do player.
            player.move_x(-player_vel * janela.delta_time())
        else:
            x = player.x
            y = player.y
            # Definindo o sprite original caso não haja movimento lateral
            player = carro_ret
            player.set_position(x, y)

        carrega_fofon += janela.delta_time()
        if teclado.key_pressed("space") and carrega_fofon >= 0.8:
            carrega_fofon = 0
            buzina_sound.play(False)


        # COLISÃO!!!!!!!!!
        if player.collided(inimigo1) or player.collided(inimigo2) or player.collided(inimigo3):
            inGame = GF.gameOver(teclado, janela, cont_moedas, cont_distancia)

        # definição da velocidade qual o fundo estara deslizando:
        fundo2.move_y(fundo_vel * janela.delta_time() + vel_bonus)
        fundo.move_y(fundo_vel * janela.delta_time() + vel_bonus)

        # mecanismo de reposição do fundo:
        if fundo2.y > janela.height:
            fundo2.set_position(0, -fundo2.height + sobra)
        if fundo.y > janela.height:
            fundo.set_position(0, -fundo.height + sobra)

        # atualizando e desenhando os componentes de jogo na tela
        # atualizando a posição dos inimigos:
        inimigo1, inimigos_loc[0] = GF.mover_inimigo(inimigo1, vel_bonus, janela, rua_i, inimigos_loc[0])
        inimigo2, inimigos_loc[1] = GF.mover_inimigo(inimigo2, vel_bonus, janela, rua_i, inimigos_loc[1])
        inimigo3, inimigos_loc[2] = GF.mover_inimigo(inimigo3, vel_bonus, janela, rua_i, inimigos_loc[2])

        inimigo1.x, inimigo1.y = GF.tem_sobrepos(inimigo1, inimigos_loc[0], inimigo2, inimigos_loc[1])
        inimigo1.x, inimigo1.y = GF.tem_sobrepos(inimigo1, inimigos_loc[0], inimigo3, inimigos_loc[2])
        inimigo2.x, inimigo2.y = GF.tem_sobrepos(inimigo2, inimigos_loc[1], inimigo3, inimigos_loc[2])
        # atualizando a posição dos coletaveis
        if Moedas:
            for mod in Moedas:
                modx = mod[0].x
                mody = mod[0].y
                if player.collided(mod[0]) and mod[0].file_name == "assets/coletaveis/moeda.png":
                    cont_moedas += 1
                    moeda_sound.play(False)
                if mod[0].collided(player):
                    mod[1] = 1
                    mod[0] = Sprite("assets/coletaveis/moeda(1).png")
                    mod[0].set_sequence_time(0, 8, 300, True)
                    mod[0].set_position(modx, mody)

                mod[0].draw()
                mod[0].update()
        GF.mover_moedas(Moedas, janela, fundo_vel, rua_i)

        cont_tick += 1
        if cont_tick == 60 and vel_bonus < 15:
            cont_tick = 0
            if vel_bonus <= 20:
                vel_bonus += 0.1
            else:
                vel_bonus += 0.3
            if vel_bonus == 10:
                player_vel += 50
            if vel_bonus == 15:
                player_vel += 50

        if vel_bonus <= 8:
            cont_distancia += 0.05
        elif vel_bonus <= 15:
            cont_distancia += 0.7
        else:
            if cont_distancia >= 1000:
                cont_distancia += 3
            elif cont_distancia >= 500:
                cont_distancia += 1.5

        # desenhando o player:
        player.draw()

        # desenhando os inimigos:
        inimigo1.draw()
        inimigo2.draw()
        inimigo3.draw()

        # dezenhado o hud
        hud.draw()
        janela.draw_text(f"G:{cont_moedas}", 10, 10, 20, (0,0,255), 'Arial', True, False)
        janela.draw_text(f"D:{cont_distancia:.2f}m", 10, 30, 20, (0, 0, 255), 'Arial', True, False)
        # atualizando a tela.
        clock.tick(60)
        janela.update()
