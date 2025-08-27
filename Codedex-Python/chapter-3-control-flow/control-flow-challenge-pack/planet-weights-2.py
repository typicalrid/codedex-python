# Write code below 💖
weight = float(input("weight on Earth(kg): "))
planet = int(input("planet: "))

if planet == 1 or planet == 3:
  gravity = 0.38
elif planet == 2:
  gravity = 0.91
elif planet == 4:
  gravity = 2.53
elif planet == 5:
  gravity = 1.07
elif planet == 6:
  gravity = 0.89
elif planet == 7:
  gravity = 1.14
else:
  print ("Invalid planet number")

dest_weight = (weight) * (gravity) ##formula to calculate weight on planet

if planet == 1 or planet == 3:
  print(dest_weight)
elif planet == 2:
  print(dest_weight)
elif planet == 4:
  print(dest_weight)
elif planet == 5:
  print(dest_weight)
elif planet == 6:
  print(dest_weight)
elif planet == 7:
  print(dest_weight)
else:
  print ("Invalid planet number")