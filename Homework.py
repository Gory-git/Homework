import pygame
import time
import random

from pygame.time import Clock

pygame.init()   #avvio pigame

##### VARIABILI GLOBALI #####
velocita_serpente = 12    #imposto la velocità del 'serpente'

punteggio = 0   #inizializzo la varabile punteggio la quale terrà traccia del punteggio

finestra_x = 720  #larghezza finestra
finestra_y = 480  #altezza finestra

fps = pygame.time.Clock()

pygame.display.set_caption('Snake') #imposto il titolo della finestra
finesta_di_gioco = pygame.display.set_mode((finestra_x, finestra_y))    #creo la finestra di gioco

font = "Helvetica neue"

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


#definisco la funzione che consente all'utente di inserire il nickname
def inserisci_nickname():
    return


#creo il menu di gioco
def menu():
    selezionato = 'RESTART' #preseleziono come opzione START

    while True:
        #catturo gli eventi da tastiera per potermi muovere nel menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #se l'utente chiude la finestra con la crocetta
                termina_partita()           #invoco la funzione termina partita per arrestare il programa

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_LEFT:
                    selezionato = 'RESTART'
                elif event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
                    selezionato = 'QUIT'
                if event.key == pygame.K_RETURN:
                    if selezionato == 'RESTART':
                       avvia_partita()
                    if selezionato == 'QUIT':
                        termina_partita()
        
        if selezionato == 'RESTART':
            testo_restart = testo('RESTART', bianco, font, 40)
        else:
            testo_restart = testo('RESTART', nero, font, 40)

        if selezionato == 'QUIT':
            testo_quit = testo('QUIT', bianco, font, 40)
        else:
            testo_quit = testo('QUIT',  nero, font, 40)
        
        rettangolo_restart = testo_restart.get_rect()
        rettangolo_quit = testo_quit.get_rect()

        rettangolo_restart.bottomleft = (finestra_x - 620, finestra_y -100)
        rettangolo_quit.bottomright = (finestra_x -100, finestra_y -100)

        finesta_di_gioco.blit(testo_restart, rettangolo_restart)
        finesta_di_gioco.blit(testo_quit, rettangolo_quit)

        pygame.display.update()

#definisco la funzione testo che mi consente di  
def testo(contenuto, colore, font_, dimensione):
    
    _font_=pygame.font.SysFont(font_, dimensione)
    testo=_font_.render(contenuto, True, colore)

    return testo

def game_over():

    suono = pygame.mixer.Sound('gameOverSoundEffects.webm')
    pygame.mixer.music.load('gameOverSoundEffects.webm')
    pygame.mixer.music.play(3)

    time.sleep(3)   #sospendo il programma per 3 secondi

    pygame.mixer.music.stop()

    finesta_di_gioco.fill(blu)  #coloro lo sfondo della finestra di blu
    
    #mostro il punteggio finale sullo schermo
    testo_game_over = testo('GAME OVER: ' + str(punteggio), rosso, font, 50)
    

    rettangolo_text = testo_game_over.get_rect()

    rettangolo_text.midtop = (finestra_x/2, finestra_y/4)

    finesta_di_gioco.blit(testo_game_over, rettangolo_text)
    pygame.display.flip()
    menu()

def termina_partita():

    #arresto il programma
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
                termina_partita()           #arresto il programma invocando la funzione termina_partita
                

            if event.type == pygame.KEYDOWN:       

                if event.key == pygame.K_UP:       #se l'utente preme la freccia in alto
                    sposta_ = 'SU'                 #assegno alla variabile spsta_ il valore SU

                if event.key == pygame.K_DOWN:     #se l'utente preme la freccia in basso
                    sposta_ = 'GIU'                #assegno alla variabile spsta_ il valore GIU

                if event.key == pygame.K_LEFT:     #se l'utente preme la freccia a sinistra
                    sposta_ = 'SINISTRA'           #assegno alla variabile spsta_ il valore SINISTRA

                if event.key == pygame.K_RIGHT:    #se l'utente preme la freccia a destra
                    sposta_ = 'DESTRA'             #assegno alla variabile spsta_ il valore DESTRA

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
        #in base alla direzione scelta incremento o decremento il 
        #valore delle coordinate della testa del serpente
        if direzione == 'SU':
            posizione_serpente[1] -= 10
        if direzione == 'GIU':
            posizione_serpente[1] += 10
        if direzione == 'SINISTRA':
            posizione_serpente[0] -= 10
        if direzione == 'DESTRA':
            posizione_serpente[0] += 10

        
        #sistema di accrescimento e movimento del serpente
        corpo_serpente.insert(0, list(posizione_serpente))                                              #aggiungo all'inizio del corpo del serpente un nuovo 'blocco' contenente
                                                                                                        #la posizione corrente della testa del serpente
        if posizione_serpente[0] == posizione_mela[0] and posizione_serpente[1] == posizione_mela[1]:   #se il serpente tocca la mela 
                                                                                                        #lascio il blocco appena aggiunto al serpente
            esiste_mela = False                                                                         #assegno alla variabile 'esiste_mela' False in modo tale che successivamente si inserisca un nuovo frutto
            punteggio += 1                                                                              #e incremento il punteggio della partita 
        else:
            corpo_serpente.pop()                                                                        #altrimenti elimino l'iltimo elemento del corpo del serpente
        
        if not esiste_mela:                 #controllo se è attualmente presente una mela sul campo di gioco
            posizione_mela = genera_mela()  #in caso affermativo invoco la funzione genera_mela() per assegnare alla mela una nuova posizione all'interno della finestra di gioco
            esiste_mela = True              #e assegno alla variabile esiste_mela il valore true

        ##### CONTROLLO DEI CASI IN CUI IL GIOCO POTREBBE TERMINARE #####
        #controllo se il serpente tocca i bordi della finestra
        #in caso li tocchi invoco la funzione game_over
        if posizione_serpente[0] < 0 or posizione_serpente[0] > finestra_x-10:
            game_over()                                                   
        if posizione_serpente[1] < 0 or posizione_serpente[1] > finestra_y-10:
            game_over()

        #controllo per ogni 'blocco' del serpente esclusa la 'testa' se viene toccato da quest'ulyima
        #in caso affermativo invoco la funzione game_over
        for blocco in corpo_serpente[1:]:
            if posizione_serpente[0] == blocco[0] and posizione_serpente[1] == blocco[1]:
                game_over()
        
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

        punti = testo('Puntieggio: ' + str(punteggio), nero, font, 30)

        rettangolo_punti = punti.get_rect()
        finesta_di_gioco.blit( punti, rettangolo_punti)

        #refresh della schermata di gioco
        pygame.display.update()

	    #frequenza di aggiornamento
        fps.tick(velocita_serpente)

def main():
    avvia_partita()
main()