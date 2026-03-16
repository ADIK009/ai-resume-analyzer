import random

def number_guessing_game():
	print("Welcome to the Number Guessing Game!")
	number = random.randint(1, 20)
	attempts = 0
	while True:
		try:
			guess = int(input("Guess a number between 1 and 20: "))
			attempts += 1
			if guess < number:
				print("Too low!")
			elif guess > number:
				print("Too high!")
			else:
				print(f"Congratulations! You guessed the number in {attempts} attempts.")
				break
		except ValueError:
			print("Please enter a valid integer.")

if __name__ == "__main__": 
	number_guessing_game()


	# that complete the code 