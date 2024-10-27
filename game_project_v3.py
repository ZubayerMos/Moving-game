def GameMainFunction():
    value = input("Enter 's' to start the game : ")
    
    while(value != "e"):
        value = input("Give a move: ")
        if value == "i":
            movingUp()
        elif value =="k":
            movingDown()
        elif value == "l":
            movingRight()
        elif value == "j":
            movingLeft()
        elif value == "e":
            endGame()
        else:
            continue
            
        
    
def movingRight():
    print ("Moving Right")
    
def movingLeft():
    print ("Moving Left")
    
def movingUp():
    print ("Moving Up")
    
def movingDown():
    print ("Moving Down")

def endGame():
    print("Game Ended.")

GameMainFunction()