print("\n\nSCRABBLE\n\n")
print('''GAME RULES:
        1.you have to form a word from the letters you got randomly from the bag
        2.your score is sum of all the numbers on the letters of your so formed word
        3.some squares in the grid have letters "2L", "3L", "2W" and "3W
        4.2L and 3L doubles and triples the score of letters respectively and 2W and 3W doubles and triples the score of word respectively.
        5.game ends when there are no letters left in the bag.
        6.person with highest score at the end wins the game."''')
global tiles_in_bag
tiles_in_bag = 100
board = [['RC', '1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 '] 
       , ['1 ', '3W', '__', '__', '2L', '__', '__', '__'] 
       , ['2 ', '__', '2W', '__', '__', '__', '3L', '__']         
       , ['3 ', '__', '__', '2W', '__', '__', '__', '2L'] 
       , ['4 ', '2L', '__', '__', '2W', '__', '__', '__'] 
       , ['5 ', '__', '__', '__', '__', '2W', '__', '__'] 
       , ['6 ', '__', '3L', '__', '__', '__', '3L', '__'] 
       , ['7 ', '__', '__', '2L', '__', '__', '__', '2L'] 
       , ['8 ', '3W', '__', '__', '2L', '__', '__', '__']] 
       
     
def display_board(a):
    for i in range(0, 7):
       for j in range(0, 7):
           print(a[i][j],end=' ')
       print('\n')
    return "Board is as above"

display_board(board)
import random
def getRandomRack(n):
    list = []
    
    for i in range(n):
        list.append(random.choice("abcdefghijklmnopqrstuvwxyz"))
    
    return list


score1 = 0
score2 = 0

bag = {"a": 1, "e" : 1, "i" : 1,"l" : 1, "n" : 1, "o" : 1, "r" : 1, "s" : 1, "t" : 1, "u" : 1, "d" : 2, "g" : 2, "b" : 3, "c" : 3, "m" : 3, "p" : 3, "f" : 4, "h" : 4, "v" : 4, "w" : 4, "y" : 4, "k" : 5, "j" : 8, "x" : 8, "q" : 10, "z" : 10}
print(bag)

def putTheword(direction, row, column):
    global l
    
    score = 0
    word = input("Enter the word: ")
    length = len(word)
    
    if direction  == "vertical":
        x = 0
        
        for k in range(row, row + length):
            w = word[x]
            if board[k][column] == "2L":
                score += bag[str(w)]
            if board[k][column] == "3L":
                score += 2 * bag[str(w)]
                 
            
             
            if board[k][column] == "3W":
                l = 3
            if board[k][column] == "2W":
                l = 2  
           
            board[k][column] = str(w) + " "
            score += bag[word[x]]
            x += 1    
        
        if l == 2:
            score *= 2
        if l == 3:
            score *= 3
        l = 0          
        return score
            
    if direction  == "horizontal":
        x = 0
                
        for k in range(column, column + length):

            w= word[x]
            if board[row][k] == "2L":
                score +=  bag[str(w)]
            if board[row][k] == "3L":
                score += 2 * bag[str(w)]
            if board[row][k] == "__":
                score += bag[str(w)] 
            if board[row][k] == "3W":
                l = 3
            if board[row][k] == "2W":
                l = 2  
            board[row][k] = str(w) + " "
            x += 1
        
       
        if l == 2:
            score += score
        if l == 3:
            score += 2 * score
        l = 0
        return score   
   
        
        

def personTurn():
    
    rack = getRandomRack(9)
    print("you got the tiles:",rack)
    global tiles_in_bag
    tiles_in_bag -= 9
    if tiles_in_bag <= 0:
         print("GAME IS OVER")
         print("person 1's score is:", score1)
         print("person 2's score is:", score2)
         if score1 > score2:
             print("PERSON 1 WINS:)")
         elif score1 < score2:
             print("PERSON 2 WINS:)")
         else:
             print("GAME IS TIED")
         exit() 
    
    print("tiles ramaining in the bag:", tiles_in_bag)
    
    row = int(input("enter position to word i.e, row:"))
    column = int(input("enter column:"))
    direction = input("enter the direction to put the word:")
    score = putTheword(direction, row, column)
    
    return score
    
def game():
    global score1
    global score2
    score1 = 0
    score2 = 0
    while True:
        
            
        print("\nPERSON 1'S TURN:\n")
        score1 +=  personTurn() 
        
        display_board(board)
        print("person 1's score is", score1)
        print("person 2's score is", score2)
        
        print("\nPERSON 2'S TURN:\n")
         
        score2 += personTurn()
        display_board(board)
        print("person 1's score is", score1)
        print("person 2's score is", score2)
        
game()
