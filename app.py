# Ingreso de datos
#productos = []
# Lista para prueba de borrado y mostrar datos
productos = [
    ["pelota de fútbol", 1500.00, 25],
    ["muñeca de trapo", 1200.50, 30],
    ["auto de carreras", 2300.75, 15],
    ["rompecabezas 1000 piezas", 3500.00, 10],
    ["set de bloques de construcción", 2800.00, 20],
    ["oso peluche", 1800.00, 18],
    ["juego de té infantil", 900.50, 22],
    ["pistola de agua", 750.00, 40],
    ["camión de bomberos", 3200.00, 12],
    ["kit de pintura", 1300.25, 25],
    ["ajedrez", 2100.75, 17],
    ["lego clásico", 4500.00, 8],
    ["monopatín infantil", 3000.00, 14],
    ["caja registradora de juguete", 1600.50, 20],
    ["patines", 2500.00, 11],
    ["avión de juguete", 1700.75, 19],
    ["mini cocina", 2900.00, 13],
    ["casa de muñecas", 5200.00, 5],
    ["bicicleta sin pedales", 3700.50, 9],
    ["robot interactivo", 4800.00, 6]
]
# while que genera un bucle infinito, mostrando en pantalla el menu de opciones.
while  True:
    print("=" * 70)
    print("Menu principal.")
    print("=" * 70)
    print("1. Agregar producto.")
    print("2. Mostrar productos.")
    print("3. Actualizar stock de un producto.")
    print("4. Eliminar producto.")
    print("5. Buscar producto.")
    print("6. Reporte de bajo stock.")
    print("0. Salir del programa.")
    
    # Variable que almacena la opcion seleccionada por le usuario.
    opcion =  input("Ingrese la opción deseada: ")
    # print(opcion.isdigit()) # Sirve para saber si todos los caracteres de esa cadena son dígitos (es decir, números enteros no negativos del 0 al 9).
    if opcion.isdigit(): # Compruebo que el dato ingresado sea  un número (True).
        opcion = int(opcion) # Convierto el dato string en integer
    else: # Si no es un numero (False), muestro un mensaje de error y vuelvo a dar las opciones.
        print("Opción invalida, por favor ingrese un número entero.")
        continue # Uso continue para que pase a la siguiente iteracion del while, repitiendo asi el codigo donde solicita los datos.
    
    # if para determinar  que opción selecciono el usuario y  realizar la acción correspondiente.
    if 0 <= opcion <= 6: # comprueba que opcion sea mayor a 0 y menor o igual a 6
        if opcion > 0 and opcion < 7:
            if opcion ==  1:
                # Pido al usuario ingrese  el nombre del producto, el precio y el stock almacenandolo en distintas variables.
                while True:
                # Validar nombre (solo letras y espacios)
                    nombre = input("Nombre del producto: ").strip().lower() #.strip() es como el .trim() en js que saca espacios atras y adelante
                    nombre_valido = True # Variable "bandera" que me ayuda a enviar mensaje de error
                    for char in nombre: # Recorro la cadena de caracteres para encontrar simbolos o numeros
                        if not (char.isalpha() or char.isspace()): # Aca comparo con negacion si  no es letra o espacio
                            nombre_valido = False #Si encuentro un numero o simbolo,  la variable se vuelve False
                            break  # Salgo del bucle si encontramos un simbolo o numero
                    #  Mostrar resultado
                    if not nombre_valido: # En este if verifico si nombre_valido esta en True o False. Si esta en False, quiere decir que el usuario metio la pata y hay que pedirle de nuevo los datos
                        print("El nombre del producto solo puede contener letras y espacios.")
                        continue # Uso continue para que pase a la siguiente iteracion del while, repitiendo asi el codigo donde solicita los datos.
                    break  # Rompemos el while para que continue a la proxima linea de codigo                  
                while True:
                    precio = input("Precio del producto: ")
                    if precio.isdigit(): # Compruebo que el dato ingresado sea  un número (True).
                        precio = int(precio) # Convierto el dato string en integer
                    elif precio.replace('.', '', 1).isdigit() and precio.count('.') == 1: # Honestidad, ayuda de chatgpt...Explicacion al final del codigo, porque investigue y lo entendi si no, no sirve
                        precio = float(precio)
                    else: # Si no es un numero (False), muestro un mensaje de error y vuelvo a dar las opciones.
                        print("Opción invalida, por favor ingrese un número entero.")
                        continue # Uso continue para que pase a la siguiente iteracion del while, repitiendo asi el codigo donde solicita los datos.
                    break
                    # Validar stock (número entero positivo)
                while True:
                    stock = input("Ingrese cantidad del producto: ")
                    if stock.isdigit() == False:
                        print("El stock debe ser numero entero y positivo. Vuelva a intentarlo.")
                        continue
                    else:
                        stock = int(stock) # Convierto el dato string en integer
                    # Si todas las validaciones son correctas, salimos del bucle
                    break
                productos.append([nombre, precio, stock])  # Agrego el producto a la lista de productos en un orden que siempre sera el mismo
                # Creo una lista con los nombres de las variables, de este modo se guardara sola la informacion que contienen.
            elif opcion == 2:
                # Reviso si la lista tiene elementos dentro de ella, si no es asi, envio un mensaje advirtiendo que no hay nada que mostrar
                if len(productos) == 0:
                    print("-" * 70)
                    print("No hay productos para mostrar.")
                    print("-" * 70)
                else: # Caso contrario, armo  un bucle for para mostrar los productos
                    print("-" * 70)  #para que se vea bonito
                    print("Lista de productos:")
                    print("-" * 70)
                    print(f"{'Nombre':<40}{'Precio':<15}{'Stock':<10}")
                    print("-" * 70)
                    # Recorro la lista de listas con un for para ingresar a cada elemento de la lista y asi imprimirla por pantalla
                    for producto in productos:
                        # Como se en que lugar de la lista va a encontrarse cada elemento, puedo acceder a ellos por el indice que ocupan
                        nombre = producto[0]
                        precio = producto[1]
                        stock = producto[2]
                        print(f"{nombre:<40}{precio:<15}{stock:<10}")
            elif opcion == 3:
                while True:
                    if len(productos) != 0:
                        while True:
                    # Validar nombre (solo letras y espacios)
                            busqueda = input("Ingrese el nombre del producto a modificar:  ").strip().lower() # Pido el nombre del producto a buscar y lo paso a minusculas para evitar errores
                            nombre_valido = True # Variable "bandera" que me ayuda a enviar mensaje de error
                            for char in busqueda: # Recorro la cadena de caracteres para encontrar simbolos o numeros
                                if not (char.isalpha() or char.isspace()): # Aca comparo con negacion si  no es letra o espacio
                                    nombre_valido = False #Si encuentro un numero o simbolo,  la variable se vuelve False
                                    break  # Salgo del bucle si encontramos un simbolo o numero
                            if nombre_valido == False: # En este if verifico si nombre_valido esta en True o False. Si esta en False, quiere decir que el usuario metio la pata y hay que pedirle de nuevo los datos
                                print("-" * 70)
                                print("El nombre del producto solo puede contener letras y espacios.")
                                print("-" * 70)
                                continue # Uso continue para que pase a la siguiente iteracion del while, repitiendo asi el codigo donde solicita los datos.
                            break
                        while True:
                            control_busqueda = False # Variable para control que indica si se encontro o no el producto.
                            for producto in productos: # Genero un bucle donde revisare cada posicion del array en busca de coincidencias.
                                if producto[0] == busqueda: # Si se encuentra el nombre buscado,  actualizo el stock y cambio el valor de la variable control_busqueda a True
                                # asi, de esta manera evito el if al final del bucle.
                                    stock = int(input("nueva cantidad en stock: "))
                                    producto[2] = stock
                                    control_busqueda = True # Cambio la variable a True para evitar ingresar al if al final del bucle y mostrar mensaje de no encontrado
                                    #Muestro como queda el producto  modificado para que el usuario controle si es correcta la modificacion.
                                    print("-" * 70)
                                    print(f"Producto actualizado: Nombre: {producto[0]}, Precio: {producto[1]}, Stock: {producto[2]}")
                                    print("-" * 70)
                                break
                            if control_busqueda == False: # Si no se encuentra el producto, ingresara a este if para mostrar el mensaje de producto no encontrado.
                                print("-" * 70)
                                print("Producto no encontrado, intente nuevamente.")
                                print("-" * 70)
                                break
                    else:
                        print("-" * 70)
                        print("No hay productos para mostrar")
                        print("-" * 70)
                        break
            elif  opcion == 4:
                while True:
                    if len(productos) != 0:
                        while True:
                            # Validar nombre (solo letras y espacios)
                            busqueda = input("Ingrese el nombre del producto a eliminar: ").strip().lower() # Pido el nombre del producto a buscar y lo paso a minusculas para evitar errores
                            nombre_valido = True # Variable "bandera" que me ayuda a enviar mensaje de error
                            for char in busqueda: # Recorro la cadena de caracteres para encontrar simbolos o numeros
                                if not (char.isalpha() or char.isspace()): # Aca comparo con negacion si  no es letra o espacio
                                    nombre_valido = False #Si encuentro un numero o simbolo,  la variable se vuelve False
                                    break  # Salgo del bucle si encontramos un simbolo o numero
                            if nombre_valido == False: # En este if verifico si nombre_valido esta en True o False. Si esta en False, quiere decir que el usuario metio la pata y hay que pedirle de nuevo los datos
                                print("-" * 70)
                                print("El nombre del producto solo puede contener letras y espacios.")
                                print("-" * 70)
                                continue # Uso continue para que pase a la siguiente iteracion del while, repitiendo asi el codigo donde solicita los datos.
                            break
                        control_busqueda = False # Variable para control que indica si se encontro o no el producto.
                        for producto in productos: # Genero un bucle donde revisare cada posicion del array en busca de coincidencias.
                            if producto[0] == busqueda: # Si se encuentra el producto, ingresa al if
                                control_busqueda = True # Cambio la variable a True para evitar ingresar al if al final del bucle y mostrar mensaje de no encontrado
                                productos.remove(producto) # Elimino el producto de la lista con el metodo .remove()
                                print("-" * 70)
                                print("Producto eliminado correctamente. ") # Informo la correcta eliminacion del producto
                                print("-" * 70)
                                # Si la lista queda sin productos, indico que no hay nada que mostrar
                                if len(productos) == 0:
                                    print("-" * 70)
                                    print("No hay productos para mostrar.")
                                    print("-" * 70)
                                else: # Caso contrario, armo  un bucle for para mostrar los productos que quedaron.
                                    print("-" * 70)  #para que se vea bonito
                                    print("Lista de productos:")
                                    print("-" * 70)
                                    print(f"{'Nombre':<40}{'Precio':<15}{'Stock':<10}")
                                    print("-" * 70)
                                # Recorro la lista de listas con un for para ingresar a cada elemento de la lista y asi imprimirla por pantalla
                                    for producto in productos:
                                # Como se en que lugar de la lista va a encontrarse cada elemento, puedo acceder a ellos por el indice que ocupan
                                        nombre = producto[0]
                                        precio = producto[1]
                                        stock = producto[2]
                                        print(f"{nombre:<40}{precio:<15}{stock:<10}")
                                    break
                        if control_busqueda == False:  # Si no se encuentra el producto, ingresara a este if para mostrar el mensaje de producto no  encontrado.
                            print("-" * 70)
                            print("Producto no encontrado, intente nuevamente.")
                            print("-" * 70)
                        break
                    else:
                        print("-" * 70)
                        print("No hay productos para mostrar.")
                        print("-" * 70)
                        break
            elif  opcion == 5:
                while True:
                    if len(productos) != 0:
                        while True:
                            # Validar nombre (solo letras y espacios)
                            busqueda = input("Ingrese el nombre del producto buscado: ").strip().lower() # Pido el nombre del producto a buscar y lo paso a minusculas para evitar errores
                            nombre_valido = True # Variable "bandera" que me ayuda a enviar mensaje de error
                            for char in busqueda: # Recorro la cadena de caracteres para encontrar simbolos o numeros
                                if not (char.isalpha() or char.isspace()): # Aca comparo con negacion si  no es letra o espacio
                                    nombre_valido = False #Si encuentro un numero o simbolo,  la variable se vuelve False
                                    break  # Salgo del bucle si encontramos un simbolo o numero
                            if nombre_valido == False: # En este if verifico si nombre_valido esta en True o False. Si esta en False, quiere decir que el usuario metio la pata y hay que pedirle de nuevo los datos
                                print("-" * 70)
                                print("El nombre del producto solo puede contener letras y espacios.")
                                print("-" * 70)
                                continue # Uso continue para que pase a la siguiente iteracion del while, repitiendo asi el codigo donde solicita los datos.
                            break
                        control_busqueda = False # Variable para control que indica si se encontro o no el producto.
                        for producto in productos: # Genero un bucle donde reviso cada posicion del array en busca de coincidencias.
                            if producto[0] == busqueda: # Si se encuentra el producto,  muestro el  producto.
                                control_busqueda = True # Cambio la variable a True para evitar ingresar al if al final del bucle y mostrar mensaje de no encontrado
                                print("-" * 70)
                                print(f"Producto encontrado:   Nombre: {producto[0]}, Precio: {producto[1]}, Stock: {producto[2]}")
                                print("-" * 70)
                                break
                        if control_busqueda == False: # Si no se encuentra el producto, ingresara a este if para mostrar el mensaje de producto no encontrado.
                            print("-" * 70)
                            print("Producto no encontrado, intente nuevamente.")
                            print("-" * 70)
                        break
                    else:
                        print("-" * 70)
                        print("No hay productos para mostrar.")
                        print("-" * 70)
                        break
            elif  opcion == 6:
                while True:
                    if len(productos) != 0:
                        while True:
                            bajo_stock = input("Ingrese el numero considerado stock bajo: ") # Le pido al usuario  que ingrese el numero de stock bajo
                            if bajo_stock.isdigit() == False: # Compruebo que el dato ingresado sea  un número (True)
                                print("-" * 70)
                                print("El stock debe ser numero entero y positivo. Vuelva a intentarlo.") # Le aviso que se equivoco
                                print("-" * 70)
                                continue  # Uso continue para que pase a la siguiente iteracion del while, repitiendo asi  el codigo donde solicita los datos.
                            else:
                                bajo_stock = int(bajo_stock) # Convierto el dato string en integer
                            # Si todas las validaciones son correctas, salimos del bucle
                            break
                        productos_bajo_stock = [] # Creo una lista para almacenar los datos que coincidan con la busqueda
                        for producto in productos: # Hago un bucle for que recorra la lista de productos
                            if producto[2] <= bajo_stock: # Con un if, comparo el stock de cada producto con el ingresado por el usuario
                                productos_bajo_stock.append(producto) # Cuando existe coincidencia, agrego ese producto  a la lista productos_bajo_stock
                        if len(productos_bajo_stock) == 0: # Si no hay ningun producto que tenga bajo stock, informo al usuario
                            print("-" * 70)
                            print("No hay productos con stock bajo.")
                            print("-" * 70)
                        else:  # Si hay productos con stock bajo, muestro la lista de productos con stock bajo
                            print("-" * 70)
                            print(f"{'Nombre':<40}{'Precio':<15}{'Stock':<10}")
                            print("-" * 70)
                            for producto in productos_bajo_stock:  # Recorro la lista de listas con un for para ingresar a cada elemento de la lista y  asi imprimirla por pantalla los resultados
                                nombre = producto[0]
                                precio = producto[1]
                                stock = producto[2]
                                print(f"{nombre:<40}{precio:<15}{stock:<10}")
                            break
                    else:
                        print("-" * 70)
                        print("No hay productos para mostrar.")
                        print("-" * 70)
                        break
                                        
        else: # Si la opcion es 0, saldra automaticamente del programa.
            print("Saliendo del programa.")
            break
    else: # Si la opcion ingresada no es valida, le informo al usuario y vuelvo a solicitar el ingreso del dato.
        print("-" * 70)
        print("Opción no válida. Por favor, ingrese una opción válida.")
        print("-" * 70)

