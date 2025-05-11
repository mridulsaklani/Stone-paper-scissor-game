import random 
computer = random.choice([1,2,0])

dict = {1: "stone", 0 : 'paper', 2: "scissor"}

myInt = int(input('1 for stone, 0 for paper, 2 for scissor. Chose your num: '))


System = dict[computer]
    

my = dict[myInt]

print(f"you chose {my} and computer choose {System}")

if(System == my):
    print("Match Draw")
    
else:
    if(System == "stone" and my == "paper"):
        print("You are win")
    elif(System == "paper" and my == "stone"):
        print("Computer Win")
    elif(System == "paper" and my == "scissor"):
        print("You Win")
    elif(System == "stone" and my == "scissor"):
        print("Computer Win")
    elif(System == "scissor" and my == "stone"):
        print("You Win")
    elif(System == "scissor" and my == "paper"):
        print("Computer Win")
    else:
        print("something went wrong")


