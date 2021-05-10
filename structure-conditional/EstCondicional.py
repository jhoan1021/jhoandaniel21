def muestraMenorEdad():
  #Definir variables y otros
  pnombre=""
  pedad=0
  #datos de entrada
  p1nombre=input("ingrese nombre 1ra persona:")
  p1edad=int(input("ingrese edad 1ra persona:"))
  p2nombre=input("ingrese nombre 2ra persona:")
  p2edad=int(input("ingrese edad 2ra persona:"))
  p3nombre=input("ingrese nombre 3ra persona:")
  p3edad=int(input("ingrese edad 3ra persona:"))
  #proceso
  if p1edad<p2edad and p1edad<p3edad:
    pnombre=p1nombre
    pedad=p1edad
  elif p2edad<p1edad and p2edad<p3edad:
    pnombre=p2nombre
    pedad=p2edad
  else:
    pnombre=p3nombre
    pedad=p3edad
  #Datos de salida
  print("la persona con menor edad es:", pnombre, "y su edad es:", pedad)
  
  muestraMenorEdad()

import os

calificacion = int (input ('Ingresa el valor de calificacion: '))
if calificacion==10:
    print ('A')
if calificacion==9:
    print ('B')
if calificacion==8:
    print ('C')
if calificacion==7:
    print ('D')
if calificacion==6:
    print ('E')
if calificacion<=5:
    print ('F')
print ()

import os

presupuesto = int (input ('Ingresa el valor de presupuesto: '))
if presupuesto<=10:
    print ('Tarjeta')
if presupuesto>=11 and presupuesto<=100:
    print ('Chocolates')
if presupuesto>=101 and presupuesto<=250:
    print ('Flores')
if presupuesto>=251:
    print ('Anillo')
print ()


import os

edad = int (input ('Ingresa el valor de edad: '))
if edad>=18:
    print ('S\u00ED puede votar en las pr\u00F3ximas elecciones.')
else:
    print ('No puede votar en las pr\u00F3ximas elecciones.')
print ()

import os

antiguedad = float (input ('Ingresa el valor de antiguedad: '))
sueldo = float (input ('Ingresa el valor de sueldo: '))
bono_por_antiguedad=0
if antiguedad>2 and antiguedad<5:
    bono_por_antiguedad=sueldo*0.2
if antiguedad>=5:
    bono_por_antiguedad=sueldo*0.3
bono_por_sueldo=0
if sueldo<=1000:
    bono_por_sueldo=sueldo*0.25
if sueldo>1000 and sueldo<=3500:
    bono_por_sueldo=sueldo*0.15
if sueldo>3500:
    bono_por_sueldo=sueldo*0.1
if bono_por_antiguedad>bono_por_sueldo:
    bono_mensual=bono_por_antiguedad
else:
    bono_mensual=bono_por_sueldo
print ('Valor de bono mensual: ' + repr (bono_mensual))
print ('Valor de bono por antiguedad: ' + repr (bono_por_antiguedad))
print ('Valor de bono por sueldo: ' + repr (bono_por_sueldo))
print ()
   

import os

edad = float (input ('Ingresa el valor de edad: '))
promedio = float (input ('Ingresa el valor de promedio: '))
beca=0
if edad>18 and promedio>=9:
    beca=2000
if edad>18 and promedio>=7.5 and promedio<9:
    beca=1000
if edad>18 and promedio>=6 and promedio<7.5:
    beca=500
if edad<=18 and promedio>=9:
    beca=3000
if edad<=18 and promedio>=8 and promedio<9:
    beca=2000
if edad>18 and promedio>=6 and promedio<8:
    beca=100
if promedio<6:
    print ('Se env\u00EDa carta de invitaci\u00F3n a estudiar m\u00E1s')
print ('Valor de beca: ' + repr (beca))
print ()

    import os

dia_de_la_semana = int (input ('Ingresa el valor de dia de la semana: '))
if dia_de_la_semana==1:
    print ('Lunes')
if dia_de_la_semana==2:
    print ('Martes')
if dia_de_la_semana==3:
    print ('Mi\u00E9rcoles')
if dia_de_la_semana==4:
    print ('Jueves')
if dia_de_la_semana==5:
    print ('Viernes')
if dia_de_la_semana==6:
    print ('S\u00E1bado')
if dia_de_la_semana==7:
    print ('Domingo')
if dia_de_la_semana<1 or dia_de_la_semana>7:
    print ('D\u00EDa no v\u00E1lido')
print ()
