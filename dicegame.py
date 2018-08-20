import random

player = random.randint(1,6)
cpu    = random.randint(1,6)


print( 'You rolled {}'.format(player))
print( 'Computer  rolled {}'.format(cpu))

if player>cpu:
	print('You win')
else :
	print ('you lose')	
