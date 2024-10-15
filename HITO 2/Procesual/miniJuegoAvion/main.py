# Importar el módulo pygame
import pygame

# Importar al azar para números aleatorios
import random

# Importar pygame.locals para un acceso más fácil a las coordenadas clave
# Actualizado para cumplir con los estándares flake8 y negro
# de pygame.locals import *
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
    K_KP0,
    K_KP1,
    K_0,
    K_1,    
    K_s,
    K_z,
    K_x,
    K_c,
)

# Definir constantes para el ancho y alto de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
sw = 0
x = 0


# Define el objeto Player extendiendo pygame.sprite.Sprite
# En lugar de una superficie, usamos una imagen para un sprite más atractivo
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Mueve el sprite basado en las pulsaciones de teclascccxz
    def update(self, pressed_keys):
        if pressed_keys[K_UP] or pressed_keys[K_s]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if pressed_keys[K_DOWN] or pressed_keys[K_x]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
        if pressed_keys[K_LEFT] or pressed_keys[K_z]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] or pressed_keys[K_c]:
            self.rect.move_ip(5, 0)

        # Mantener al jugador en la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def automatico(self, mov):
        if mov == 1:
            self.rect.move_ip(0, 25)
            move_down_sound.play()
        else:
            self.rect.move_ip(0, -25)
            move_up_sound.play()

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    # MOvimiento automatico a la derecha
    def moveR(self):
        self.rect.move_ip(5, 0)

    # MOvimiento automatico a la derecha
    def moveL(self):
        self.rect.move_ip(-5, 0)

    # Posicion del personaje(Avion)
    def position(self):
        return self.rect.right
 

# Define el objeto enemigo extendiendo pygame.sprite.Sprite
# En lugar de una superficie, usamos una imagen para un sprite más atractivo
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        # La posición inicial se genera aleatoriamente, al igual que la velocidad
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)


    # Mueve al enemigo según la velocidad
    # Eliminarlo cuando pase el borde izquierdo de la pantalla
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Define el objeto de la nube extendiendo pygame.sprite.Sprite
# Usa una imagen para un sprite más atractivo
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # La posición inicial se genera aleatoriamente
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Mueve la nube en base a una velocidad constante
    # Eliminarlo cuando pase el borde izquierdo de la pantalla
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


# Configuración para sonidos, los valores predeterminados son buenos
pygame.mixer.init()


# Inicializar pygame
pygame.init()


# Configurar el reloj para una velocidad de fotogramas decente
clock = pygame.time.Clock()


# Crear el objeto de pantalla
# El tamaño está determinado por la constante SCREEN_WIDTH y SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Crear eventos personalizados para agregar un nuevo enemigo y nube
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Crea nuestro 'jugador'
player = Player()

# Crear grupos para contener sprites enemigos, sprites de nubes y todos los sprites
# - enemigos se utiliza para la detección de colisiones y actualizaciones de posición
# - nubes se utiliza para actualizaciones de posición
# - all_sprites se usa para renderizar
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Load and play our background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/

# pygame.mixer.music.load("Apoxode_-_Electric_1.mp3")
# pygame.mixer.music.play(loops=-1)


# Cargue todos nuestros archivos de sonido
# Fuentes de sonido: Jon Fincher
move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("Collision.ogg")

# Establecer el volumen base para todos los sonidos
move_up_sound.set_volume(0.5)
move_down_sound.set_volume(0.5)
collision_sound.set_volume(0.5)

# Variable para mantener nuestro ciclo principal en funcionamient
running = True

# Nuestro bucle principal
while running:
# Mira cada evento en la cola
    for event in pygame.event.get():
        # ¿El usuario presionó una tecla?
        if event.type == KEYDOWN:
            # ¿Era la tecla Escape? Si es así, pare el ciclo
            if event.key == K_ESCAPE:
                running = False

        # ¿El usuario hizo clic en el botón de cerrar ventana? Si es así, pare el ciclo
        elif event.type == QUIT:
            running = False

        # ¿Deberíamos agregar un nuevo enemigo?
        elif event.type == ADDENEMY:
            # Crea el nuevo enemigo y agrégalo a nuestros grupos de sprites
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # ¿Deberíamos agregar una nueva nube?
        elif event.type == ADDCLOUD:
            # Cree la nueva nube y agréguela a nuestros grupos de sprites
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # Obtenga el conjunto de teclas presionadas y verifique la entrada del usuario
    pressed_keys = pygame.key.get_pressed()

    # condicinal//Paraactivar el modo Automatico/////////////////////////////////////////////////////////
    if sw == 0:
        player.update(pressed_keys)

    if sw == 0 and (pressed_keys[K_KP0] or pressed_keys[K_0]):
        sw = 1
    elif sw == 1 and (pressed_keys[K_KP1] or pressed_keys[K_1]):
        sw = 0


    # Actualizar la posición de nuestros enemigos y nubes.
    enemies.update()
    clouds.update()

    # Llena la pantalla con azul cielo
    screen.fill((135, 206, 250))

    # Dibuja todos nuestros sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    
    # Movimiento automatico////////////////////////////////////////////////////////

    if sw == 1:
        # Cambio de movimiento
        if player.position() <= 100:
            x = 0
        elif player.position() >=  700:
            x = 1
        # Movimiento de derecha a izquierda
        if x == 0:
            player.moveR()
        else:
            player.moveL()

    # /////////////////////////////////////////////////////////////////////////////

    if sw == 1 and pygame.sprite.spritecollideany(player, enemies):
        # Modo Automatico (manipulacion automatica)
        player.automatico(random.randint(0,1))
        
    # Comprueba si algún enemigo ha chocado con el jugador
    elif pygame.sprite.spritecollideany(player, enemies):
        
        # Si es así, retira el reproducto
        player.kill()

        # Detenga cualquier sonido en movimiento y reproduzca el sonido de colisión
        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()

        # Detener el ciclo
        running = False

    # Voltear todo a la pantalla
    pygame.display.flip()

    # Asegúrese de mantener una velocidad de 30 fotogramas por segundo
    clock.tick(30)

# En este punto, hemos terminado, así que podemos detener y salir del mezclador.
pygame.mixer.music.stop()
pygame.mixer.quit()
