
from random import randint    
from math import trunc
import copy

# ACA DEFINO CODIGOS DE COLORES (No se donde deberia ir "class", 
# la pongo arriba de todo para que resalte, y se corrija)

class color:
    rojo="\033[31m"
    azul="\033[34m"
    amarillo="\033[33m"
    reset="\033[39m"

def validar_entrada_numerica(entrada:str,limite_inferior:int,limite_superior:int)->int:
    """ Obj: Recibe un string, lo transforma a entero y devuelve ese entero si esta entre 2 numeros pasados por parametro
        Pre: String de entrada. Dos enteros que funcionen como limites del intervalo
        Post:Devuelve un entero en el intervalo especificado"""

    while not (entrada.isnumeric()):
        print("El valor debe ser un numero!!")
        entrada=input("reingrese el valor:")
    entrada=int(entrada)
    while (entrada<limite_inferior or entrada>limite_superior):
        print("El valor deber estar entre",limite_inferior,"y",limite_superior)
        entrada=input("reingrese el valor:")
        while not (entrada.isnumeric()):
            print("El valor debe ser un numero!!")
            entrada=input("reingrese el valor:")
        entrada=int(entrada)        
    return(entrada)

def generar_numeros(cant_filas:int,cant_columnas:int,carton:list):
    
    """ Obj: Recibe una matriz, y la devuelve de dimensiones nxm indicadas por parametro y llena de numeros aleatorios
        Pre: 2 enteros para las dimensiones, una matriz a modificar
        Post: Devuelve una matriz de n x m completa con numeros aleatorios"""

    for i in range (cant_filas):
        fila:list=[]
        carton.append(fila)    
        for j in range (cant_columnas):
            casillero:int=randint(1,11)
            casillero=casillero + j*11
            fila.append(casillero)
        
    return()

def quitar_repetidos(carton:list):
    """ Obj: Recibe una lista, y reemplaza los numeros repetidos en ella con numeros aleatorios        
        Pre: lista con numeros enteros.
        Post: Devuelve una lista de enteros sin numeros repetidos """
    existe_numero:list=[]
    # valida que no haya numeros iguales, avanza columna en columna
    for columna in range (len(carton[0])):
        for fila in range (0,len(carton)):
            if (carton[fila][columna] not in existe_numero):
                existe_numero.append(carton[fila][columna])
            else:
                while (carton[fila][columna] in existe_numero):
                    carton[fila][columna]=randint(1,11)+ columna*11
    return()

def remover_numeros(carton):    
    """ Obj: Recibe una lista y reemplaza 4 elementos de ella por ceros        
        Pre: Lista a modificar
        Post: Devuelve la lista con 4 elementos transformados en ceros """    

#quita "n" elementos, por defecto quitara 4
    numeros_a_quitar:int=4 

    for fila in range(len(carton)):
        for i in range (numeros_a_quitar):
            columna:int=randint(0,8)

            while (carton[fila][columna]==0):
                columna=randint(0,8)
            carton[fila][columna]=0

    return()

def crear_carton(carton:list)->list:
    """ Obj: Crea una matriz de enteros de nxm sin repetidos
        Pre: Una Lista vacia recibida por parametro
        Post: Devuelve una matriz de nxm sin numeros repetidos """
        
    cant_filas:int=3
    cant_columnas:int=9
    
    generar_numeros(cant_filas,cant_columnas,carton)
    quitar_repetidos(carton)
    remover_numeros(carton)

    return(carton)    

def iniciar_cartones(carton:list,cant_cartones_jugador:int,cartones_PC:dict,cartones_jugador:dict):
    """ Obj: Crea N cartones y reparte X cartones a un jugador y N-X al otro
        Pre: Cantidad X de cartones para el 1er jugador y 2 diccionarios donde guardar los cartones generados.
        Post: 2 Diccionarios con X cartones en uno de ellos y N-X en el otro.
    """
    cant_cartones_juego:int=10

    for i in range(cant_cartones_juego):
        carton=crear_carton(carton)    
        if (i<cant_cartones_jugador):
            cartones_jugador[i+1]=carton
        else:
            cartones_PC[(i+1)-cant_cartones_jugador]=carton
        carton=[]
    
    return()    

