import random

ask = str(input("Question: "))

response = ('Yes -definitely.', 
'It is decidedly so.', 
'Without a doubt.', 
'Reply hazy, try again.', 
'Ask again later', 
'Better not tell you now.', 
'My sources say no.', 
'Outlook not so good', 
'Very doubtful')

response_random = random.choice(response)

print("Magic 8 Ball: ", response_random)
