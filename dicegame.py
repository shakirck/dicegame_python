import random
import time
player = random.randint(1,6)
cpu    = random.randint(1,6)

def dice_game():
	print( 'You rolled {}'.format(player))
	
	print('Computer\'s Turn............')
	time.sleep(3) 
	print( 'Computer  rolled {}'.format(cpu))
	
	if player>cpu:
		print('You win')
	elif player == cpu: 
		print('The game is a tie')
	else :
		print ('you lose')	

	print('Quit: Y/N')


	choice = input()

	if choice == 'Y' or choice == 'y':
		exit()
	if choice == 'N' or choice =='n' :
		pass
	else :
		print ('Unknown Input...Game will Quit')
		exit()

while True:
	print("Press any key")
	enter=input()
	dice_game()