from Package_Input.input import *
from Especificas import *
from Array_Generales import *


def menu()->str:
    limpiar_pantalla()
    print(f"{'Menu de Opciones':^50s}")
    print("1 Ingresar de 10 números enteros entre -1000 y 1000.")
    print("2 Mostrar la cantidad de números positivos y negativos.")
    print("3 Mostrar la sumatoria de los números pares.")
    print("4 Informar el mayor de los números impares.")
    # print("5 Listar todos los números ingresados.")
    print("5 Listar todos los números pares.")
    print("6 Listar los números de las posiciones impares. ")
    print("7 Salir")
    return input("Ingrese una opcion: ")
def pausar():
    import os
    os.system("pause") 
    
def limpiar_pantalla():
    import os
    os.system('cls')



bandera = False
while True:
    
    match menu():
        case "1":
            resultado = pedir_numero()         
            print(f"Ingreso los numeros: {resultado}")  
            bandera = True
    
        case "2":
            if bandera:
                positivos, negativos = mostrar_positivo_negativos(resultado)
                print(f"Cantidad de números positivos: {positivos}")
                print(f"Cantidad de números negativos: {negativos}")
            else:
                print("Primero debes ingresar los números (opción 1).")    
        case "3":
            if bandera:
                respuesta = sumar_pares(resultado)
                print(f"La suma total de pares es: {respuesta}")
            else:
                print("Primero debes ingresar los números (opción 1).") 
            
        case "4":
            if bandera:
                respuesta_par_mayor = mostrar_par_mayor(resultado)
                print(f"El mayor de par es: {respuesta_par_mayor}")
            else:
                print("Primero debes ingresar los números (opción 1).") 
        case "5":
            if bandera:
                mostrar_pares = listar_pares(resultado)
                print(f"Mostra lista de pares: {mostrar_pares}")
            else:
                print("Primero debes ingresar los números (opción 1).") 
          
        case "6":
            if bandera:
                mostrar_posicion_impar = listar_impares(resultado)
                print(f"Mostrar los numero que se encuentra en posicion impar: {mostrar_posicion_impar}")
            else:
                print("Primero debes ingresar los números (opción 1).") 
        case "7":
            break
    pausar()                 
            
            
    
    
print("Fin del programa")
    
















