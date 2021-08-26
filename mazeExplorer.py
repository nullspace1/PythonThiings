import random

def mazeConstructor(X,Y):
    newMaze = []
    for x in range(X):
        row = []
        for y in range(Y):
            cell = Cell(x,y)
            row.append(cell)
        newMaze.append(row)
    return newMaze

class Cell :
    def __init__(self,xCoord,yCoord):
        self.coordinates = (xCoord,yCoord)
        self.connected = []
        self.hasBeenVisited = False
    def Connect(self,PairTuple):
        self.connected.append(PairTuple) 

class Maze :

    def __init__(self):
        self.height = 10
        self.width = 10
        self.maze = mazeConstructor(10,10)
        self.howManyVisited = 0
        self.stack = [(0,0)]
        self.maze[0][0].hasBeenVisited = True
    
    def visitCell(self,previousCellCoordinates,newCellCoordinates): 
        xOld = previousCellCoordinates[0]
        yOld = previousCellCoordinates[1]
        self.howManyVisited += 1
        self.maze[xOld][yOld].hasBeenVisited = True
        self.stack.append(newCellCoordinates)
    # takes the previous cell coordinates and goes to the new cell and connects the previous
    # cell to the new one via cell.Connect
    # updates howManyVisited and adds the newCellCoordinates to the stack.
    # Sets the new cell to visited.

    def notAllExplored(self):
        for x in range(self.width):
            for y in range(self.height):
               cell = self.maze[x][y]
               if (cell.hasBeenVisited == False):
                    return True
        return False

    def getAvailableCellNeighbours(self,currentCell): 
        listOfCells = []
        x = currentCell[0]
        y = currentCell[1]
        if (x < (self.width - 1)): 
            if(self.maze[x+1][y].hasBeenVisited == False):listOfCells.append(self.maze[x+1][y].coordinates)
        if (x > 0): 
            if(self.maze[x-1][y].hasBeenVisited == False): listOfCells.append(self.maze[x-1][y].coordinates)
        if (y < (self.height - 1)): 
            if(self.maze[x][y+1].hasBeenVisited) == False: listOfCells.append(self.maze[x][y+1].coordinates)
        if (y > 0): 
            if(self.maze[x][y-1].hasBeenVisited == False): listOfCells.append(self.maze[x][y-1].coordinates)
        return listOfCells


def getRandomNeighbour(ListOfNeighbours,seed):
    length = len(ListOfNeighbours)
    randomStep = random.randrange(-1,length)
    cell = ListOfNeighbours[randomStep]
    return cell

def createMaze(mazeObject,seed):
    while(mazeObject.notAllExplored()): 
        currentCell = mazeObject.stack[-1]
        print(currentCell)
        ListOfNeighbours = mazeObject.getAvailableCellNeighbours(currentCell)
        if (len(ListOfNeighbours) > 0):
            randomCell = getRandomNeighbour(ListOfNeighbours,seed)
            mazeObject.visitCell(currentCell,randomCell)
        else:
           x = currentCell[0]
           y = currentCell[1]
           mazeObject.maze[x][y].hasBeenVisited = True 
           mazeObject.stack.pop()
            


def main():
    mazeObject = Maze()
    createMaze(mazeObject,348223)
    print(mazeObject.howManyVisited)
    
if __name__ == "__main__":
    main()