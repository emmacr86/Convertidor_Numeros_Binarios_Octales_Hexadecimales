#Funcion para convertir un decimal a cualquier base segun la opcion digitada
#Divide el numero hasta que el dividendo quede menor al dvisor

def convertir_decimal_a_base(numero, base):
    resultado = ''
    while numero // base != 0:
        resultado = asignar_caracter_a_numero(numero %base)+resultado
        numero = numero // base
    return asignar_caracter_a_numero(numero)+str(resultado)
    
#Definicion para base 2 
def convertir_decimal_a_base_2(decimal) :
    return convertir_decimal_a_base(decimal, 2)
    
#Definicion para base 8     
def convertir_decimal_a_base_8(decimal) :
    return convertir_decimal_a_base(decimal, 8)
    
#Definicion base 16
def convertir_decimal_a_base_16(decimal) :
    return convertir_decimal_a_base(decimal, 16)
#Esta funcion cambia los numeros a hexadecimales, como la base es 16 y no hay mayor base, no es necesario seguir cambiando los datos a alfanumericos

def asignar_caracter_a_numero(numero):
    if numero < 10 : return str(numero)
    else :
        if numero == 10: return "A"
        elif numero == 11: return "B"
        elif numero == 12: return "c"
        elif numero == 13: return "D"
        elif numero == 14: return "E"
        else : return "F"

def convertir_base_a_decimal(decimal, base):
  i =1
  resultado = 0
  for componente in decimal:
    exp = len(numero)-i;
    resultado = resultado+base**exp*asignar_numero_a_caracter(componente)
    i=i+1
  return resultado

#Definicion para base 2 
def convertir_base_2_a_decimal(numero):
  return convertir_base_a_decimal(numero, 2)

#Definicion para base 8  
def convertir_base_8_a_decimal(numero):
  return convertir_base_a_decimal(numero, 8)

#Definicion base 16
def convertir_base_16_a_decimal(numero):
  return convertir_base_a_decimal(numero, 16)

#Esta funcion cambia los numeros a hexadecimales
def asignar_numero_a_caracter(numero):
  if numero < 10 : return str(numero)
  else:
    if numero == "A": return 10
    elif numero == "B": return 11
    elif numero == "C": return 12
    elif numero == "D": return 13
    elif numero == "E": return 14
    elif numero == "F": return 15
    else : return int(numero)
    
#Inicio y desglose de opciones del programa
print "Este programa le ayudara a convertir sus numeros de decimal a numeros binarios, octales y hexadecimales o viceversa si es necesario."
print "A continuacion le desgloso las opciones disponibles: "
print "1) Convertir de Decimal a otras bases"
print "2) Convertir de Otras bases a Decimal."
print "3) Salir del programa."

opcion = int(input('Cual de las opciones desea utilizar? '))
while opcion <= 3:
    if opcion == 1:
#Menu de opciones para convertir de bases a decimales
        print "1) Convertir un numero decimal a binario"
        print "2) Convertir un numero decimal a octal"
        print "3) Convertir un numero decimal a hexadecimal"
#Se selecciona la opcion y realiza la operacion designada       
        seleccion = int(input('Digite la opcion a seleccionar? '))
        if seleccion ==1:
            numero = int(input('Introduce el numero a convertir a binario: '))
            print(convertir_decimal_a_base_2(numero))  
            opcion = int(input('Cual de las opciones desea utilizar? '))
        elif seleccion ==2:
            numero = int(input('Introduce el numero a convertir a octal: '))
            print(convertir_decimal_a_base_8(numero))  
            opcion = int(input('Cual de las opciones desea utilizar? '))
        elif seleccion ==3:
            numero = int(input('Introduce el numero a convertir a hexadecimal: '))
            print(convertir_decimal_a_base_16(numero))  
            opcion = int(input('Cual de las opciones desea utilizar? '))
    elif opcion ==2:
#Menu de opciones para convertir de bases a decimales
        print "1) Convertir un numero binario a decimal"   
        print "2) Convertir un numero octal a decimal"
        print "3) Convertir un numero hexadecimal a decimal"
#Se selecciona la opcion y realiza la operacion designada      
        seleccion = int(input('Digite la opcion a seleccionar? '))
        if seleccion == 1:
            numero = str(input('Introduce el numero a convertir a decimal: '))
            print (convertir_base_2_a_decimal(numero))
            opcion = int(input('Cual de las opciones desea utilizar? '))
        elif seleccion == 2:
            numero = str(input('Introduce el numero a convertir a decimal: '))
            print (convertir_base_8_a_decimal(numero))
            opcion = int(input('Cual de las opciones desea utilizar? '))
        elif seleccion == 3:
            numero = str(raw_input('Introduce el numero a convertir a decimal: '))
            print (convertir_base_16_a_decimal(numero))
            opcion = int(input('Cual de las opciones desea utilizar? '))
#Salida       
    elif opcion ==3:
        print "Muchas gracias "
        print "Lo esperamos pronto..."
        break
    else :
        print "Esa opcion no es valida"
        