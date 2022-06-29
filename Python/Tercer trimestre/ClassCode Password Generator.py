import random
#agregar el resto del abecedario

#volver el codigo infinito usando un while true
base="abcde1"

pasw=""
#permite que el usuario seleccione la longitud de su
# password

for i in range (15):
  pasw=pasw+random.choice(base)
print("pasword", pasw)
input()