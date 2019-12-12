def cifrado_cesar():
    # Obtenemos mensaje a cifrar desde el usuario
    # llamamos a upper para obtener s�lo may�sculas
    texto = raw_input("Mensaje > ")

    # Pedimos al usuario la cantidad de desplazamiento
    n = int(input("Desplazamiento > "))

    # Abecedario a utilizar en el cifrado
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    # Variable para guardar mensaje cifrado
    cifrado = ""
    for l in texto:
        # Si la letra est� en el abecedario se reemplaza
        if l in abc:
            cifrado += abc [(abc.index(l)+n)%(len(abc))]
        else:
            # Si no est� en el abecedario s�lo a�adelo
            cifrado+= l

    print("Mensaje cifrado:", cifrado)
cifrado_cesar()
