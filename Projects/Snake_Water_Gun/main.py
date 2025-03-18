import random

'''
1 from Snake
-1 for Water
0 from gun
'''

Computer = random.choice([-1,0,1])
youChoose = input("Enter Your Choice: ")
yourDictionary = {'s': 1, 'w': -1 , 'g' : 0}
reverseDictionary = {1: 's', -1 : 'w', 0 : 'g'}

you = yourDictionary[youChoose]

print(f"You Choose {reverseDictionary[you]} \nComputer choose {reverseDictionary[Computer]}")

if(Computer == you):
    print("Tie!")
else:
    if(Computer == -1 and you == 1):
        print("You Win!")
    elif(Computer == -1 and you ==0):
        print("You Lose!")  
    elif(Computer == 1 and you == 0):
        print("You Win!")
    elif(Computer == 1 and you == -1):
        print("You Lose!")  
    elif(Computer == 0 and you == 1):
        print("You Lose!")
    elif(Computer == 0 and you == -1):
        print("You Win!")

    else:
        print("Something Went Wrong!")    