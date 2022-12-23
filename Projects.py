#Taking input from the user in the form of list as Initial Puzzle problem Matrix.
print("Enter the Initial State Of the tiles")
current=[]                              #empty list defined
str=input()                             #First row of current matrix is taken in form of a string.

for i in range(len(str)):
    if ord(str[i]) in range(48,58):     #ord function is used to calculate the ASCII value of str[i] which is a character.
        current.append(int(str[i]))     #This will append str[i] as integer into current list.

str1=input()                            #Second row of current matrix(input).
for i in range(len(str1)):
    if ord(str1[i]) in range(48,58):
        current.append(int(str1[i]))

str2=input()                             #Third row of current matrix(input).
for i in range(len(str2)):
    if ord(str2[i]) in range(48,58):
        current.append(int(str2[i]))


#Taking input from the user in the form of list as Puzzle Goal Matrix.
print("Enter the Goal You Want to Achieve:")
goal=[]                                 #empty list defined
str=input()                             #First row of goal matrix is taken in form of a string.

for i in range(len(str)):
    if ord(str[i]) in range(48,58):       #ord function is used to calculate the ASCII value of str[i] which is a character.
        goal.append(int(str[i]))          #This will append str[i] as integer into goal list.

str1=input()                            #Second row of goal matrix(input).
for i in range(len(str1)):
    if ord(str1[i]) in range(48,58):
        goal.append(int(str1[i]))

str2=input()                            #Third row of goal matrix(input).
for i in range(len(str2)):
    if ord(str2[i]) in range(48,58):
        goal.append(int(str2[i]))


#Checking the inversion no. of the Current as Well as Goal Lists:
#(INversion No: For every element of the list sum the no. of elements which are smaller
# than it and neither of them equal to zero.Take the Sum for all Elements of the list.)

currentCt=0                             #This stores the inversion count of current list.
for i in range(9):
    for j in range(i+1,9):
        if(current[j]<current[i] and current[i]!=0 and current[j]!=0):
            currentCt=currentCt+1

goalCt=0                                #This stores the inversion count of goal list.
for i in range(9):
    for j in range(i+1,9):
        if(goal[j]<goal[i] and goal[i]!=0 and goal[j]!=0):
            goalCt=goalCt+1


#Function for printing the Puzzle Matrix solved so far(modified current matrix).
def Matrixprint(array):
    for i in range(9):
        #Printing a new line after every 3 tiles.
        if i%3 == 0 and i > 0:
            print("")
        
        #Printing the tiles.
        print(array[i]," ", end = "")


# Function for calculating the Heuristic count for Puzzle Matrix solved so far.
def heuristicCount(l):
    #Below Variable initiates the heuristic count.
    c = 0

    #Loop that iterates through all the tiles of unsolved puzzle and compares that every tile with
    #the corresponding tile of Goal Matrix. If they don't match, then increase the heuristic count by 1.
    for i in range(9):
        if (l[i] != 0 and l[i] != goal[i]):
            c += 1
            
    #return the counted heuristic value:    
    return c

# Function for Updating the Puzzle Matrix solved so far (puzzle state) to reach the goal.
def updateMatrix(ar, p, st):
    
    #variable that stores minimum heuristic value of a moved state
    maxhur = 10
    
    #Copy the puzzle state to another list variable to be used in here.
    store_string = st.copy()
    
    #Loop that makes moves of blank tiles to all possible positions
    for i in range(len(ar)):
        
        #Copying the current puzzle state to another list variable to be
        #used in the swapping blank tile operation.
        dupl_sting = st.copy()
        
        #swapping(with temp variable creted dynamically) the blank tile.
        temp = dupl_sting[p]
        dupl_sting[p] = dupl_sting[ar[i]]
        dupl_sting[ar[i]] = temp
        
        #counting the heuristic value for swaped puzzle state.
        revised_mh = heuristicCount(dupl_sting)
        
        #if current swaped puzzle state has the less heuristic value than
        #the before one, then store current Puzzle state and current heuristic value
        if (revised_mh < maxhur):
            maxhur = revised_mh
            store_string = dupl_sting.copy()
      
    #Return the Puzzle state with the minimum heuristic value(in form of a list) along with the heuristic value.
    return store_string, maxhur


