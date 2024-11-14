# Calcolo del Perimetro di diverse figure geometriche

import math
import time

lista=['CERCHIO','QUADRATO','RETTANGOLO', 'PENTAGONO', 'ESAGONO']

print("\n\n ***** CALCOLO PERIMETRO DI UNA FIGURA GEOMETRICA *****")

while True:
    print("\nScegli una delle seguenti figure geometriche:\n")

    for figura in lista: 
        print(figura, end="\t\t")
        time.sleep(1)

    scelta=input("\n\nScelta: ")

    # Opzioni di input accettabili per ogni figura
    opzioni_cerchio = [lista[0], lista[0].lower(), lista[0].capitalize(), "1"]
    opzioni_quadrato = [lista[1], lista[1].lower(), lista[1].capitalize(), "2"]
    opzioni_rettangolo = [lista[2], lista[2].lower(), lista[2].capitalize(), "3"]
    opzioni_pentagono = [lista[3], lista[3].lower(), lista[3].capitalize(), "4"]
    opzioni_esagono = [lista[4], lista[4].lower(), lista[4].capitalize(), "5"]


    if scelta in opzioni_cerchio:
        print(f"\nFigura selezionata: {lista[0]}")
        raggio=float(input("\nQual'è la misura del raggio (in cm)? "))
        perimetroc=2*raggio*math.pi
        print(f"\nIl Perimetro del {lista[0]} è {perimetroc:.2f} cm.\n\n")
           
    elif  scelta in opzioni_quadrato:
        print(f"\nFigura selezionata: {lista[1]}")
        latoq=float(input(f"\nQuanto misura il lato del {lista[1]} (in cm)? "))
        perimetroq=latoq*4
        print(f"\nIl Perimetro del {lista[1]} è {perimetroq:.2f} cm.")
    
    elif scelta in opzioni_rettangolo:
        print(f"\nFigura selezionata: {lista[2]}")
        altezzar=float(input(f"\nQuanto misura l'altezza (h) del {lista[2]} (in cm) ? "))
        baser=float(input(f"\nQuanto misura la base (b) del {lista[2]} (in cm) ? "))
        perimetror=(altezzar*2)+(baser*2)
        print(f"\nIl Perimetro del {lista[2]} è di {perimetror:.2f} cm.")

    elif scelta in opzioni_pentagono:
        print(f"\nFigura selezionata: {lista[3]}")
        latop=float(input(f"\nQuanto misura il lato del {lista[3]} (in cm) ? "))
        perimetrop=latop*5
        print(f"\nIl Perimetro del {lista[3]} è di {perimetrop:.2f} cm.")

    elif scelta in opzioni_esagono:
        print(f"\nFigura selezionata: {lista[4]}")
        latoe=float(input(f"\nQuanto misura il lato dell' {lista[4]} (in cm) ? "))
        perimetroe=latoe*6
        print(f"\nIl Perimetro del {lista[4]} è di {perimetroe:.2f} cm.")

    else:
        print("\n \U0001F61E "+" Errore! Riprova.\n\n")
        continue

    continua=input("\nVuoi calcolare il perimetro di un'altra figura? (Y/N)")
    if continua=="Y" or continua=="y":
        print("\n\n")
        continue
    else:
        print("\nOk! A presto. \U0001F44B \n")
        break
    