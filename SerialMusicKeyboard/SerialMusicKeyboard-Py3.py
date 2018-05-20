import sys
import pygame
import serial
screen = pygame.display.set_mode((470, 100))
background = pygame.image.load("fundo_teclado_arduino.png")
screen.blit(background, (0, 0))
pygame.display.flip()
ser = serial.Serial("COM3", 9600)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            ser.write(chr(event.key))
        elif event.type == pygame.KEYUP:
                ser.write(chr(256))