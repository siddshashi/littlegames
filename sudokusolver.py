board = [
    [8,0,0,0,0,0,6,0,0],
    [0,7,0,1,2,0,0,0,0],
    [0,4,0,0,0,9,2,0,0],
    [0,0,0,3,0,0,5,8,0],
    [1,0,0,0,5,0,0,0,6],
    [0,6,5,0,0,2,0,0,0],
    [0,0,8,4,0,0,0,2,0],
    [0,0,0,0,8,7,0,3,0],
    [0,0,4,0,0,0,0,0,9]
]


# printing board
def print_board(b):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")

# find empty square
def find_empty(b): 
  for i in range(9):
    for j in range(9):
      if b[i][j] == 0: 
        return (i, j) # you get the empty square in as row, col
  return None


# check if the board is valid

def check_valid(b, num, pos):
  
  # check if there is the same number in the row
  for i in range(9):
    if b[pos[0]][i] == num and pos[1] != i: # check entire row, if it's in the position we just inserted, we don't care
      return False
  
  #check column
  for i in range(9):
    if b[i][pos[1]] == num and pos[0] != i: 
      return False
  
  # check box
  # first, figure out which box we are in, use integer division
  box_x = pos[1] // 3
  box_y = pos[0] // 3

  for i in range(box_y * 3, box_y * 3 + 3): 
    for j in range(box_x * 3, box_x * 3 + 3): 
      if b[i][j] == num and (i,j) != pos: 
        return False
  
  return True

def solve(b): 
  find = find_empty(b)
  if not find: 
    return True
  else: 
    row, col = find

  for i in range(1,  10): 
    if check_valid(b, i, (row, col)):
      b[row][col] = i

      if solve(b): 
        return True

      b[row][col] = 0

  return False


print_board(board)
solve(board)
print("solution:  ")
print_board(board)    