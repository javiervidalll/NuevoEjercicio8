import persistencia_json

listacoches = []
while True:
    marcacoche = input("Escribe una marca de coche: ")
    if marcacoche == "fin":
        break
    modelocoche = input("Modelo del coche : ")
    combustible = input("¿Que combustible usa?: ")
    cilindrada = input("¿que tamaño tiene es su cilindrada?: ")

    datos = {}

    datos["marcacoche"] = marcacoche
    datos["modelocoche"] = modelocoche
    datos["combustible"] = combustible
    datos["cilindrada"] = cilindrada

    listacoches.append(datos)
persistencia_json.store(listacoches, "Coches.txt")
listacoches = []
listacoches = persistencia_json.retrieve("Coches.txt")
print("Lista coches: \n", listacoches)