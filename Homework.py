import pygame
import time
import random

pygame.init()   #avvio pigame

##### VARIABILI GLOBALI #####
velocita_serpente = 12    #imposto la velocità del 'serpente'

punteggio = 0   #inizializzo la varabile punteggio la quale terrà traccia del punteggio

finestra_x = 720  #larghezza finestra
finestra_y = 480  #altezza finestra

fps = pygame.time.Clock()

pygame.display.set_caption('Snake') #imposto il titolo della finestra
finesta_di_gioco = pygame.display.set_mode((finestra_x, finestra_y))    #creo la finestra di gioco

##### DEFINIZIONE COLORI #####
nero = pygame.Color(0, 0, 0)
bianco = pygame.Color(255, 255, 255)
rosso = pygame.Color(255, 0, 0)
verde = pygame.Color(0, 255, 0)
blu = pygame.Color(0, 0, 255)
giallo = pygame.Color(255,255,0)
##### FINE VARIABILI GLOBALI E DEFINZIONE COLORI #####

################################################################
# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
corpo_serpente = [[100, 50],
			     [90, 50],
			     [80, 50],
			     [70, 50]
			     ]


# setting default snake direction towards
# right
direzione = 'DESTRA'
###############################################################
def inserisci_mela():
    global posizione_mela, esiste_mela
    posizione_mela = [random.randrange(1, (finestra_x//10)) * 10,   #la posizione della mela è
	                  random.randrange(1, (finestra_y//10)) * 10]

    esiste_mela = True

def inserisci_nickname():
    return
def termina_partita():
    return
def inizia_partita():
    return

def main():
    sposta_ = direzione   #inizializzo la variabile sposta_ che fa muovere il serpente nella direzione indicata dalla variabile direzione
    while True:
        ##### CATTURO GLI EVENTI DELL'UTENTE #####
        for event in pygame.event.get():    #catturo ogni evento della tastiera
            if event.type == pygame.QUIT:   #se l'evento è il click sulla crocetta per chiudere la finestra
                pygame.quit()               #arresto il programma
                exit()

            if event.type == pygame.KEYDOWN:       #se l'evento è un tasto della tasiera premuto

                if event.key == pygame.K_UP:       #e il tasto è la freccia in alto
                    sposta_ = 'SU'                 #

                if event.key == pygame.K_DOWN:     #e il tasto è la freccia in basso
                    sposta_ = 'GIU'                #

                if event.key == pygame.K_LEFT:     #e il tasto è la freccia a sinistra
                    sposta_ = 'SINISTRA'           #

                if event.key == pygame.K_RIGHT:    #e il tasto è la freccia a destra
                    sposta_ = 'DESTRA'             #
4
main()