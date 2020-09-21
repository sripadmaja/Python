import random
number=random.randint(1,100)#computer will generate a number between 1 to 10
name=input("HELLO WHAT'S YOUR NAME")
print("okay" +name+ "guess a number between 1 to 100")
def ng(n):
    guess=int(input("guess a number:"))
    if n>5:
        print("you lost the game")
        return
    if guess!=number and guess>number:
        print("your guess is too high")
        return ng(n+1)
    elif guess!=number and guess<number:
        print("your output is too low")
        return ng(n+1)
    else:
        if guess==number:
            print("you won the game")
ng(1)

