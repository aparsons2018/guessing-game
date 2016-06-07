#Austin Parsons

import random #random number 
computerNumber = random.randint(1,100) 
guesses = []
play = True
while play == True:
	number = input("Guess a number between 1 and 100 or press 'q' to quit. ")
	if number == 'q':
		print("Too bad. Better luck next time.")
		play = False
	elif computerNumber > int(number):
		guesses.append(number)
		print("Too low. ")
	elif computerNumber < int(number):
		guesses.append(number)
		print("Too high. ")
	elif computerNumber == int(number):
		print("That's the number! Good Job")
		guesses.append(number)
		guesses.sort()
		final = ""
		bestGuess = guesses[-1] #most resent guess/winning guess
		if number == bestGuess:
			guesses.remove(bestGuess) #remove bestGuess so you can replace it
			bestGuess = "*{}*".format(bestGuess) #remove bestGuess so that you can give it **
		else:
			guesses.remove(bestGuess)
			index = guesses.index(number)
			guesses.remove(number)
			number = "*{}*".format(number)
			guesses.insert(index,number)
		for number in guesses:
			final += "{}, ".format(number)
		final += str(bestGuess)
		print("Your guesses were: {}".format(final))
		play = False 