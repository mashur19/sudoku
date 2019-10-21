
sudokuBoard=[[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]]
#welcome to sudoku solver with graphic board
#print('Do want to use the sudoku solver to solve a sudoku board(Y/N)?')
#reading from a file 
print('enter the numbers on sudoku board and type "-" for missing numbers')
fi=open("input1.txt","r")
text=fi.read()
fi.close()
k=0
#get all numbers from the user to solve the sudoku
for i in range(9):
    for j in range(9):
            sudokuBoard[i][j]= text[k]
            k=k+1

                      

#function to display the solved sudoku
def displayBoard(): 
        for i in range(9):
                for j in range(9):
                        print(' '+sudokuBoard[i][j],end=' |')
                print()
        print('---------------------------------------------------------') 
   
#display the sudoku board once before solving
displayBoard()
#funtion to check numbers in a row
def rowChecker(testValue,rowNo):        
        for r in range(9):
               if (sudokuBoard[rowNo][r] in testValue) and (len(sudokuBoard[rowNo][r]) == 1):
                       testValue.remove(sudokuBoard[rowNo][r])
        return testValue

#function to check numbers in column
def columnChecker(testValue,columnNo):        
        for c in range(9):
               if (sudokuBoard[c][columnNo]) in testValue and (len(sudokuBoard[c][columnNo]) == 1):# next condition to not include the long string of numbers
                       testValue.remove(sudokuBoard[c][columnNo])
        return testValue
#group board into sub-blocks of 3*3
def subgroupChecker(testValue,rowNo,columnNo):
        startRow,stopRow,startColumn,stopColumn=0,0,0,0
        if int(rowNo) < 3 and int(columnNo)<3:
                startRow,stopRow,startColumn,stopColumn=0,3,0,3
        elif int(rowNo) < 3 and int(columnNo)<6:
                startRow,stopRow,startColumn,stopColumn=0,3,3,6
        elif int(rowNo) < 3 and int(columnNo)<9:
                startRow,stopRow,startColumn,stopColumn=0,3,6,9
        elif int(rowNo) < 6 and int(columnNo)<3:
                startRow,stopRow,startColumn,stopColumn=3,6,0,3
        elif int(rowNo) < 6 and int(columnNo)<6:
                startRow,stopRow,startColumn,stopColumn=3,6,3,6
        elif int(rowNo) < 6 and int(columnNo)<9:
                startRow,stopRow,startColumn,stopColumn=3,6,6,9
        elif int(rowNo) < 9 and int(columnNo)<3:
                startRow,stopRow,startColumn,stopColumn=6,9,0,3
        elif int(rowNo) < 9 and int(columnNo)<6:
                startRow,stopRow,startColumn,stopColumn=6,9,3,6
        elif int(rowNo) < 9 and int(columnNo)<9:
                startRow,stopRow,startColumn,stopColumn=6,9,6,9
        else:
                print('Unknown Error')


        for r in range(startRow,stopRow):
                for c in range(startColumn,stopColumn):
                        if (sudokuBoard[r][c] in testValue) and (len(sudokuBoard[r][c]) == 1):
                                testValue.remove(sudokuBoard[r][c])
        return testValue

print('Do you want to solve this Board(Y/N)?')
choice = input().lower()
# prepare sublist of every possible number on missing numbers
       
#function to solve the sudoku board

if choice == 'y':
        t=0
        while True:
                k=0     
                for i in range(9):
                    for j in range(9):
                            if sudokuBoard[i][j] == '-':                                                        
                                    sudokuBoard[i][j] = '1 2 3 4 5 6 7 8 9'
                                    test = list(sudokuBoard[i][j].split(' '))                                                                
                                    test = rowChecker(test,i)                                
                                    test = columnChecker(test,j)                                
                                    test = subgroupChecker(test,i,j)                              
                                    sudokuBoard[i][j] = ','.join(test)                                
                            elif len(sudokuBoard[i][j])!=1:
                                    test = list(sudokuBoard[i][j].split(','))                                                                
                                    test = rowChecker(test,i)                                
                                    test = columnChecker(test,j)                                
                                    test = subgroupChecker(test,i,j)                              
                                    sudokuBoard[i][j] = ','.join(test)
                            else:
                                    k=k+1
                t=t+1                      
                if k == 81:
                        break              
                         
                print("\nEnd of round:"+str(t)+'\n')                
                displayBoard()



print('Final Board is ********************************************')
displayBoard()
                        