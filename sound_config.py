from pygame import mixer
from pygame.time import Clock
from PPlay.sprite import *


def configuracoes(janela, teclado, mouse, efeitos_vol, music_vol):
    clock = Clock()

    backcround = Sprite("assets/background/configbackground.png")
    backcround.set_position(janela.width//2 - backcround.width//2, janela.height//2 - backcround.height//2)

    mais_normal_1 = Sprite('assets/BUTTONS/minb1.png')
    mais_normal_2 = Sprite('assets/BUTTONS/minb1.png')
    menos_normal_1 = Sprite('assets/BUTTONS/minb1.png')
    menos_normal_2 = Sprite('assets/BUTTONS/minb1.png')

    mais_selec_1 = Sprite('assets/BUTTONS/minb2.png')
    mais_selec_2 = Sprite('assets/BUTTONS/minb2.png')
    menos_selec_1 = Sprite('assets/BUTTONS/minb2.png')
    menos_selec_2 = Sprite('assets/BUTTONS/minb2.png')

    mais_normal_1.set_position(300, 300)
    mais_selec_1.set_position(300, 300)

    menos_normal_1.set_position(150, 300)
    menos_selec_1.set_position(150, 300)

    mais_normal_2.set_position(300, 500)
    mais_selec_2.set_position(300, 500)

    menos_normal_2.set_position(150, 500)
    menos_selec_2.set_position(150, 500)

    mousebox = Sprite('assets/mousebox.png')
    mouse_delay = 1

    configurando = True
    while configurando:
        backcround.draw()
        mousex, mousey = mouse.get_position()
        mousebox.set_position(mousex, mousey)

        mouse_delay += janela.delta_time()

        janela.draw_text(f"volume musica:  {music_vol*100:.0f}", 150, 250, 30, (0,0,0), "arial", False, False)
        if mousebox.collided(mais_normal_1):
            mais_selec_1.draw()
            if mouse.is_button_pressed(1) and mouse_delay >= 0.5 and music_vol <= 0.9:
                mouse_delay = 0
                music_vol += 0.1
        else:
            mais_normal_1.draw()
        janela.draw_text(f"+", 320, 300, 30, (0, 0, 0), "arial", False, False)
        if mousebox.collided(menos_normal_1):
            menos_selec_1.draw()
            if mouse.is_button_pressed(1) and mouse_delay >= 0.5 and music_vol >= 0.1:
                mouse_delay = 0
                music_vol -= 0.1
        else:
            menos_normal_1.draw()
        janela.draw_text(f"-", 170, 300, 30, (0, 0, 0), "arial", False, False)

        janela.draw_text(f"volume efeitos:  {efeitos_vol*100:.0f}", 150, 450, 30, (0, 0, 0), "arial", False, False)
        if mousebox.collided(mais_normal_2):
            mais_selec_2.draw()
            if mouse.is_button_pressed(1) and mouse_delay >= 0.5 and efeitos_vol <= 0.9:
                mouse_delay = 0
                efeitos_vol += 0.1
        else:
            mais_normal_2.draw()
        janela.draw_text(f"+", 320, 500, 30, (0, 0, 0), "arial", False, False)
        if mousebox.collided(menos_normal_2):
            menos_selec_2.draw()
            if mouse.is_button_pressed(1) and mouse_delay >= 0.5 and efeitos_vol >= 0.1:
                mouse_delay = 0
                efeitos_vol -= 0.1
        else:
            menos_normal_2.draw()
        janela.draw_text(f"-", 170, 500, 30, (0, 0, 0), "arial", False, False)


        if teclado.key_pressed("escape"):
            configurando = False

        clock.tick(60)
        janela.update()

    return efeitos_vol, music_vol
