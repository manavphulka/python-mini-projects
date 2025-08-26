import random
'''

-1 = water
0 = gun
1 = snake 

'''
comp = random.choice([1,-1,0])

youStr = input("Enter your choice: ")
youDict= {"s":1,"w":-1,"g":0}
reverseDict = {1:"Snake",-1:"Water",0:"Gun"}

you = youDict[youStr]

print(f"you chose {reverseDict[you]}\n computer chose {reverseDict[comp]}")

if(comp==you):
    print("DRAW")

else:
    if(comp == -1 and you == 1):
        print("YOU WON!")
    elif(comp == 1 and you == 0):
        print("YOU WON!")
    elif(comp == -1 and you == 0):
        print("YOU WON!")
    elif(comp == 0 and you == -1):
        print("YOU LOST")
    elif(comp == 0 and you == 1):
        print("YOU LOST")
    elif(comp == 1 and you == -1):
        print("YOU LOST")
    else:
        print("ERRO 404")