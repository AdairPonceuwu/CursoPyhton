import sys 

if len(sys.argv) == 3:
    texto=sys.argv[1]
    repeticiones = int(sys.argv[2])

    for f in range(repeticiones):
        print(texto)
else:
    print("Error-introduce los argumetnos correctamente")
    print("Ejemplo: escribir_lineas.py \"Texto\" 5")