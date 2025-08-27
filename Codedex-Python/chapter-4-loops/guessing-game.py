# Write code below 💖
guess = 0
tries = 0

while guess != 6 and tries < 5:
  guess = int(input('Guess the number: \n'))
  print (tries)
  tries += 1 #add tries counter
#update tries

  if  guess != 6:
    if tries < 5:
      print(f"wrong number. tries left: {5 - tries}")
    else:
      print(f"Run out of tries. Tries count: {tries}")
  else:
    print("You got it!")