def mostrar_cartones(player:str,cartones:dict)->None:
    """ Obj: Muestra por pantalla un diccionario 
        Pre: Un String, para el dueño del diccionario, un diccionario.
        Post Muestra por consola los elementos del diccionario, sus claves y a quien pertenece:
    """
    print("Los cartones de",player,"son:")
    if (player=="PC"):
         for carton in cartones:
            print("\nEl carton",carton,"de",player,"es:")
            for fila in range(len(cartones[carton])):
                print(color.azul,cartones[carton][fila],color.reset)
    else:
        for carton in cartones:
            print("\nEl carton",carton,"de",player,"es:")
            for fila in range(len(cartones[carton])):
                print(color.rojo,cartones[carton][fila],color.reset)
    
    return()

def iniciar_datos_de_control(datos_de_control:dict,cartones_PC:dict,cartones_jugador:dict):
    """ Obj: Hace una copia del diccionario de los valores del diccionario de jugador, y crea una matriz de booleanos para la PC.  
        Pre: 2 diccionarios con los datos a copiar, un diccionario donde guardar las copias de los valores.
        Post Almacena la copia de los valores del diccionario Jugador, y la matriz de booleanos de la PC en 1 diccionario.
    """
    datos_de_control["cartones_originales"]:dict=copy.deepcopy(cartones_jugador)#Hace una copia de los VALORES de cartones originales del usuario
    for carton in cartones_PC:
        datos_de_control["premios"]["PC"][carton]=[]
        for fila in range(len(cartones_PC[carton])):
            cantada:bool=False
            datos_de_control["premios"]["PC"][carton].append(cantada)            
    gano_PC=False    
    datos_de_control["premios"]["PC"]["Victoria"]=gano_PC
    
    return()

def hay_linea(fila:list)->bool:
    """ Obj: Recibe una lista y chequea si todos sus elementos son cero. 
        Pre: Una lista a chequear.
        Post Devuelve el valor True si todos los elementos de la lista son cero, False en otro caso.
    """
    contador:int=0
    for columna in range(len(fila)):
        if (fila[columna]==0):
            contador+=1
    if contador==(len(fila)) and (contador!=0):
        linea=True
    else:
        linea=False    
    return(linea)

def hay_bingo(carton:list,numeros_validos:dict)->bool:
    """ Obj: Recibe un carton y chequea si todos sus elementos son cero. 
        Pre: Una carton a chequear.
        Post Devuelve el valor True si todos los elementos son cero, False en otro caso.
    """
    contador:int=0
    for fila in carton:
        if (hay_linea(fila)):
            contador+=1    
    if (contador==len(carton)):
       bingo=True
    else:
        bingo=False
    return(bingo)

def tachado_automatico(carton:list,numero_a_marcar:int):
    """ Obj: Recibe una lista y reemplaza por cero un valor entero especificado por parametro. 
        Pre: Una lista para modificar y un entero para buscar dentro de la lista.
        Post Devuelve la lista con un cero en cada posición donde aparece el valor indicado.
    """
    if (numero_a_marcar%11==0):
        columna=int((numero_a_marcar/11)-1) 
    else:
        columna=int(trunc(numero_a_marcar/11)) #calcula la columna donde va a ir a buscar el numero, para ahorrar comparaciones 
                        
    for fila in range(len(carton)):
        if (numero_a_marcar==carton[fila][columna]):
            carton[fila][columna]=0
    return()

