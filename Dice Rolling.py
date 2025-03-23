#  let's write code to play a game of rolling the dice.
# the game should ask user if they want to play the game or not.
# it user says yes then he should be able to roll the dice and see the values.
# if user says no then the game should end.
# import random module to generate random numbers.
# 

import random
import time
while True:
 
 print ('Do you want to play the game?   ' )
 answer = input().lower()

 if answer == 'y':
   print ('Rolling the dice...' )
   time.sleep(2)
   a = random.randint(1,6)
   b = random.randint(1,6)
   print(a,b)

 elif answer =='n':
   print("No problem, see you next time")
   break
 
 else:
   print("Please enter a valid input")
