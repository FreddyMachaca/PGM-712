import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moviendo imagen horizontalmente")

# Cargar la imagen
image = pygame.image.load("1.png")
# Escalar la imagen a un tamaño adecuado
image = pygame.transform.scale(image, (100, 100))

# Posición inicial de la imagen
x = 0
y = HEIGHT // 2 - 50  # Centrar la imagen verticalmente

# Velocidad de movimiento
velocidad = 5

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento horizontal
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= velocidad
    if keys[pygame.K_RIGHT]:
        x += velocidad

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Dibujar la imagen en la nueva posición
    screen.blit(image, (x, y))

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar la velocidad de fotogramas
    pygame.time.Clock().tick(60)

# Salir del juego
pygame.quit()
sys.exit()
