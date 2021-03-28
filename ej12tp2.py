def convertir_mapa_en_matriz(b_lleno):
    """ Convierte mapa en matriz de caracteres y reemplaza guiones por 0s
    """
    for i in range(len(b_lleno)):
        b_lleno[i] = b_lleno[i].replace("-","0") # Reemplazar guiones por 0
        b_lleno[i] = list(b_lleno[i])
    return b_lleno


def convertir_mapa_en_strings(b_lleno):
    """ Vuelve a convertir la matriz en filas de strings
    """
    fila = ""
    for i in range(len(b_lleno)):
        for j in range(len(b_lleno[i])):
            fila += str(b_lleno[i][j])
        b_lleno[i] = fila
        fila = ""
    return b_lleno


def incrementar_minas(b_lleno, posX, posY):
    """Incrementa las cantidad de minas alrededor de la posicion indicada
    posX (int): ubicacion de la fila
    posY (int): ubicacion de la columna
    """
    maximoFila = len(b_lleno)
    maximoColumna = len(b_lleno[0])
    for i in range(-1,2): 
      for j in range(-1,2):
        posX1 = posX + i
        posY1 = posY + j
        if (-1 < posX1 < maximoFila) and (-1 < posY1 < maximoColumna):
            if b_lleno[posX1][posY1] != "*":
                b_lleno[posX1][posY1] = str(int(b_lleno[posX1][posY1]) + 1)
    return b_lleno


def imprimir_resultados(b_lleno):
    """ Imprime los resultados del buscaminas en formate del juego
    """
    for fila in b_lleno:
        print(fila)



# programa principal

buscamina_lleno = [
'-*-*-',
'--*--',
'----*',
'*----',
]

buscamina_lleno = convertir_mapa_en_matriz(buscamina_lleno)

for i in range(len(buscamina_lleno)):  # cantidad de filas
    for j in range(len(buscamina_lleno[i])):  # logitud de la fila
        if buscamina_lleno[i][j] == "*":  # si encuentra una mina
            buscamina_lleno = incrementar_minas(buscamina_lleno, i, j)

buscamina_lleno = convertir_mapa_en_strings(buscamina_lleno)


imprimir_resultados(buscamina_lleno)
