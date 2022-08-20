import machine
from machine import Pin, Timer
from pyb import DAC

#dac = DAC(x, bits=12) #Declaramos el pin de salida del conversor D/A como x, para llenarlo más tarde.
#Declaramos un DAC de 12 bits


def temporizador(timer):
    #Variables globales compartidas con el main
    global contador, sentido
    #Lógica de la interrupción
    if sentido:
        contador += 1      
    else:
        contador -= 1

def cuadrado():
        global contador, sentido
        contador = 0
        sentido = True
    
        tim = Timer()
        tim.init(period= 100, mode=Timer.PERIODIC, callback=temporizador)
        while True:
            #Si contador es nueve coloque el sentido del contador a decrementar
            if contador == 5:
                sentido = False
                print("3,3")
                #dac.write(4095)  #enviar 3,3 al DAC
        
        #Si contador es cero coloque el sentido del contador a incrementar
            if contador == 0:
                sentido = True
                print("0")
                #dac.write(0)  #enviar 0 al DAC
                 
cuadrado()
                


