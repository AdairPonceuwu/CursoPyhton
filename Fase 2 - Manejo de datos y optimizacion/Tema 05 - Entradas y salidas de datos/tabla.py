import sys

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    if(filas<9 and filas >1 and columnas<9 and columnas>1):
        for i in range(filas):
            for j in range(columnas):
                print(" * ", end='')
            print("\n")
    else:
        print("Error argumentos incorrectos")

else:
    print("Error argumentos incorrectos")
    print("Ejemplo: tabla.py [1-9][1-9]")