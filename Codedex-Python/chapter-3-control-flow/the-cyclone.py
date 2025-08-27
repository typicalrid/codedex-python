height=float(input('height: '))
credits=int(input('credits: '))

if height >= 137 and credits >= 10:
  print('Enjoy the ride!')
elif height < 137 and credits >= 10:
  print('You are not tall enough to ride.')
elif height >= 137 and credits < 10:
  print('You dont have enough credits.')
else:
  print('You do not meet any of the requirements to ride. Sorry :(')