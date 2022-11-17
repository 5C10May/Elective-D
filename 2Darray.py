arr = [ ['-','-','-'],
        ['-','-','-'],
        ['-','-','-']]

last_played = 'O'

i = 0
last_played = 'O'
game_over = False

while i != -1 and game_over == False:

    i,j = map(int, input('Enter row and column (1-3). enter -1 -1 to quit').split())
    if i == -1:
        break								#break the loop and quit
    
    if i > 3 or j > 3:
        print('Error: should be within the range! ')
        continue    							#by-pass this iteration
    elif  arr[i-1][j-1] != '-':
        print('Error: already occupied! ')
        continue    
    
    if last_played == 'O':
       last_played = 'X'
       print('Player X played:')
    else:
       last_played = 'O'
       print('Player O played:')
    arr[i-1][j-1] = last_played
        
    #print the 2D array
    for a in range(3):
        for b in range(3):
            print(arr[a][b], end=' ')
        print()
    
    r = 0
    for i in range(3):        
        if arr[i][0] != '-' and arr[i][0] == arr[i][1] and arr[i][1] == arr[i][2]:  #horizontal case
            game_over = True
            winner = "Winner: " + arr[i][0]
        elif arr[0][i] != '-' and arr[0][i] == arr[1][i] and arr[1][i] == arr[2][i]:  #vertical case
            game_over = True
            winner = "Winner: " + arr[0][i]
        elif arr[0][0] != '-' and arr[0][0] == arr[1][1] and arr[1][1] == arr[2][2]:  #斜1
            game_over = True
            winner = "Winner: " + arr[0][0]
        elif arr[0][2] != '-' and arr[0][2] == arr[1][1] and arr[1][1] == arr[2][0]:  #斜2
            game_over = True
            winner = "Winner: " + arr[0][2]
        elif arr[i][0] != '-' and arr[i][1] != '-' and arr[i][2] != '-':  #draw case
            r = r+1
            if r == 3:  #how many row(s) have been occupied
                game_over = True
                winner = "Draw"
    
print('Game Over -- ' + winner)
