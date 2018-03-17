import random

class Cell:
    def __init__(self):
        self.isOpen = False
        self.isMine = False
        self.isFlag = False
        self.surround = None #no. of surrounding mines
        
    def setMine(self):
        self.isMine= True
        
    def setFlag(self):
        #returns correctFlagCount, setCellCount
        if self.isOpen:
            return 0, 0
        if self.isMine:
            if self.isFlag:
                self.isFlag = False
                return -1, -1
            else:
                self.isFlag = True
                return 1, 1
        return 0, 0
        
    def click(self):
        #returns explodeBool, setCellCount
        if self.isMine:
            return True, 0 #lose
        elif self.isOpen:
            return False, 0
        else:
            self.isOpen = True
            return False, 1
    
    def draw(self, flag):
        if flag == 0:
            return self.drawLimit()
        else:
            return self.drawAll()
    
    def drawLimit(self):
        if self.isOpen:
            return str(self.surround)
        elif self.isFlag:
            return 'F'
        else:
            return ' '
        
    def drawAll(self):
        if self.isMine:
            return 'M'
        elif self.isFlag:
            return 'F'
        else:
            return str(self.surround)
    
class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.numMines = (self.rows*self.cols)//4 #decide how many mines
        self.correctFlagCount = 0
        self.setCellCount = 0
        self.randomize()
        
    def clickCell(self, r, c):
        explode, cellCount = self.grid[r][c].click()
        self.setCellCount += cellCount
        return explode
    
    def flagCell(self, r, c):
        flagCount, cellCount = self.grid[r][c].setFlag()
        self.correctFlagCount += flagCount
        self.setCellCount += cellCount
        
    def findSurrounds(self, r, c):
        neighbours = [(r-1, c-1), (r-1, c), (r-1, c+1),
                      (r, c-1),             (r, c+1),
                      (r+1, c-1), (r+1, c), (r+1, c+1)]
        n = 0
        for x, y in neighbours:
            if x < 0 or x >= self.rows or y < 0 or y >= self.cols:
                pass
            elif self.grid[x][y].isMine:
                n += 1
        return n
    
    def checkComplete(self):
        return (self.rows * self.cols) == self.setCellCount
    def checkWin(self):
        return self.numMines == self.correctFlagCount
    
    def randomize(self):
        mineIndex = random.sample(list(range(0, self.rows*self.cols-1)), self.numMines)
        
        for i in mineIndex:
            self.grid[i//self.rows][i%self.cols].setMine()
            
        #compute surrounds
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c].surround = self.findSurrounds(r, c)
        
    def redraw(self, x):
        todraw = ""
        for r in range(self.rows):
            for c in range(self.cols):
                todraw += '[' + self.grid[r][c].draw(x) + ']'
            todraw += '\n'
        print(todraw)
        
    
def printInstructions():
    print("Game begins!!")
    print("Type c, x, y to 'click' position x, y. Index starting from 0. E.g. c, 1, 2 will open cell[1][2]")
    print("Type f, x, y to 'flag' position x, y. Index starting from 0. E.g. f, 1, 2 will flag cell[1][2]")

    
def main():
    inp = None
    size = 0
    while (size <= 0):
        inp = input("Choose size of minefield: ")
        try:
            size = int(inp)
        except: 
            print("Size given is not a positive integer! Try again.")
        
    grid = Grid(size, size)
    
    printInstructions()
    
    print("FYI! Number of mines : " + str(grid.numMines))
    grid.redraw(0)
    
    explode = False
    
    while(True): #main game loop
        inp = input("Pending input : ")
        if inp.strip() == 'exit':
            break
        try:
            actions = [x.strip() for x in inp.split(',')]
            print(actions)
            x = int(actions[1])
            y = int(actions[2])
            if actions[0] == 'c':
                explode = grid.clickCell(x, y)
                if explode:
                    print("You ded!!!!")
                    grid.redraw(1)
                    break;#end game
            elif actions[0] == 'f':
                grid.flagCell(x, y)
            else:
                print("Unknown action! Try again.")
                
            print(grid.setCellCount)
            if grid.checkComplete() and grid.checkWin():
                print("You won!!!!")
                grid.redraw(1)
                break;#end game
                
        except TypeError:
            print("Incorrect input! Try again.")
        
        grid.redraw(0)
    
if __name__ == '__main__':
    main()