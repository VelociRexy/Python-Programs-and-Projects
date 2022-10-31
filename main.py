def sum(a,b,c):
  return a+b+c

def printBoard(xstate,ostate):
#Defining each block status for each turn
  one='X' if(xstate[0]==1) else('O' if(ostate[0]==1) else ' ')
  two='X' if(xstate[1]==1) else('O' if(ostate[1]==1) else ' ')
  three='X' if(xstate[2]==1) else('O' if(ostate[2]==1) else ' ')
  four='X' if(xstate[3]==1) else('O' if(ostate[3]==1) else ' ')
  five='X' if(xstate[4]==1) else('O' if(ostate[4]==1) else ' ')
  six='X' if(xstate[5]==1) else('O' if(ostate[5]==1) else ' ')
  seven='X' if(xstate[6]==1) else('O' if(ostate[6]==1) else ' ')
  eight='X' if(xstate[7]==1) else('O' if(ostate[7]==1) else ' ')
  nine='X' if(xstate[8]==1) else('O' if(ostate[8]==1) else ' ')
#Printing my board 
  #if one==':'
  print(f" {one} | {two} | {three} ")
  print(f"---|---|---")
  print(f" {four} | {five} | {six} ")
  print(f"---|---|---")
  print(f" {seven} | {eight} | {nine} ")

#Function that checks winner--> Returns 1 if X won , 0 if O won or -1 if match is drawn
def checkWinner(xstate,ostate,turn):
  win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]#List that contains different lists having different ways of winning

  for item in win:
    #Loop that checks for all the combination
    if( sum(xstate[item[0]],xstate[item[1]],xstate[item[2]])==3):
      printBoard(xstate,ostate)
      print("X won")
      return 1
    if( sum(ostate[item[0]],ostate[item[1]],ostate[item[2]])==3):
      printBoard(xstate,ostate)
      print("O won")
      return 0
# Match drawn=> All blocks are filled and above ifs are not executed--> Possible when turn>9
  if turn>9:
    printBoard(xstate,ostate)
    print("Match drawn")
    return -1
#End of above function

#Program execution begins here
print("Welcome to Tic Tac Toe")
xstate=[0,0,0,0,0,0,0,0,0]#Refers to turns of X
ostate=[0,0,0,0,0,0,0,0,0]#Refers to turns of O
turn=1 #1 for X 0 for O

#Game Loop that executes till game does not end 
while True:
  printBoard(xstate,ostate)
  if(turn%2 == 1):
    x="X'S Turn"
    print(f'{x:.^20}')
    value=int(input("Please Enter  Position : "))-1
    if(value>8 or value<0):
      print("Invalid Value... Enter again\n")
      turn-=1
    else:
      if(xstate[value]==1 or ostate[value]==1):
        print(f"Position {value+1} is already occupied")
        turn-=1
      else:
        xstate[value]=1
  else:
    o="O'S Turn"
    print(f"{o:.^20}")
    value=int(input("Please enter a value : "))-1
    if(value>8 or value<0):
      print("Invalid Value... Enter again\n")
      turn-=1
    else:
      if(xstate[value]==1 or ostate[value]==1):
        print(f"Position {value+1} is already occupied")
        turn-=1
      else:
        ostate[value]=1
  turn+=1
  win = checkWinner (xstate,ostate,turn)#Invoking checkWinner function after each turn
  if(win == 1 or win == 0 or win == -1):
    break

