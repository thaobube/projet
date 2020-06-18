from random import randint
number = randint(1, 10)

print(number)

guess = int(input("Choose a number between 1 and 10: "))
count = 3

while guess != number and count > 1:

        count -= 1
        if guess < number:
                print("Damn! Too low.")
        elif guess > number:
                print("Damn! Too high.")
        
        print("You can try " + str(count) + " more time(s)")
        guess = int(input("Choose a number between 1 and 10: "))
        
if count == 1 and guess != number:
        print("Game over! The correct guess was " + str(number))

if guess == number:
    print("Great! That's " + str(guess) + " indeed.")


