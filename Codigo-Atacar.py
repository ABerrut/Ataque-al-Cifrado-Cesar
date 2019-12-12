def ataque_cifrado():
    texto=raw_input("Mensaje a desencriptar: " ) # Obtenemos mensaje a cifrar desde el usuario
    caracter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789�"        #Es el diccionario que usaremos 

    for key in range(len(caracter)):        #se iran recorriendo la posicion del diccionario
        traducido=''                        #Se crea la variable donde se guardara los que traduciremos

        for elem in texto:                          #Se iran recorriendo letra por letra del mensaje encriptado
            if elem in caracter:                    #Despues se ira recorriendo letra por letra del diccionario 
                elemIndex=caracter.find(elem)       # se buscara la posicion del la letra en el diccionario
                tradIndex= elemIndex-key            #Se le restara el numero que tenga que key al indice de la letra encontrada

                if tradIndex<0:                                 #Si el indice del indice de la traduccion es menor se 
                    tradIndex= tradIndex+len(caracter)          # suma el numero mas es numero del total de letras del diccionario
                traducido= traducido+caracter[tradIndex]        #despues en traducido se agrega la letra que puede ser el de la traduccion
            else:
                traducido=traducido+elem                        #si no a la traduccion se le agrega el mismo caracter

            if len(traducido)==len(texto):                      #esta es para imprimir solamente la cuando la cadena de texto traducida
                print('key #%s: %s' % (key, traducido))         #sea igual al de texto para mostrarla
ataque_cifrado()

