from PPlay.sprite import *
from PPlay.window import *
import pygame
from time import sleep


def loja(janela, teclado, mouse, carro_selecionado, flag1, flag2, flag3, flag4):
    clock = pygame.time.Clock()

    carro1 = Sprite('assets/PLAYER/carro1_ret.png')
    carro2 = Sprite('assets/PLAYER/carro2_ret.png')
    carro3 = Sprite('assets/PLAYER/carro3_ret.png')
    carro4 = Sprite('assets/PLAYER/carro4_ret.png')

    carro1.set_position(150,150)
    carro2.set_position(300, 150)
    carro3.set_position(150, 400)
    carro4.set_position(300, 400)

    bot1_normal = Sprite('assets/BUTTONS/minb1.png')
    bot1_selec = Sprite('assets/BUTTONS/minb2.png')

    bot2_normal = Sprite('assets/BUTTONS/minb1.png')
    bot2_selec = Sprite('assets/BUTTONS/minb2.png')

    bot3_normal = Sprite('assets/BUTTONS/minb1.png')
    bot3_selec = Sprite('assets/BUTTONS/minb2.png')

    bot4_normal = Sprite('assets/BUTTONS/minb1.png')
    bot4_selec = Sprite('assets/BUTTONS/minb2.png')

    bot1_normal.set_position(carro1.x, carro1.y + carro1.height + 20)
    bot1_selec.set_position(bot1_normal.x, bot1_normal.y)

    bot2_normal.set_position(carro2.x, carro2.y + carro2.height + 20)
    bot2_selec.set_position(bot2_normal.x, bot2_normal.y)

    bot3_normal.set_position(carro3.x, carro3.y + carro3.height + 20)
    bot3_selec.set_position(bot3_normal.x, bot3_normal.y)

    bot4_normal.set_position(carro4.x, carro4.y + carro4.height + 20)
    bot4_selec.set_position(bot4_normal.x, bot4_normal.y)

    text2_venda = 'Preço: 250G'
    text3_venda = 'Preço: 500G'
    text4_venda = 'Preço: 1000G'

    text_selec = 'Selecionado!'
    text_comprado = 'Comprado!'

    background = Sprite("assets/background/configbackground.png")
    background.set_position(100, 100)

    mousebox = Sprite('assets/mousebox.png')
    mouse_delay = 1

    arq = open('registro.txt', 'r')
    lines = arq.readlines(-1)
    a = lines[0]
    moedas_posse = int(a)
    arq.close()

    comprando = True
    while comprando:
        background.draw()

        mousex, mousey = mouse.get_position()
        mousebox.set_position(mousex, mousey)

        mouse_delay += janela.delta_time()

        if mousebox.collided(bot1_normal):
            bot1_selec.draw()
            if mouse.is_button_pressed(1) and mouse_delay >= 1:
                flag1 = 2
                carro_selecionado = 1
                if flag2 != 0:
                    flag2 = 1
                if flag3 != 0:
                    flag3 = 1
                if flag4 != 0:
                    flag4 = 1
        else:
            bot1_normal.draw()
        carro1.draw()
        if flag1 == 2:
            janela.draw_text(text_selec, carro1.x - 15, carro1.y + carro1.height, 20, (0, 150, 0), 'Arial', False, False)
        else:
            janela.draw_text(text_comprado, carro1.x - 15, carro1.y + carro1.height, 20, (0, 0, 200), 'Arial', False, False)


        if mousebox.collided(bot2_normal):
            bot2_selec.draw()
            if mouse.is_button_pressed(1) and mouse_delay >= 1:
                if flag2 == 1:
                    carro_selecionado = 2
                    flag2 = 2
                    if flag1 != 0:
                        flag1 = 1
                    if flag3 != 0:
                        flag3 = 1
                    if flag4 != 0:
                        flag4 = 1
                elif flag2 == 0:
                    if moedas_posse >= 250:
                        carro_selecionado = 2
                        moedas_posse -= 250
                        flag2 = 2
                        if flag1 != 0:
                            flag1 = 1
                        if flag3 != 0:
                            flag3 = 1
                        if flag4 != 0:
                            flag4 = 1
                    else:
                        alerta(janela, mouse)

        else:
            bot2_normal.draw()
        carro2.draw()
        if flag2 == 0:
            janela.draw_text(text2_venda, carro2.x - 15, carro2.y + carro2.height, 20, (200, 150, 0), 'Arial', False, False)
        elif flag2 == 1:
            janela.draw_text(text_comprado, carro2.x - 15, carro2.y + carro2.height, 20, (0, 0, 200), 'Arial', False, False)
        else:
            janela.draw_text(text_selec, carro2.x - 15, carro2.y + carro2.height, 20, (0, 150, 0), 'Arial', False, False)


        if mousebox.collided(bot3_normal):
            bot3_selec.draw()
            if mouse.is_button_pressed(1) and mouse_delay >= 1:
                if flag3 == 1:
                    carro_selecionado = 3
                    flag3 = 2
                    if flag2 != 0:
                        flag2 = 1
                    if flag1 != 0:
                        flag1 = 1
                    if flag4 != 0:
                        flag4 = 1
                elif flag3 == 0:
                    if moedas_posse >= 500:
                        moedas_posse -= 500
                        carro_selecionado = 3
                        flag3 = 2
                        if flag2 != 0:
                            flag2 = 1
                        if flag1 != 0:
                            flag1 = 1
                        if flag4 != 0:
                            flag4 = 1
                    else:
                        alerta(janela, mouse)
        else:
            bot3_normal.draw()
        carro3.draw()
        if flag3 == 0:
            janela.draw_text(text3_venda, carro3.x - 15, carro3.y + carro3.height, 20, (200, 150, 0), 'Arial', False, False)
        elif flag3 == 1:
            janela.draw_text(text_comprado, carro3.x - 15, carro3.y + carro3.height, 20, (0, 0, 200), 'Arial', False, False)
        else:
            janela.draw_text(text_selec, carro3.x - 15, carro3.y + carro3.height, 20, (0, 150, 0), 'Arial', False, False)


        if mousebox.collided(bot4_normal):
            bot4_selec.draw()
            if mouse.is_button_pressed(1) and mouse_delay >= 1:
                if flag4 == 1:
                    carro_selecionado = 4
                    flag4 = 2
                    if flag2 != 0:
                        flag2 = 1
                    if flag1 != 0:
                        flag1 = 1
                    if flag3 != 0:
                        flag3 = 1
                elif flag4 == 0:
                    if moedas_posse >= 1000:
                        moedas_posse -= 1000
                        carro_selecionado = 4
                        flag4 = 2
                        if flag2 != 0:
                            flag2 = 1
                        if flag1 != 0:
                            flag1 = 1
                        if flag3 != 0:
                            flag3 = 1
                    else:
                        alerta(janela, mouse)
        else:
            bot4_normal.draw()
        carro4.draw()
        if flag4 == 0:
            janela.draw_text(text4_venda, carro4.x - 15, carro4.y + carro4.height, 20, (200,150,0), 'Arial', False, False)
        elif flag4 == 1:
            janela.draw_text(text_comprado, carro4.x - 15, carro4.y + carro4.height, 20, (0, 0, 200), 'Arial', False, False)
        else:
            janela.draw_text(text_selec, carro4.x - 15, carro4.y + carro4.height, 20, (0, 150, 0), 'Arial', False, False)


        janela.draw_text(f'G: {moedas_posse}', janela.width//2 - 120, janela.height//3 + 50, 50, (250, 180,0), "Arial", False, False)

        if teclado.key_pressed("escape"):
            comprando = False

        clock.tick(60)
        janela.update()

    arqf = open('carros.txt', 'w')
    arqf.write(f"{flag1}\n{flag2}\n{flag3}\n{flag4}\n")
    arqf.close()

    arq = open('registro.txt', 'w')
    arq.write(f'{moedas_posse}')
    arq.close()
    return carro_selecionado, flag1, flag2, flag3, flag4


def alerta(janela, mouse):
    alert = Sprite('assets/background/alerta.png')
    bot_n = Sprite('assets/BUTTONS/minb1.png')
    bot_s = Sprite('assets/BUTTONS/minb2.png')

    mousebox = Sprite('assets/mousebox.png')
    alert.set_position(janela.width//2 - alert.width//2, janela.height//2 - alert.height//2)
    bot_n.set_position(janela.width//2 - bot_n.width//2, janela.height//2 - bot_n.height//2)
    bot_s.set_position(bot_n.x, bot_n.y)

    mouse_delay = 1
    aviso = True
    while aviso:
        Sprite('assets/background/fundo.png').draw()

        mouse_x, mouse_y = mouse.get_position()
        mousebox.set_position(mouse_x, mouse_y)

        mouse_delay += janela.delta_time()
        alert.draw()

        if mousebox.collided(bot_n):
            bot_s.draw()
            if mouse_delay >= 1 and mouse.is_button_pressed(1):
                aviso = False
        else:
            bot_n.draw()

        janela.update()
    Sprite('assets/background/fundo.png').draw()
    janela.update()