def turno_PC(cartones_PC:dict,numeros_validos:dict,ronda:int,bolilla:int)->bool:
    """ Obj: Realiza lo pedido en el TP para la PC en 1 ronda(tachado automatico de numero y anuncia si hay premios.) 
        Pre: El diccionario con cartones de PC, 1 entero para la bolilla de la ronda correspondiente.
        Post Devuelve un booleano con True si hay bingo, False en otro caso .
    """                           
    for carton in cartones_PC:
        tachado_automatico(cartones_PC[carton],bolilla)

    if (ronda>5):
        for carton in cartones_PC:
            numero_fila:int=0
            for fila in cartones_PC[carton]:
                cantada:bool=numeros_validos["premios"]["PC"][carton][numero_fila] 
                #defino la variable cantada para q la logica del if quede mas clara               
                if(hay_linea(fila) and not cantada):
                    numeros_validos["premios"]["PC"][carton][numero_fila]=True
                    print("Mensaje de PC: Tengo linea en el carton:",carton)
                numero_fila+=1
    
    if (ronda>14):
        hubo_bingo=False
        for carton in cartones_PC:
            bingo=hay_bingo(cartones_PC[carton],numeros_validos)
            if bingo:
                print("Mensaje de PC: BINGOOOOOOOOOOOOOOOO")
                print("En el carton:",carton)
                print("\n\nGAME OVER\n\n")
                gano_PC=True    
                numeros_validos["premios"]["PC"]["Victoria"]=gano_PC
                hubo_bingo:bool=True                            
        if(hubo_bingo==True):               
            bingo=True
    else: 
        bingo=False

    return(bingo)
    
def tachar_numero(cartones_player:dict,numero_a_tachar:int):

    """ Obj: Permite el tachado manual de un numero, ingresando los valores por teclado. 
        Pre: Un diccionario con cartones, un entero con el numero a ser tachado.
        Post Diccionario modificado, con un cero en la posicion indicada por el usuario por teclado.
    """           
    print("Ok!Hora de tachar numeros!! Dónde está el",color.amarillo,numero_a_tachar,"?",color.reset)
    
    continuar:bool=False
    while not continuar:        
        mostrar_cartones("Jugador",cartones_player)
        print("\nSi no tiene el numero en sus cartones, presione 0 para volver al menu")
        marca_carton:str=(input( "En cual carton tachamos el numero?:"))
        marca_carton=validar_entrada_numerica(marca_carton,0,len(cartones_player))
        if (marca_carton==0):
            continuar=True
        else:                        
            for fila in cartones_player[marca_carton]:
                print(color.rojo,fila,color.reset)    
            marca_fila:str=(input("\nEn que fila??"))
            marca_fila=validar_entrada_numerica(marca_fila,1,len(cartones_player[marca_carton]))
            marca_columna:str=(input("En que columna??"))
            marca_columna=validar_entrada_numerica(marca_columna,1,len(fila))
            print("En la fila:",marca_fila,"columna:",marca_columna,"usted tiene el",numero_a_tachar,"?")
            player_decide:str=(input("Presione Y para confirmar:"))
            if (player_decide.upper()=="Y"):
                cartones_player[marca_carton][marca_fila-1][marca_columna-1]=0
                #el usuario marca fila y columna como humano (empezando del 1)
                print("Numero marcado!!")
                player_decide=input("Algún otro carton para marcar? pulse Y para marcar,cualquier tecla para seguir jugando:")
                if (player_decide.upper()=="Y"):
                    continuar=False
                else:
                    print("Seguimos!")
                    continuar=True
            else:
                print("Mire con cuidado!! si no marca correctamente perdera a la hora de validar.\n")
            
    return()

