import pygame

pygame.init()

#Pantalla
ANCHO, ALTURA = 800, 400
pantalla = pygame.display.set_mode((ANCHO, ALTURA))
pygame.display.set_caption("Wagon Wild")

#Imagen background (momentaneo)
background = pygame.image.load('imagenes/background.png')
background = pygame.transform.scale(background, (ANCHO, ALTURA))

#Icono (momentaneo)
icon = pygame.image.load('imagenes/icono juego.png')
pygame.display.set_icon(icon)

#Imagen botones (momentaneo)
play_img = pygame.image.load('imagenes/start2.png')
play_img = pygame.transform.scale_by(play_img, 1.4)
play_pos = (298, 200)
play_rect = play_img.get_rect(topleft=play_pos)

instructions_img = pygame.image.load('imagenes/instructions2.png')
instructions_img = pygame.transform.scale_by(instructions_img, 1.4)
instructions_pos = (298, 250)
instructions_rect = instructions_img.get_rect(topleft=instructions_pos)

quit_img = pygame.image.load('imagenes/quit2.png')
quit_img = pygame.transform.scale_by(quit_img, 1.4)
quit_pos = (298, 300)
quit_rect = quit_img.get_rect(topleft=quit_pos)

#crear boton
def dibujar_play():
    pantalla.blit(play_img, play_pos)

def dibujar_instructions():
    pantalla.blit(instructions_img, instructions_pos)

def dibujar_quit():
    pantalla.blit(quit_img, quit_pos)

#ciclo principal
run = True
while run:

    #background
    pantalla.blit(background, (0, 0))

    #dibujar botones
    dibujar_instructions()
    dibujar_play()
    dibujar_quit()

    pygame.display.update()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

        #detectar acciones mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(evento.pos) and pygame.mouse.get_pressed()[0]:
                print("Iniciar juego")
            elif instructions_rect.collidepoint(evento.pos) and pygame.mouse.get_pressed()[0]:
                print("Mostrar instrucciones")
            elif quit_rect.collidepoint(evento.pos) and pygame.mouse.get_pressed()[0]:
                pygame.quit()

pygame.quit()