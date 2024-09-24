

#D_Informar el mayor de los números impares.
def mostrar_par_mayor(lista:list)->int:
    """muestra mayor pares

    Args:
        lista (list): lista mayor par

    Returns:
        int: devuelve mayor par
    """
    numero_mayor_par = 0
    for i in range(len(lista)):
       if lista[i] % 2 == 0:
           if lista[i] > numero_mayor_par:
               numero_mayor_par = lista[i]
            
    return numero_mayor_par   


#F_Listar todos los números pares.
def listar_pares(lista:list)->list:
    """Crea lista de pares

    Args:
        lista (list): lista pares

    Returns:
        list: devuelve pares
    """
    
    lista_pares = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            lista_pares.append(lista[i])
       
    return lista_pares


#G_Listar los números de las posiciones impares. 
def listar_impares(lista:list)->list:
    """lista las posiciones de impares

    Args:
        lista (list): crea la lista con los elementos que ocupan posisicon impar

    Returns:
        list: devielve la lista
    """
    
    lista_posiciones_impares = []
    for i in range(len(lista)):
        if i % 2 != 0:
            lista_posiciones_impares.append(lista[i])
    return lista_posiciones_impares