import random

player = random.randint(1,6)
cpu    = random.randint(1,6)

if player>cpu:
	print('You win')
else :
	print ('you lose')	
