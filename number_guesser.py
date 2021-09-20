# Made by Devroop Banerjee
# Generate a random number between a range chosen by user
# Tell user whether they need to go higher or lower
# Return the number of attempts it took

import random

print("Please input the range of values from which a random number will be generated. You will have to have to guess this number.")

while True:
	start = input("Starting value for range: ")
	if start.lstrip("-").isdigit(): start = int(start)
	else:
		print("Please enter a number next time!")
		quit()

	end = input("Ending value for range: ")
	if end.lstrip("-").isdigit(): end = int(end)
	else:
		print("Please enter a number next time!")
		quit()

	if end<start:
		print("End of range can not be smaller than the start. Please try again")
	else:
		break

r_num = random.randrange(start, end+1)
attempt = 0

while True:
	answer = int(input("What number do you guess? "))
	attempt +=1
	if (answer > end) or (answer < start):
		print("Please guess a number within the range you provided")
	elif answer > r_num:
		print("Guess lower!")
	elif answer < r_num:
		print("Guess higher!")
	else:
		print("You have correctly guessed the answer after %d attempts" %attempt)
		break