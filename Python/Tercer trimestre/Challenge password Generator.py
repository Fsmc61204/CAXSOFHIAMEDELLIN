import random

base="abcdefghijklmnñopqrstuvwxyz"

while True:
  x=int(input("que tan larga quiere su  contraseña?"))
  y=int(input("cuantas contraseñas quiere?"))

  passw=""
  
  for i in range (y):
    for u in range (x):
      passw=passw+random.choice(base)
       
    print("password",passw)
    input()
    passw=""
  