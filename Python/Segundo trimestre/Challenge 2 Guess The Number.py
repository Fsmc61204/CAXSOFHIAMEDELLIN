while True:
  n=float(input("guess the bumber:"))
  if(n<5):
    print("is short")
    
  if(n>5):
    print("is bigger")

  if(n==5):
    print("you guessed the number")