''' 1 for snake
    -1 for water
    0 for gun '''
import random
computer = random.choice([1,0,-1])
youstr=input("Enter your choice:")
youDict={"r":1,"p":-1,"s":0}
you=youDict[youstr]
reversedict={1:"Rock",-1:"Paper",0:"Scissors"}
print(f"You have chosen: {reversedict[you]}\nComputer has chosen: {reversedict[computer]}")
if(computer ==you):
  print("Its a draw")
else:
    if (computer ==-1 and you ==1):
        print("You Lose!")
    elif(computer ==-1 and you==0):
        print("You Win!")
    elif(computer == 1 and you ==-1):
        print("You Win!")
    elif(computer ==1 and you==0):
        print("You Lose!")
    elif(computer ==0 and you ==-1):
        print("You lose!")
    elif(computer ==0 and you ==1):
        print("You Win!")
    else:
        print("Something went wrong!")


