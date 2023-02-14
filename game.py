import random
import time

while True:
    print ("Rock Papers Scissors")
    print ("Choose an option : (Press 4 to exit)")
    print ("1. ROCK")
    print ("2. PAPERS")
    print ("3. SCISSORS")
    op = int(input(''))
    cpu = random.randint(1,3)

    if (op==1):
        print ("You chose Rock")
    elif (op==2):
        print ("You chose Papers")
    elif (op==3):
        print ("You chose Scissors")
    elif (op==4):
        print ("Bye have a great time")
        break
    else:
        print ("Invalid Choice. Please try again")

    if (op > 0 and op <=3):
        if (cpu==1):
            print ("CPU chose Rock")
            if (op==1):
                print ("Match Draw")
            elif (op==2):
                print ("You Lose")
            elif (op==3):
                print ("You Win")
        if (cpu==2):
            print ("CPU chose Papers")
            if (op==1):
                print ("You Lose")
            elif (op==2):
                print ("Match Draw")
            elif (op==3):
                print ("You Win")
        if (cpu==3):
            print ("CPU chose Scissors")
            if (op==1):
                print ("You Win")
            elif (op==2):
                print ("You Lose")
            elif (op==3):
                print ("Match Draw")
    time.sleep(2)