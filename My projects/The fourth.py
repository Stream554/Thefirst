import random
thenumber= random.randint(0,10)
guess1= int(input("Make your first guess:"))
if thenumber==guess1 :
    print("You won!")
else :
    guess2=int(input("One last chance:"))
    if thenumber==guess2 :
        print("You won, close!")
    else :
        print("no no nooooooo")
