import pygame
import random
import sys

c1 = random.randint(0, 255)
c2 = random.randint(0, 255)
c3 = random.randint(0, 255)

# Inicialización de Pygame
colorizar = (c1, c2, c3)
pygame.init()

# Configuración de la ventana
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Movimiento Horizontal del Círculo")

# Colores
white = (255, 255, 255)

# Propiedades del círculo
circle_radius = 30
circle_x = circle_radius
circle_y = height // 2
circle_speed = 5

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mover el círculo
    circle_x += circle_speed

    # Si el círculo sale de la ventana, invertir la velocidad
    if circle_x > width - circle_radius or circle_x < circle_radius:
        circle_speed *= -1
        c1 = random.randint(0, 255)
        c2 = random.randint(0, 255)
        c3 = random.randint(0, 255)
        colorizar = (c1, c2, c3)
        
    # Rellenar la ventana con color blanco
    window.fill(white)

    # Dibujar el círculo
    pygame.draw.circle(window, colorizar, (circle_x, circle_y), circle_radius)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(60)