def cantar_premio(cartones_player:dict,numeros_validos:dict)->bool:
    """ Obj: Permite al user indicar el premio ganado mediante el ingreso por teclado de un string, guarda ese elemento en control. 
        Pre: Diccionario con cartones del usuario, diccionario donde almacenar la copia de los elementos ganadores.
        Post Devuelve True si el premio ingresado es Bingo.
    """
    premio:str=input("Algun premio? (Linea o Bingo)")

    if(premio.upper()=="LINEA"):
        carton_ganador:str=(input("Bien!! En que carton?"))
        carton_ganador=validar_entrada_numerica(carton_ganador,1,len(cartones_player))
        fila_ganadora:str=(input("Cual fila??"))
        fila_ganadora=validar_entrada_numerica(fila_ganadora,1,len(cartones_player[carton_ganador]))
        numeros_validos["premios"]["player"]["linea"].append(numeros_validos["cartones_originales"][carton_ganador][fila_ganadora])
        print("El carton",carton_ganador,"en su fila",fila_ganadora,"ha sido marcada!!")
        print("Felicitaciones, los premios seran chequeados y otorgados solo al final del juego")
        bingo=False
    
    elif(premio.upper()=="BINGO"):
        numero_carton_ganador:str=(input("De verdad!? En que carton!!?"))
        numero_carton_ganador=validar_entrada_numerica(numero_carton_ganador,1,len(cartones_player))
        numeros_validos["premios"]["player"]["carton"].append(numero_carton_ganador) 
        numeros_validos["premios"]["player"]["carton"].append(numeros_validos["cartones_originales"][numero_carton_ganador])
        print("Tenemos un ganador!!!!!\n")
        bingo=True
    
    else:
        print("Si no hay premio, seguimos jugando\n")
        bingo=False
        
    return(bingo)

def turno_player(cartones_player:dict,cartones_PC:dict,numeros_validos:dict,bolilla:int)->bool:
    """ Obj: Mostrar el estado actual del juego y un menu de opciones al usuario. 
        Pre: Diccionario con datos de control, diccionario con cartones de jugadores.Entero, con la bolilla de la ronda.
        Post Devuelve un bool:True si el usuario cantó Bingo en la ronda, False en cualquier otro caso.
    """
    pasar_ronda:bool=False
    OPCIONES: tuple = ( "1) Ver mis cartones",
                        "2) Ver cartones PC",
                        "3) Volver a ver el numero que salio",
                        "4) Tachar numero",
                        "5) Cantar premio!!!",
                        "6) Siguiente ronda"
                        )    
    print(color.amarillo+"\nHa salido el numero:",bolilla,"\n"+color.reset)

    while not(pasar_ronda):
        for item in OPCIONES:
            print(item)
        opcion:str =(input("\nPor favor, seleccione una opción:"))
        opcion=validar_entrada_numerica(opcion,1,len(OPCIONES))
        if (opcion==1):
            mostrar_cartones("Jugador",cartones_player)
            print()
        elif(opcion==2):
            mostrar_cartones("PC",cartones_PC)
            print()
        elif (opcion==3):
            print(color.amarillo+"\nHa salido el numero:",bolilla,"\n"+color.reset)
        elif (opcion==4):
            tachar_numero(cartones_player,bolilla)    
        elif (opcion==5):
            bingo=cantar_premio(cartones_player,numeros_validos)
            if bingo:
                pasar_ronda=True    
        elif (opcion==6):
            print("Proxima bolilla!!")
            pasar_ronda=True
            bingo=False
    return (bingo)

