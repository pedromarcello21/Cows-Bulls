import random
num = str(random.randint(1000,9999))
#print(num)

guess = str(input("Guess a #\n>>>"))
while len(guess) < 4 or len(guess) > 4:
    guess = str(input("Guess a 4 digit #\n>>>"))
attempts = 1

while guess != num:
    count = 0
    bulls = 0
    cows = 0
    extraBulls = 0
    while count < len(num):
        for i in num:
            if i == guess[count]:
                cows+=1
                guess = guess.replace(guess[count],"X",1)
                count+=1
            elif i in guess:
                bulls+=1
                guess = guess.replace(str(guess.index(i)),"X")
                count +=1
            else:
                count +=1
    guess = str(input(str(cows)+" cow(s) and "+ str(bulls) + " bull(s)\n"+ "Guess another #\n>>>"))
    while len(guess) < 4 or len(guess) > 4:
        guess = str(input("Guess a 4 digit #\n>>>"))
    attempts +=1
print("You got it in "+str(attempts) + " attempt(s)")
    