'''======================================================================
Explicacion de precio.replace('.', '', 1).isdigit() and precio.count('.') == 1: (Validacion de numero decimal o entero en ingreso de datos del item 1)
Paso a Paso
1. precio.replace('.', '', 1)

Objetivo: Quitar un solo punto decimal (si existe) de la cadena precio.
Explicación: replace('.', '', 1) reemplaza el primer punto (.) que encuentra en precio con una cadena vacía (''), eliminándolo. El 1 significa que solo se eliminará el primer punto que aparezca, sin afectar otros caracteres.
Ejemplo:
    Si precio = "3.14", el resultado será "314".
    Si precio = "3.14.15", el resultado será "314.15" (solo elimina el primer .).

2. .isdigit()

Objetivo: Comprobar si todos los caracteres restantes en la cadena (después de haber eliminado un punto) son dígitos.
Explicación: isdigit() devuelve True solo si la cadena contiene exclusivamente números (después de haber eliminado un punto).
Ejemplo:
    "314".isdigit() devuelve True.
    "314.15".isdigit() devuelve False porque queda un punto.
Entonces, hasta aquí, precio.replace('.', '', 1).isdigit() será True solo si precio contenía solo dígitos y como máximo un punto decimal.
3. and precio.count('.') == 1
Objetivo: Verificar que haya exactamente un punto decimal en precio.
Explicación: count('.') cuenta cuántas veces aparece el punto en la cadena precio.
precio.count('.') == 1 asegura que solo hay un punto decimal. '''