# importing counter 
from collections import Counter

#initializing counter
house = Counter(
  Gry=0,
  Huf=0,
  Sly=0,
  Rav=0)

#Question 1
Q1 = int(input('Do you like Dawn or Dusk?\n 1)Dawn\n 2)Dusk\nEnter your answer (1-2): '))

if(Q1 == 1):
  house.update(Gry=1, Rav=1)
elif(Q1 == 2):
  house.update(Sly=1, Huf=1)
else:
  print ('Wrong input.')

#Q2
Q2 = int(input("\nWhen I'm dead, I want people to remember me as:\n 1)The Good\n 2)The Great\n 3)The Wise\n 4)The Bold\nEnter your answer (1-4): "))

if(Q2 == 1):
  house.update(Huf=2)
elif(Q2 == 2):
  house.update(Sly=2)
elif(Q2 == 3):
  house.update(Rav=2)
elif(Q2 == 4):
  house.update(Gry=2)
else:
  print ('Wrong input.')

#Q3
Q3 = int(input("\nWhich kind of instrument most pleases your ear?:\n 1)The violin\n 2)The trumpet\n 3)The piano\n 4)The drum\nEnter your answer (1-4): "))

if(Q3 == 1):
  house.update(Sly=4)
elif(Q3 == 2):
  house.update(Huf=4)
elif(Q3 == 3):
  house.update(Rav=4)
elif(Q3 == 4):
  house.update(Gry=4)
else:
  print ('Wrong input.')


print ("\n",house)
print (" Most Points:",house.most_common(1))