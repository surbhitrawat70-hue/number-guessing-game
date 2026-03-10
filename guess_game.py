import random

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")
print("You have 3 chances!")

random_number = random.randint(1, 100)

for i in range(3):
    user_number = int(input("Enter your guessing number: "))

    if user_number < random_number:
        print("Too low! Try again.")

    elif user_number > random_number:
        print("Too high! Try again.")

    else:
        print("Congratulations! You guessed the number!")
        break

else:
    print("Sorry, you lost!")
    print("The correct number was:", random_number)