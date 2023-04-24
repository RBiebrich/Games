# variables
players = ['Player 1', 'Player 2']
chars = [None, None]

columns = ['1', '2', '3', '4', '5', '6', '7']
top = '''
      1   2   3   4   5   6   7
   ╔═════════════════════════════╗'''
clean_row = '   ║ ( ) ( ) ( ) ( ) ( ) ( ) ( ) ║'
row1 = row2 = row3 = row4 = row5 = row6 = row7 = clean_row

bottom = '   ╚═════════════════════════════╝'

rows = [row1, row2, row3, row4, row5, row6, row7]
positions = [6, 10, 14, 18, 22, 26, 30]
row_counts = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0,}

# formatting funcs
def buffer(lines):
    s = ''
    for i in range(lines):
        s += '\n'
    print(s)

def barrier(length):
    s = ''
    for i in range(length):
        s += '='
    print(s)

def cont():
    input('press enter to continue...')
    buffer(50)

def board():
    print (top)
    for row in rows[::-1]:
        print(row)
    print(bottom)

# the welcome screen
buffer(6)
print('                          WELCOME TO CONNECT 4!')
print('                      A project by Robert Biebrich')
buffer(2)
print('                      [press enter to continue...]')
buffer(2)
barrier(72)
input()
buffer(50)

# the setup
for i in range(len(players)):
    while True:
        name = str(input(players[i]+', enter your name: ')).capitalize()
        if len(name) > 20:
            print('Please pick a shorter name.')
            continue
        elif name in players:
            print('You must pick a unique name.')
        elif len(name) < 1:
            name = players[i]
            break
        else:
            response = ''
            while response != 'Y' and response != 'N':
                print('Your name is ' + name + '. Is that correct?')
                response = input('(Y / N)')
                response = response.upper()
                if response != 'Y' and response != 'N':
                    print('Please respond with either Y for yes or N for no.')
            if response == 'N':
                continue
            else:
                players[i] = name
                print(players)
                break
    buffer(50)
    print('Hi ' + name + '!')
    buffer(1)

    while True:
        char = str(input(name + ', select your character from the keyboard: ')).upper()
        if len(char) != 1:
            print('You must select a single character to play!')
        elif char in chars:
            print('You must pick a unique character.')
        else:
            chars[i] = char
            print(name + ', you selected', chars[i])
            break

    cont()
player1 = players[0]
char1 = chars[0]
player2 = players[1]
char2 = chars[1]

# the game
print ('THE GAME WILL NOW BEGIN!')


def updateRow(selected, char):
    index = selected*4+2
    check = 0
    for row in range(len(rows)):
        if rows[row][index] == ' ':
            rows[row] = rows[row][:index] + char + rows[row][index+1:]
            check += 1
            break
        else:
            continue
    return check

def checkConnect():

    #check across
    for row in rows:
        char1_count = 0
        char2_count = 0
        for pos in positions:
            if row[pos] == char1:
                char1_count += 1
                char2_count = 0
            elif row[pos] == char2:
                char2_count += 1
                char1_count = 0
            else:
                char1_count = 0
                char2_count = 0
            if char1_count == 4:
                return 0
            elif char2_count == 4:
                return 1
    
    #check down
    for pos in positions:
        char1_count = 0
        char2_count = 0
        for row in rows:
            if row[pos] == char1:
                char1_count += 1
                char2_count = 0
            elif row[pos] == char2:
                char2_count += 1
                char1_count = 0
            if char1_count == 4:
                return 0
            elif char2_count == 4:
                return 1

    #check diagonal

    #sloping down to the right
    #GLITCHES SEEM TO OCCUR HERE, NOT IN DOWN TO LEFT
    for i in range(13):
        char1_count = 0
        char2_count = 0

        if i <= 7:
            index = len(rows[:i])-1

            for r in range(len(rows[:i])):
                if rows[r][positions[index]] == char1:
                    char1_count += 1
                    char2_count = 0
                elif rows[r][positions[index]] == char2:
                    char2_count += 1
                    char1_count = 0
                if char1_count == 4:
                    return 0
                elif char2_count == 4:
                    return 1
                index -= 1
        else:
            count = i-7
            index = len(rows[:-1])

            for r in range(count, 7):
                if rows[r][positions[index]] == char1:
                    char1_count += 1
                    char2_count = 0
                elif rows[r][positions[index]] == char2:
                    char2_count += 1
                    char1_count = 0

                if char1_count == 4:
                    return 0
                elif char2_count == 4:
                    return 1
                index -= 1
            count += 1
        
        # sloping down to the left
        for i in list(range(13))[::-1]:
            char1_count = 0
            char2_count = 0
            if i < 7:
                index = i
                for r in range(6-i, 7)[::-1]:
                    if rows[r][positions[index]] == char1:
                        char1_count += 1
                        char2_count = 0
                    elif rows[r][positions[index]] == char2:
                        char2_count += 1
                        char1_count = 0

                    if char1_count == 4:
                        return 0
                    elif char2_count == 4:
                        return 1
                    index -= 1
            else:
                index = 6
                for r in list(range(13-i))[::-1]:
                    if rows[r][positions[index]] == char1:
                        char1_count += 1
                        char2_count = 0
                    elif rows[r][positions[index]] == char2:
                        char2_count += 1
                        char1_count = 0

                    if char1_count == 4:
                        return 0
                    elif char2_count == 4:
                        return 1
                    index -= 1
        

while True:
    for i in range(len(players)):
        board()
        check = 0
        while check == 0:
            select = input(players[i]+ ' select a column...')
            if select not in columns:
                buffer(50)
                board()
                print('Column must be a number from 1 to 7!')
                continue
            elif row_counts[select] == 7:
                buffer(50)
                board()
                print('That column is already full!')
            else:
                row_counts[select] += 1
                select = int(select)
                check = updateRow(select, chars[i])
                buffer(50)
        winner = checkConnect()
        if winner != None:
            break
        elif sum(row_counts.values()) == 49:
            buffer(50)
            board()
            input('The board is full! Press enter to reset the board...')
            row1 = row2 = row3 = row4 = row5 = row6 = row7 = clean_row
            rows = [row1, row2, row3, row4, row5, row6, row7]
            buffer(50)
            continue

            
    buffer(50)
    if winner != None:
        board()
        print(players[winner].upper(), 'WINS!!!')
        cont()

    else:
        buffer(50)
        continue

    # post game
    print('GAME OVER!')

    while True:
        print('Would you like to play again?')
        response = input('(Y / N)')
        response = response.upper()
        if response != 'Y' and response != 'N':
            print('Please respond with either Y for yes or N for no.')
        else:
            break
    if response == 'N':
        break
    else:
            row1 = row2 = row3 = row4 = row5 = row6 = row7 = clean_row
            rows = [row1, row2, row3, row4, row5, row6, row7]
            row_counts = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0,}
            buffer(50)
            continue


buffer(50)
print('THANKS FOR PLAYING!!!\n')
input('[Press enter to close the game...]')