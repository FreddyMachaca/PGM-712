import pygame
import random
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pelota que rebota")

# Colores
white = (255, 255, 255)

# Pelota
ball_radius = 30
ball_x = width // 2 #significa que la pelota se encuentra en la mitad del ancho de la pantalla de eje x
ball_y = height // 2 #significa que la pelota se encuentra en la mitad del alto de la pantalla de eje y
ball_speed_x = 10
ball_speed_y = 10

# Contadores
horizontal_bounces = 0 #contador de rebotes horizontales
vertical_bounces = 0 #contador de rebotes verticales
max_bounces = 5 #cantidad de rebotes antes de cambiar de dirección

# Dirección actual
moving_horizontal = True 

# Función para generar un color aleatorio
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #genera un color aleatorio

# Color inicial de la pelota
ball_color = random_color() 

# Bucle principal del juego
clock = pygame.time.Clock() 
running = True 

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

    if moving_horizontal:
        ball_x += ball_speed_x 
        if ball_x <= ball_radius or ball_x >= width - ball_radius: 
            ball_speed_x = -ball_speed_x 
            ball_color = random_color()
            horizontal_bounces += 1 #incrementa el contador de rebotes horizontales
            
        if horizontal_bounces == max_bounces: #si el contador de rebotes horizontales es igual a la cantidad de rebotes máximos
            moving_horizontal = False #cambia la dirección de la pelota
            horizontal_bounces = 0 
            ball_x = width // 2 
            ball_y = height // 2
    else:
        ball_y += ball_speed_y
        if ball_y <= ball_radius or ball_y >= height - ball_radius: 
            ball_speed_y = -ball_speed_y 
            ball_color = random_color()
            vertical_bounces += 1
            
        if vertical_bounces == max_bounces:
            moving_horizontal = True
            vertical_bounces = 0
            ball_x = width // 2
            ball_y = height // 2

    # Limpia la pantalla
    window.fill(white)

    # Dibuja la pelota
    pygame.draw.circle(window, ball_color, (int(ball_x), int(ball_y)), ball_radius)

    # Actualiza la pantalla
    pygame.display.flip()

    # Controla la velocidad del juego
    clock.tick(60)

# Cierra Pygame
pygame.quit()
sys.exit()