import time 
import copy

size = 10 #10x10
matrix = [[0 for x in range(size)] for y in range(size)]

def start_game():
    # init
    global matrix
    matrix[0][2] = 1
    matrix[1][0] = 1
    matrix[1][2] = 1
    matrix[2][1] = 1
    matrix[2][2] = 1
    
    # run!
    starttime=time.time() 
    while True: 
        run_step()
        time.sleep(1.0 - ((time.time() - starttime) % 1.0)) # run every 1 sec
        


def count_live_neighbours(a,b):
    global matrix
    total=0
    if a > 0:
        total+=matrix[a-1][b]
        if b > 0:
            total+=matrix[a-1][b-1]
        if b < size-1:
            total+=matrix[a-1][b+1]
    if a < size-1:
        total+=matrix[a+1][b]
        if b > 0:
            total+=matrix[a+1][b-1]
        if b < size-1:
            total+=matrix[a+1][b+1]
    if b > 0:
        total+=matrix[a][b-1]
    if b < size-1:
        total+=matrix[a][b+1]
    return total

def run_step():
    global matrix
    print("\033[H\033[J", end="") #clear scr
    
    new_matrix=copy.deepcopy(matrix)
    for a in range(size): #next step
        for b in range(size):
            count = count_live_neighbours(a,b)
            if matrix[a][b] == 1:
                if count<2:
                    new_matrix[a][b] = 0
                elif count>3:
                    new_matrix[a][b] = 0
                else:
                    new_matrix[a][b] = 1
            elif matrix[a][b] == 0:
                if count==3:
                    new_matrix[a][b] = 1
            # for debug purposes
            #print (("♥" if matrix[a][b]==1 else "‧") +f"({str(count)}) ", end="") #draw
            #prod        
            print (("  ♥  " if matrix[a][b]==1 else "  ‧  "), end="") #draw the current matrix
        print ("\n") 
    matrix = copy.deepcopy(new_matrix) #then replace the old one with the new calculated






#test
start_game()    
# print(str(matrix))