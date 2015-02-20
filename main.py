import pygame
import sys
import classJuego
import threading
pygame.init()




class eventosPygame:
    def __init__(self):
        self.exit = False
    def devolver(self):
        mouse =[0,0,0]
        mouse[0] = False
        key = False
        Down = None
        if self.exit == True:
            return ["exit",0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                self.exit = True
                return ["exit",0]
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse[0] = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse[0] = False
            if event.type == pygame.KEYDOWN:
                key = event.key
                Down = True
                
            if event.type == pygame.KEYUP:
                key = event.key
                Down = False
                
        
        mouse[1], mouse[2] = pygame.mouse.get_pos()
        
        keyss = pygame.key.get_pressed()
        keys = []
        for x in range(len(keyss)):
            if keyss[x] == 1:
                keys.append(x)
        
        return [mouse,[key,Down,keys]]
class treadEventosPygame(threading.Thread):
    def run(self):
        
        reloj = pygame.time.Clock()
        eventos = eventosPygame()
        self.cont = True
        while self.cont == True:
            self.eventos = eventos.devolver()
            if self.eventos[0] == "exit":
                self.cont = False
                
            reloj.tick(10)
        sys.exit()
    def devolver(self):
        try:
            return self.eventos
        except:
            return [[0,0],[None,False]]








def main():
    print "Welcome to this free kick game"
    print "Press space to shot"
    print "Press the keys to select the initial direction and then the effect"
    print "Press 'R' to restart the shot"
    print "Press shift while pressing a key to change the direction faster"
    print "Enjoy!"
    cont = True
    pantalla = pygame.display.set_mode((800,600),pygame.HWSURFACE)
    
    
    pygame.display.set_caption("penalty soccer")
    reloj = pygame.time.Clock()
    eventos = treadEventosPygame()
    juego = classJuego.practica(-200,200)
    ticks = False
    full = False
    eventos.start()
    while cont == True:
        
        events = eventos.devolver()
        if events[0] == "exit":
            cont = False
            sys.exit()
            print "h"   
        if events[1][0] == pygame.K_r and events[1][1] == True:
            juego.__init__(-200,200)
        if events[1][1] == True and events[1][0] == pygame.K_F11:
            if full == False:
                pantalla = pygame.display.set_mode((800,600),pygame.FULLSCREEN)
                full = True
            else:
                pantalla = pygame.display.set_mode((800,600))
                full = False
        pantalla.fill((0,255,0))
       
        reloj.tick(40)
       
      
        juego.actualizar(pantalla, events[1])
        pygame.display.update()
    
    
main()
