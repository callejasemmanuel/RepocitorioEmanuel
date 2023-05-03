ejercicios = int(input("Ingrese el ejercicio que desea ejecutar: "))

if ejercicios == 1:
  #Ejercicio 1
  base = int(input(" Ingrese la base del triangulo:  "))
  altura = int(input(" ingrese la altura del triangulo: "))
  area =  (base * altura) / 2 
  print("El area de un triangulo es :", area)
elif ejercicios == 2:
  #Ejercicio 2
  n1 = int(input("¿Dime el primer numero para sumar? "))
  n2 = int(input("¿Dime el segundo numero para sumar? "))
  sum = (n1 + n2 )
  print (" el resultado  de la suma es :",sum ) 
elif ejercicios == 3:
  #Ejercicio 3
  numero = int(input("Ingrese el numero: "))
  elevado = numero * numero
  print("Resultado: ", elevado) 
elif ejercicios == 4:
  #Ejecicio 4 
  operacion = 1234 + 532
  print("La suma es", operacion) 
elif ejercicios == 5:
  #Ejecicio 5
  operacion = 1234 - 532
  print("La resta es",  operacion ) 
elif ejercicios == 6:
  #Ejercicio 6 
  operacion = 1234 * 532
  print("La multiplicación es",  operacion)
elif ejercicios == 7:
  #Ejecicio 7
  operacion = 1234 / 532
  print("La division es",  operacion )
elif ejercicios == 8:
  #Ejecicio 8
  operacion = 1234 % 532
  print("El modulo es",  operacion )
elif ejercicios == 9:
  #Ejecicio 9 
  euro = float(input("Ingrese valor euros: "))
  dolar = euro*1.10
  print(euro, "euros son", dolar, "dolares")
elif ejercicios == 10:
  #Ejecicio 10
  base = float(input("Ingrese base del rectangulo: "))
  altura = float(input("Ingrese altura del rectangulo: "))
  area = base * altura
  print("El valor del area es", area)
elif ejercicios == 11:
  #Ejecicio 11
  lado = float(input("Ingrese el valor de un lado: "))
  area = lado * lado
  perim = lado * 4
  print("Area: ", area)
  print("Perimetro: ", perim)
elif ejercicios == 12:
  #Ejecicio 12
  radio = float(input("Ingrese radio: : "))
  altura = float(input("Ingrese altura: "))
  area = (2 * 3.14159265 * radio * altura) + (2 * 3.14159265 * (radio * radio))
  volumen = 3.14159265 * (radio * radio) * altura
  print("Area: ", area)
  print("Volumen: ", volumen)
elif ejercicios == 13:
  #Ejecicio 13
  radio = float(input("Ingrese radio: "))
  longitud = (radio * 2) * 3.14159265
  area = (radio * radio) * 3.14159265
  print("Longitud:", longitud)
  print("Area:", area)
elif ejercicios == 14:
  #Ejecicio 14
  primNumero = float(input("Primer numero: "))
  segNumero = float(input("Segundo numero: "))
  terNumero = float(input("Tercer numero: "))
  promedio = (primNumero + segNumero + terNumero) / 3
  print("Promedio:", promedio)