#Creating a Blank Dictionary as myDict.
#This will store all the the Puzzle states lists as "values" with corresponding "key" as(operation number).
#starting from first operation till a maximum of 10.
myDict ={}

#Checking the condition whether the Puzzle State"current" given as input can be converted into Goal or not. 
if((currentCt + goalCt)%2==0):             #If it can be converted then:

    hur = heuristicCount(current)            #Stores the initial heuristicCount of the Puzzle state.             
    
    Level = 0                              #Keeps track of search levels.
    
    myDict.update({Level:current})         #Updating the dictionary for first pair of key and value
    
    
    #The main loop to find the solution and printing every search level with operation number 
    # and Puzzle State solved so far(as Matrix).
    while (hur>0 and Level<=10):
        #Store the position of the blank tile labeled '0' in the updated list 'current'.
        zeroIndex = int(current.index(0))
        
        #Increasing level as one level of search is executing now
        Level += 1
        
        #If blank tile is in index 0, then  all possible movement operation
        if zeroIndex == 0:
            #array of indexes where blank tile can be moved
            Possiblities = [1, 3]
            current, hur = updateMatrix(Possiblities, zeroIndex, current)
            
        #if blank tile is at index 1, then all possible movement operation
        elif zeroIndex == 1:
            #array of indexes where blank tile can be moved
            Possiblities = [0, 2, 4]
            current, hur = updateMatrix(Possiblities, zeroIndex, current)
            
        #if blank tile is in index 2, then all possible movement operation    
        elif zeroIndex==2:
            #array of indexes where blank tile can be moved
            Possiblities = [1, 5]
            current, hur = updateMatrix(Possiblities, zeroIndex, current)
            
        #if blank tile is in index 3, then possible all movement operation
        elif zeroIndex==3:
            #array of indexes where blank tile can be moved
            Possiblities = [0, 4, 6]
            current, hur = updateMatrix(Possiblities, zeroIndex, current)
            
        #if blank tile is in index 4, then possible all movement operation
        elif zeroIndex==4:
            #array of indexes where blank tile can be moved
            Possiblities = [1, 3, 5, 7]
            current, hur = updateMatrix(Possiblities, zeroIndex, current)
            
        #if blank tile is in index 5, then possible all movement operation
        elif zeroIndex==5:
            #array of indexes where blank tile can be moved
            Possiblities = [2, 4, 8]
            current, hur = updateMatrix(Possiblities, zeroIndex, current)
            
        #if blank tile is in index 6, then possible all movement operation
        elif zeroIndex==6:
            #array of indexes where blank tile can be moved
            Possiblities = [3, 7]
            current, hur = updateMatrix(Possiblities, zeroIndex, current)
            
        #if blank tile is in index 7, then possible all movement operation
        elif zeroIndex==7:
            #array of indexes where blank tile can be moved
            Possiblities = [4, 6, 8]
            current, hur = updateMatrix(Possiblities, zeroIndex, current)
            
        #if blank tile is in index 8, then all possible movement operation
        elif zeroIndex==8:
            #array of indexes where blank tile can be moved
            Possiblities = [5, 7]
            current, hur = updateMatrix(Possiblities, zeroIndex, current)
        

        myDict.update({Level:current})             #Updating the dictionary that will store the level(key) and puzzle state as value.

    if(Level<=10):                                 #If the Levels are less than or equal to 10 then print all Puzzle States.
        print("Goal State can be achieved in Less than 10 operations.")
        for i in range(Level):
            print("After Operation",i+1,"Puzzle state:")
            Matrixprint(myDict[i+1])
            print("\n")
        print("Total operations required:",Level)

    else:
        print("Goal state can be achieved but required more than 10 steps")     #If Level goes above 10 and puzzle is sovable then print this.

else:                                                   #If the Puzzle is not solvable(currentCt + goalCt is not a multiple of 2).
    print("Goal state can't be achieved with given Puzzle problem state")   #then print this.
