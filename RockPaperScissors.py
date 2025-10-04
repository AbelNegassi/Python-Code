# Rock Paper Scissors Game! 
# Ask the user for an input (Either R, P, or S). Then generate a random variable. 
# Classic rock paper scissors rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock
import random
print("Welcome to Rock Paper Scissors! Enter R for Rock, P for Paper, or S for Scissors!")
player = input()
randRPSNum = random.randint(1,3)
if randRPSNum == 1:
    randRPS = "R"
elif randRPSNum == 2:
    randRPS = "P"
else:
    randRPS = "S"

if (player == "R") & (randRPS == "R"):
    print("Its a draw!")
elif (player == "P") & (randRPS == "P"):
    print("Its a draw!")
elif (player == "S") & (randRPS == "S"):
    print("Its a draw!")
elif (player == "R") & (randRPS == "P"):
    print ("You lose!")
elif (player == "R") & (randRPS == "S"):
    print ("You Win!")
elif (player == "P") & (randRPS == "S"):
    print ("You lose!")
elif (player == "P") & (randRPS == "R"):
    print ("You Win!")
elif (player == "S") & (randRPS == "R"):
    print ("You lose!")
elif (player == "S") & (randRPS == "P"):
    print ("You Win!")
else:
    print ("Please make sure to follow the instructions and ONLY enter either R, P, or S. Thank you!")