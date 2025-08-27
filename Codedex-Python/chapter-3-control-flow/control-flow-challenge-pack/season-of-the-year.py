month = int(input("enter a month number: "))

if month == 1 or month == 2 or month == 3:
  print ("Winter 🌨️")
elif month >= 4 and month <= 6:
  print ("Spring 🌱")
elif month >= 7 and month <= 9:
  print ("Summer 🌻")
elif month >= 10 and month <= 12:
  print ("Autumn 🍂")
else:
  print ("Invalid")