def jugada_especial(cartones_jugador:dict,numeros_validos:dict,ronda:int)->bool:

    """ Obj: Lanzar moneda y decidir entre un tachado manual y una creación nueva de carton. 
        Pre: Entero, numero de ronda. Diccionario con cart. de jugador, diccionario de control para modificar.
        Post Devuelve un booleano, true si el usuario canta bingo, false en otro caso.
    """
    print("Estamos en la ronda",ronda,"hora de una jugada especial!!.\n Lanzaremos una moneda, si sale 'seca' podra tachar un numero de sus cartones!!")
    print("Si es cara, le quitaremos uno de sus cartones al azar y lo reemplazaremos por uno nuevo!")
    input()

    lanzamiento_moneda:int=randint(0,1)
    if (lanzamiento_moneda==1):
        moneda:str="CARA"
        print("Salió",moneda,"!!")
        print("Lo sentimos, uno de sus cartones sera reemplazado, buena suerte:")
        carton_a_cambiar:int=randint(1,len(cartones_jugador))
        cartones_jugador[carton_a_cambiar]=[] #descarto carton
        cartones_jugador[carton_a_cambiar]=crear_carton(cartones_jugador[carton_a_cambiar])#asigno nuevo carton
        numeros_validos["cartones_originales"][carton_a_cambiar]=copy.deepcopy(cartones_jugador[carton_a_cambiar])
        print("Su carton",color.rojo,carton_a_cambiar,"sera cambiado por otro",color.reset)
        print("Aqui esta su nuevo carton, los numero que ya han salido se han marcado:\n")
        for numero in numeros_validos["numeros_sacados"]:
            if (numero!=0):
                tachado_automatico(cartones_jugador[carton_a_cambiar],numero)
        for fila in cartones_jugador[carton_a_cambiar]:
            print(color.rojo,fila,color.reset)
        bingo:bool=False
    elif(lanzamiento_moneda==0):
        moneda:str="SECA"
        print("Salió",moneda,"!!")
        numero_especial=(input("Felicidades!!!elija un numero para tachar de sus cartones:"))
        numero_especial=validar_entrada_numerica(numero_especial,1,99)
        numeros_validos["numeros_especiales"].append(numero_especial)
        tachar_numero(cartones_jugador,numero_especial)
        bingo=cantar_premio(cartones_jugador,numeros_validos)        
    
    return(bingo)

def nueva_ronda(cartones_player:dict,cartones_PC:dict,numeros_validos:dict,ronda:int)->bool:
    """ Obj: Genera una nueva bolilla, llama a los turnos de los jugadores. 
        Pre: Diccionario con Cartones de jugadores, Diccionario datos de control, numero de ronda. 
        Post Devuelve un booleano, true si el usuario o PC cantan bingo, false en otro caso.
    """
    print("Listos para la ronda:",ronda)
    bolilla:int=randint(1,99)
    while(bolilla in numeros_validos["numeros_sacados"]):
        bolilla=randint(1,99)
    numeros_validos["numeros_sacados"].append(bolilla)

    bingo=turno_PC(cartones_PC,numeros_validos,ronda,bolilla)   
    if not bingo:
        bingo=turno_player(cartones_player,cartones_PC,numeros_validos,bolilla)
    
    return(bingo)

def validar_bingo_jugador(datos_de_control:dict)->bool:
    """ Obj: Verifica si hay bingo en un carton, mediante un tachado automatico. De no haberlo, genera lista de errores. 
        Pre: Lista con un carton a chequear.
        Post Devuelve un booleano, True si el bingo era valido, False en otro caso.
    """
    valido:bool=False    
    carton_ganador:list=datos_de_control["premios"]["player"]["carton"][1]

    for numero in datos_de_control["numeros_sacados"]:
        if (numero!=0):
            tachado_automatico(carton_ganador,numero)    
    for numero in datos_de_control["numeros_especiales"]:
        if (numero!=0):
            tachado_automatico(carton_ganador,numero)    
    
    valido=hay_bingo(carton_ganador,datos_de_control)
    if not valido:
        datos_de_control["numeros_invalidos"]=[]
        for fila in carton_ganador:
            for columna in range (len(fila)):
                if (fila[columna])!=0:
                    datos_de_control["numeros_invalidos"].append(fila[columna])
    
    return(valido)

