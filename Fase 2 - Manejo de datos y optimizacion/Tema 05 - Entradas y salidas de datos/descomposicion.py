import sys

if len(sys.argv) == 2:
    argumento = int(sys.argv[1])
    if argumento<0 or argumento>9999:
        print("Digite un numero de 0 a 9999")
    else:
        numero = str(argumento)
        for i in range(len(numero)):
            print("{:04d}".format(int(numero[-1-i])*10**i))





else :
    print("Digite solo un numero")
