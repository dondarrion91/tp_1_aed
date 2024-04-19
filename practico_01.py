__author__ = "TP1-G098"

cp = input("Ingrese el código postal del lugar de destino: ")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))

ISO_3166_2_AR_DIGITS = (
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "J",
    "K",
    "L",
    "M",
    "N",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
)

# Punto 1)
isArgentina = ((len(cp) == 8 and
               (cp[0] in ISO_3166_2_AR_DIGITS) and
               len(cp[1:5]) == 4 and
               cp[1:5].isdigit() and
               len(cp[5:]) == 3) and
               cp[5:].isalpha())

isBolivia = len(cp) == 4 and cp.isdigit()

isBrasil = len(cp) == 9 and cp[:5].isdigit() and cp[5] == "-" and cp[6:].isdigit()

isChile = len(cp) == 7 and cp.isdigit()

isParaguay = len(cp) == 6 and cp.isdigit()

isUruguay = len(cp) == 5 and cp.isdigit()


if isArgentina:
    destino = "Argentina"
elif isBolivia:
    destino = "Bolivia"
elif isBrasil:
    destino = "Brasil"
elif isChile:
    destino = "Chile"
elif isParaguay:
    destino = "Paraguay"
elif isUruguay:
    destino = "Uruguay"
else:
    destino = "Otro"

# Punto 2)
primer_digito_o_letra = cp[0]

provincia = "No aplica"

if isArgentina:
    if primer_digito_o_letra == "A":
        provincia = "Salta"
    elif primer_digito_o_letra == "B":
        provincia = "Provincia de Buenos Aires"
    elif primer_digito_o_letra == "C":
        provincia = "Ciudad Autónoma de Buenos Aires"
    elif primer_digito_o_letra == "D":
        provincia = "San Luis"
    elif primer_digito_o_letra == "E":
        provincia = "Entre Ríos"
    elif primer_digito_o_letra == "F":
        provincia = "La Rioja"
    elif primer_digito_o_letra == "G":
        provincia = "Santiago del Estero"
    elif primer_digito_o_letra == "H":
        provincia = "Chaco"
    elif primer_digito_o_letra == "J":
        provincia = "San Juan"
    elif primer_digito_o_letra == "K":
        provincia = "Catamarca"
    elif primer_digito_o_letra == "L":
        provincia = "La Pampa"
    elif primer_digito_o_letra == "M":
        provincia = "Mendoza"
    elif primer_digito_o_letra == "N":
        provincia = "Misiones"
    elif primer_digito_o_letra == "P":
        provincia = "Formosa"
    elif primer_digito_o_letra == "Q":
        provincia = "Neuquén"
    elif primer_digito_o_letra == "R":
        provincia = "Río Negro"
    elif primer_digito_o_letra == "S":
        provincia = "Santa Fe"
    elif primer_digito_o_letra == "T":
        provincia = "Tucumán"
    elif primer_digito_o_letra == "U":
        provincia = "Chubut"
    elif primer_digito_o_letra == "V":
        provincia = "Tierra del Fuego"
    elif primer_digito_o_letra == "W":
        provincia = "Corrientes"
    elif primer_digito_o_letra == "X":
        provincia = "Córdoba"
    elif primer_digito_o_letra == "Y":
        provincia = "Jujuy"
    elif primer_digito_o_letra == "Z":
        provincia = "Santa Cruz"

# Punto 3)
if tipo == 0:
    inicial = 1100
elif tipo == 1:
    inicial = 1800
elif tipo == 2:
    inicial = 2450
elif tipo == 3:
    inicial = 8300
elif tipo == 4:
    inicial = 10900
elif tipo == 5:
    inicial = 14300
elif tipo == 6:
    inicial = 17900
else:
    inicial = 0

if not isArgentina:
    if (isBolivia or isParaguay or (isUruguay and int(primer_digito_o_letra) == 1) or
            (isBrasil and primer_digito in (8, 9))):
        inicial = int(inicial * 1.20)
    elif (isChile or (isUruguay and int(primer_digito_o_letra) != 1) or
          (isBrasil and int(primer_digito_o_letra) in (0, 1, 2, 3))):
        inicial = int(inicial * 1.25)
    elif isBrasil and int(primer_digito_o_letra) in (4, 5, 6, 7):
        inicial = int(inicial * 1.30)
    else:
        inicial = int(inicial * 1.50)

# Punto 4)
final = inicial

if pago == 1:
    final = int(inicial * 0.90)


print("País de destino del envío:", destino)
print("Provincia destino:", provincia)
print("Importe inicial a pagar:", inicial)
print("Importe final a pagar:", final)
