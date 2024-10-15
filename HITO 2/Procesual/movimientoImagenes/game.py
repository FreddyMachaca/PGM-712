import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Carrera De Caballos")

# Cargar las imágenes
imagenes = [
    pygame.image.load("1.png"),
    pygame.image.load("2.png"),
    pygame.image.load("3.png"),
    pygame.image.load("4.png")
]

# Escalar las imágenes a un tamaño adecuado
imagenes = [pygame.transform.scale(img, (100, 100)) for img in imagenes]

# Índice de la imagen actual
imagen_actual = 0

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

    # Movimiento horizontal y cambio de imagen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= velocidad
        imagen_actual = (imagen_actual - 1) % len(imagenes)  # Cambiar a la imagen anterior
    if keys[pygame.K_RIGHT]:
        x += velocidad
        imagen_actual = (imagen_actual + 1) % len(imagenes)  # Cambiar a la siguiente imagen

    # Limpiar la pantalla
    screen.fill((255,255,255))

    # Dibujar la imagen actual en la nueva posición
    screen.blit(imagenes[imagen_actual], (x, y))

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar la velocidad de fotogramas
    pygame.time.Clock().tick(30)

# Salir del juego
pygame.quit()
sys.exit()
