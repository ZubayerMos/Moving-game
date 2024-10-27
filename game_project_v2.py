def GameMainFunction():
    value = input("Give a move: ")
    if value == "i":
        movingUp()
    elif value =="k":
        movingDown()
    elif value == "l":
        movingRight()
    elif value == "j":
        movingLeft()
    else :
        pass
        
    
def movingRight():
    print ("Moving Right")
    
def movingLeft():
    print ("Moving Left")
    
def movingUp():
    print ("Moving Up")
    
def movingDown():
    print ("Moving Down")
    

GameMainFunction()