def repartir_premios(datos_de_control:dict, premio_adicional:bool):
    """ Obj: Hace los calculos para el monto ganado, dependiendo si hubo o no linea cantada. 
        Pre: Diccionario con datos de control para los montos, booleano: para indicar si hay q pagar un adicional por linea.
        Post Muesta por pantalla el premio ganado por el usuario.
    """
    premio:int=datos_de_control["tabla_premios"]["bingo"]
    print("\nFELICITACIONES!!!!")
    print("Usted tiene el carton ganador!!:")
    carton_ganador:list= datos_de_control["premios"]["player"]["carton"][1]
    for linea in (carton_ganador):
        print(color.rojo,linea,color.reset)
    print("\nSe lleva el premio por bingo de: $", premio)

    if (premio_adicional):
        print("Además, se lleva un adicional por linea de:",datos_de_control["tabla_premios"]["linea"])
        premio=premio+datos_de_control["tabla_premios"]["linea"]
    else:
        print("Su linea tenia un error o no fue cantada!! no se lleva el premio adicional,pero usted aun ha ganado.")
    print("Su premio total es de",premio)
    print("FELICIDADES!!! VUELVA A JUGAR PRONTO!!!")
    
    return()

def anunciar_resultados (bingo_valido:bool,datos_control:dict):
    """ Obj: Decide si hay premio o descalificacion y anuncia el resultado. 
        Pre: Booleano con el resultado del analisis del bingo, diccionario de datos de control.
        Post Muestra por pantalla el resultado del juego.
    """
    if (bingo_valido):       
            premio_adicional:bool=hay_linea(datos_control["premios"]["player"]["linea"])
            repartir_premios(datos_control,premio_adicional)
    else:
        print("Un momento...")
        print(color.rojo+"USTED HA SIDO DESCALIFICADO"+color.reset) 
        print("Su carton", datos_control["premios"]["player"]["carton"][0],"era el carton:")
        for fila in datos_control["premios"]["player"]["carton"][1]:
            print(color.rojo,fila,color.reset)
        print("Con los siguientes nuneros que no fueron parte del juego:")
        print(datos_control["numeros_invalidos"])
        print("Adios, tramposo!!")
    return()

def main ():
# DECLARACIONES:    
    carton:list=[]
    cartones_jugador:dict={}
    cartones_PC:dict={}
    datos_control:dict={"tabla_premios":{"linea":2000,"bingo":58000},
                        "numeros_sacados":[0],
                        "numeros_especiales":[],
                        "premios":{"PC":{},"player":{"linea":[],"carton":[]}}
                        }    
#SE CREAN LOS CARTONES: 
    print('Bienvenidos al Bingo de la catedra Costa: \n')
    cant_cartones_jugador:str=((input("Puede jugar con hasta 5 cartones, cuantos usará?:")))
    cant_cartones_jugador=validar_entrada_numerica(cant_cartones_jugador,1,5)        
    iniciar_cartones(carton,cant_cartones_jugador,cartones_PC,cartones_jugador)
    mostrar_cartones("jugador",cartones_jugador)
    mostrar_cartones("PC",cartones_PC)
#SE INICIAN LOS DATOS DE CONTROL:
    iniciar_datos_de_control(datos_control,cartones_PC,cartones_jugador)    
    print("\nTodo listo, que comience el juego!!!\n")
#FIN DEL SETUP

#COMIENZA EL JUEGO
    ronda:int=1
    bingo:bool=False
    
    while not bingo:
        if (ronda%4 != 0):
            bingo=nueva_ronda(cartones_jugador,cartones_PC,datos_control,ronda)
            ronda+=1
        else:
             bingo=jugada_especial(cartones_jugador,datos_control,ronda)
             if (not bingo):
                 input("Pulse una tecla para la siguiente bolilla:")
                 bingo=nueva_ronda(cartones_jugador,cartones_PC,datos_control,ronda)
                 ronda+=1        
# FIN DEL JUEGO.

#SE VALIDA LA VICTORIA, SE REPARTEN PREMIOS.
    victoria_PC:bool=datos_control["premios"]["PC"]["Victoria"]
    if (not victoria_PC):
        bingo=validar_bingo_jugador(datos_control)
        anunciar_resultados(bingo,datos_control)

main()