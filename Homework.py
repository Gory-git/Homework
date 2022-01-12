import pygame
import time
import random

from pygame.constants import RESIZABLE

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

#creo la funzione che mi consente di generare un valore in maniera casuale 
#che serva come posizione della mela nella finestra di gioco
def genera_mela():
    mela = [random.randrange(1, (finestra_x // 10) - 1) * 10,
	        random.randrange(1, (finestra_y // 10) - 1) * 10]
    return mela

def mostra_punteggio(caso, colore, font, dimensione):
    #creo un oggetto per memorizzare il font scelto per il punteggio
    font_ = pygame.font.SysFont(font, dimensione)
    
    if caso == 0:
        #creo la superficie sulla finestra all'interno della quale inserirò il punteggio di gioco
        superficie_punteggio = font_.render(
            'punteggio : ' + str(punteggio), True, colore)
        
        #creo un rettangolo all'interno del quale andrò ad inserire il punteggio
        rettangolo_punteggio = superficie_punteggio.get_rect()
        
        #faccio visualizare il testo
        finesta_di_gioco.blit(superficie_punteggio, rettangolo_punteggio)
        
    if caso == 1:
        superficie_game_over = font_.render(
		    'Game Over! : ' + str(punteggio), True, colore)
        
        #creo un rettangolo per contenere il testo
        rettangolo_game_over = superficie_game_over.get_rect()
        
        # setting position of the text
        rettangolo_game_over.midtop = (finestra_x/2, finestra_y/4)
        
        # blit wil draw the text on screen
        finesta_di_gioco.blit(superficie_game_over, rettangolo_game_over)
        pygame.display.flip()


def inserisci_nickname():
    return
def termina_partita():
    
    mostra_punteggio(1, rosso, 'Retro.ttf',50)

    time.sleep(3)

    pygame.quit()
    exit()
def avvia_partita():

    direzione = 'DESTRA'    #imposto come direzione di default 'DESTRA', 
                            #per fare in modo che all'inizio di ogni nuova partita il serpente si muova a destra

    sposta_ = direzione     #inizializzo la variabile sposta_ che fa muovere
                            #il serpente nella direzione indicata dalla variabile direzione

    
    posizione_serpente = [100, 100] #definisco la posizione di partenza del serpente

    #definisco i primi 4 blocchi del corpo del serpente
    corpo_serpente = [[100, 100],
			         [90, 100],
			         [80, 100],
			         [70, 100]]


    posizione_mela = genera_mela()  #prima di iniziare la partita assegno un posizione alla mela
    esiste_mela = True

    global punteggio
    punteggio = 0   #inizializzo la varabile punteggio la quale terrà traccia del punteggio

    while True:
        ##### CATTURO E GESTISCO GLI EVENTI DELL'UTENTE #####
        for event in pygame.event.get():    #catturo ogni evento della tastiera
            if event.type == pygame.QUIT:   #se l'evento è il click sulla crocetta per chiudere la finestra
                termina_partita()           #arresto il programma
                

            if event.type == pygame.KEYDOWN:       #se l'evento è un tasto della tasiera premuto

                if event.key == pygame.K_UP:       #e il tasto è la freccia in alto
                    sposta_ = 'SU'                 #

                if event.key == pygame.K_DOWN:     #e il tasto è la freccia in basso
                    sposta_ = 'GIU'                #

                if event.key == pygame.K_LEFT:     #e il tasto è la freccia a sinistra
                    sposta_ = 'SINISTRA'           #

                if event.key == pygame.K_RIGHT:    #e il tasto è la freccia a destra
                    sposta_ = 'DESTRA'             #

        #gestisco il caso in cui l'utente dica al programma di spostare 
        #il serpente in una direzione opposta a quella attuale
        if sposta_ == 'SU' and direzione != 'GIU':
            direzione = 'SU'
        if sposta_ == 'GIU' and direzione != 'SU':
            direzione = 'GIU'
        if sposta_ == 'SINISTRA' and direzione != 'DESTRA':
            direzione = 'SINISTRA'
        if sposta_ == 'DESTRA' and direzione != 'SINISTRA':
            direzione = 'DESTRA'


        #a questo punto posso cambiare la direzione del serpente
        #in base alla direzione scelta cambio il valore della poszione del serpente di un'unità per volta
        if direzione == 'SU':
            posizione_serpente[1] -= 10
        if direzione == 'GIU':
            posizione_serpente[1] += 10
        if direzione == 'SINISTRA':
            posizione_serpente[0] -= 10
        if direzione == 'DESTRA':
            posizione_serpente[0] += 10

        
        #sistema di accrescimento del serpente
        corpo_serpente.insert(0, list(posizione_serpente))                                              #aggiungo all'inizio del corpo del serpente un nuovo 'blocco' contenente
                                                                                                        #la posizione corrente della testa del serpente
        if posizione_serpente[0] == posizione_mela[0] and posizione_serpente[1] == posizione_mela[1]:   #se il serpente tocca il futto lo lascio
            esiste_mela = False                                                                         #assegnoo alla variabile 'esiste_mela' False in modo tale che successivamente io possa inserire un nuovo frutto
            punteggio += 1                                                                              #e incremento il punteggio della partita
        else:
            corpo_serpente.pop()                                                                        #altrimenti elimino l'iltimo elemento del corpo del serpente

        if not esiste_mela:                 #controllo se la mela è stata toccata dal serpente o meno
            posizione_mela = genera_mela()  #in caso affermativo invoco la funzione genera_mela() per assegnare alla mela una nuova posizione all'interno della finestra di gioco
            esiste_mela = True              #e assegno alla variabile esiste_mela il valore true

        #CONTROLLO DEI CASI IN CUI IL GIOCO POTREBBE TERMINARE
        #controllo se il serpente tocca i bordi della finestra
        #in caso li tocchi invoco la funzione termina partita
        if posizione_serpente[0] < 0 or posizione_serpente[0] > finestra_x-10:
            termina_partita()                                                   
        if posizione_serpente[1] < 0 or posizione_serpente[1] > finestra_y-10:
            termina_partita()

        #controllo per ogni 'blocco' del serpente esclusa la 'testa' se viene toccato da quest'ulyima
        #in caso affermativo invoco la funzione termina partita
        for blocco in corpo_serpente[1:]:
            if posizione_serpente[0] == blocco[0] and posizione_serpente[1] == blocco[1]:
                termina_partita()
        
        ##### INTERFACCIA DI GIOCO #####
        #coloro lo sfondo della finestra di verde
        finesta_di_gioco.fill(verde)

        #per ogni blocco nella finestra di gioco creo un rettangolo blu sulla sua posizione
        for blocco in corpo_serpente:
            pygame.draw.rect(finesta_di_gioco, blu,
                            pygame.Rect(blocco[0], blocco[1], 10, 10))
        
        #sulla posizione della mela creo un rettangolo rosso 
        pygame.draw.rect(finesta_di_gioco, rosso, pygame.Rect(
            posizione_mela[0], posizione_mela[1], 10, 10))

        #mostra continuamente il punteggio sullo schermo
        mostra_punteggio(0, nero, 'Retro.ttf', 30)


        #refresh della schermata di gioco
        pygame.display.update()

	    #frequenza di aggiornamento
        fps.tick(velocita_serpente)

def main():
    avvia_partita()
main()