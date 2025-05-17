from typing import Tuple

import numpy as np
import cv2 as cv
import serial,time




class ControlMotores:
    def control(self,x):

      def convertir(comando):
        comRec = comando
        comRecBytes = comRec.encode('utf-8')
        return comRecBytes     
      
      #------------------------------------------------------------------
      estado_azimut_anterior=self.estado_azimut_actual
      estado_elevacion_anterior=self.estado_elevacion_actual
      #------------------------- ---------------------------- ----------------------------------------------------
      
      #------------------------ Errores en posicion en pixeles ----------------------------------------------------
      error_posicion_azimut = x[0]
      error_posicion_elevacion =x[1]
      #------------------------- ---------------------------- ----------------------------------------------------
      #-------------------------Asignacion de estado -------------------------------------------------------------
      if error_posicion_azimut >= 0:
            if abs(error_posicion_azimut) > 30:
               self.estado_azimut_actual = "Derecha Rapido"
             #elif abs(error_posicion_azimut)<50 and abs(error_posicion_azimut)>30:
               #estado_azimut_actual = "Derecha Lento"
            else:
               self.estado_azimut_actual = "Frena"
      else:
            if abs(error_posicion_azimut) > 30:
               self.estado_azimut_actual = "Izquierda Rapido"
            #elif abs(error_posicion_azimut)<50 and abs(error_posicion_azimut)>30:
               #estado_azimut_actual = "Izquierda Lento"
            else:
               self.estado_azimut_actual = "Frena"
	
      if error_posicion_elevacion >= 0:
            if abs(error_posicion_elevacion) > 30:
               self.estado_elevacion_actual = "Arriba Rapido"
            #elif abs(error_posicion_elevacion)<50 and abs(error_posicion_elevacion)>30:
               #estado_elevacion_actual = "Arriba Lento"
            else:
               self.estado_elevacion_actual = "Frena"	
      else:
            if abs(error_posicion_elevacion) > 30:
               self.estado_elevacion_actual = "Abajo Rapido"
            #elif abs(error_posicion_elevacion)<50 and abs(error_posicion_elevacion)>30:
               #estado_elevacion_actual = "Abajo Lento"
            else:
               self.estado_elevacion_actual = "Frena"
      		
      #-----------------------------------------------------------------------------------------------------------

      #-----Comprobacion de estado y movimiento de montura--------------------------------------------------------
	
                
      #-----Comprobacion de estado y movimiento de montura--------------------------------------------------------

      if estado_azimut_anterior != self.estado_azimut_actual:
           
            if self.estado_azimut_actual == "Derecha Rapido":
                comando = convertir("-A~\n")
                print(comando)
                self.montura.write(comando)
                                             
            #elif estado_azimut_actual == "Derecha Lento":
               #lista = [0x3A,0x47,0x31,0x33,0x31,0x0D] 
               #montura_tx.write(lista)
               #time.sleep(0.02) 
               #lista = [0x3A,0x49,0x31,0x30,0x38,0x30,0x35,0x30,0x30,0x0D] 
               #montura_tx.write(lista)
               #time.sleep(0.02)
               #lista = [0x3A,0x4A,0x31,0x0D]
               #montura_tx.write(lista)		
            elif self.estado_azimut_actual == "Izquierda Rapido":
               #self.montura.write(b'-A~')
               comando = convertir("+A~\n")
               print(comando)
               self.montura.write(comando)	
           #elif estado_azimut_actual == "Izquierda Lento":
               #lista = [0x3A,0x47,0x31,0x33,0x30,0x0D] 
               #montura_tx.write(lista)
               #time.sleep(0.02) 
               #lista = [0x3A,0x49,0x31,0x30,0x38,0x30,0x35,0x30,0x30,0x0D] 
               #montura_tx.write(lista)
               #time.sleep(0.02)
               #lista = [0x3A,0x4A,0x31,0x0D]
               #montura_tx.write(lista)		
            elif self.estado_azimut_actual == "Frena":
               #self.montura.write(b'-A0')
               comando = convertir("-A!\n")
               print(comando)
               self.montura.write(comando)	

      if estado_elevacion_anterior != self.estado_elevacion_actual:
        time.sleep(0.02)
        if self.estado_elevacion_actual == "Arriba Rapido":
           #self.montura.write(b'+E°')
           comando = convertir("+E~\n")
           print(comando)
           self.montura.write(comando)
                                          		
        #elif estado_elevacion_actual == "Arriba Lento":
           #lista = [0x3A,0x47,0x32,0x33,0x31,0x0D] 
           #montura_tx.write(lista)
           #time.sleep(0.02) 
           #lista = [0x3A,0x49,0x32,0x30,0x38,0x30,0x35,0x30,0x30,0x0D] 
           #montura_tx.write(lista)
           #time.sleep(0.02)
           #lista = [0x3A,0x4A,0x32,0x0D]
           #montura_tx.write(lista) 	
        elif self.estado_elevacion_actual == "Abajo Rapido":
          #self.montura.write(b'-E~')
          comando = convertir("-E~\n")
          print(comando)
          self.montura.write(comando)
        #elif estado_elevacion_actual == "Abajo Lento":
           #lista = [0x3A,0x47,0x32,0x33,0x30,0x0D] 
           #montura_tx.write(lista)
           #time.sleep(0.02) 
           #lista = [0x3A,0x49,0x32,0x30,0x38,0x30,0x35,0x30,0x30,0x0D] 
           #montura_tx.write(lista)
           #time.sleep(0.02)
           #lista = [0x3A,0x4A,0x32,0x0D]
           #montura_tx.write(lista)		
        elif self.estado_elevacion_actual == "Frena":
           #self.montura.write(b'+E0') #'f' -> 'F' 24/04/24
           comando = convertir("+E!\n")
           print(comando)
           self.montura.write(comando) #---------------------------------------------------------------------------------------------------------
      
      
      #----------------------------------------------Imprimo en pantalla los datos------------------------------		
      #time.sleep(0.001)      #Tiempo_general
      self.montura.flushInput() # Se borra el buffer del puerto COM
      #---------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------
      
