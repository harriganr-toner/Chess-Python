import pygame, math

pygame.init()

# Assets
whitePawn = pygame.image.load("pawn.png")
whiteKnight = pygame.image.load("knight.png")
whiteBishop = pygame.image.load("bishop.png")
whiteRook = pygame.image.load("rook.png")
whiteQueen = pygame.image.load("queen.png")
whiteKing = pygame.image.load("king.png")
blackPawn = pygame.image.load("blackPawn.png")
blackKnight = pygame.image.load("blackKnight.png")
blackBishop = pygame.image.load("blackBishop.png")
blackRook = pygame.image.load("blackRook.png")
blackQueen = pygame.image.load("blackQueen.png")
blackKing = pygame.image.load("blackKing.png")
whitePawn = pygame.transform.smoothscale(whitePawn, (40, 40))
whiteKnight = pygame.transform.smoothscale(whiteKnight, (40, 40))
whiteBishop = pygame.transform.smoothscale(whiteBishop, (40, 40))
whiteRook = pygame.transform.smoothscale(whiteRook, (40, 40))
whiteQueen = pygame.transform.smoothscale(whiteQueen, (40, 40))
whiteKing = pygame.transform.smoothscale(whiteKing, (40, 40))
blackPawn = pygame.transform.smoothscale(blackPawn, (40, 40))
blackKnight = pygame.transform.smoothscale(blackKnight, (40, 40))
blackBishop = pygame.transform.smoothscale(blackBishop, (40, 40))
blackRook = pygame.transform.smoothscale(blackRook, (40, 40))
blackQueen = pygame.transform.smoothscale(blackQueen, (40, 40))
blackKing = pygame.transform.smoothscale(blackKing, (40, 40))

# Movement Variables
legalMoves = []
clickNum = 0
startX = 0
startY = 0
turn = "white"
enPassantTarget = None

# Knight = 2
# Bishop = 3
# Rook = 4
# Queen = 5
# King = 6
board = [["b4", "b2", "b3", "b5", "b6", "b3", "b2", "b4"],
         ["b1", "b1", "b1", "b1", "b1", "b1", "b1", "b1"],
         ["0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0"],
         ["1", "1", "1", "1", "1", "1", "1", "1"],
         ["4", "2", "3", "5", "6", "3", "2", "4"]
          ]
# Display
screen = pygame.display.set_mode((320, 320))



running = True

def squareCheck(row, collum):
    if board[row][collum] == "0":
        return(True)
    else:
        return(False)

def friendlyPiece (color, row, collum):
    if color == "white":
        if "b" not in board[row][collum]:
            return "friendly"
        if "b" in board[row][collum]:
            return "enemy"
    if color == "black":
        if "b" not in board[row][collum]:
            return "enemy"
        if "b" in board[row][collum]:
            return "friendly"

def legalMove(currentRow, currentCollum, destinationRow, destinationCollum):
    piece = board[currentRow][currentCollum]
    legalMoves = []

    # Rooks
    if piece == "4":
            left = currentCollum
            right = 7 - currentCollum
            for square in range(1, left + 1):
                if squareCheck(currentRow, currentCollum - square):
                    legalMoves.append((currentRow, currentCollum - square))
                elif friendlyPiece("white", currentRow, currentCollum - square) == "enemy":
                    legalMoves.append((currentRow, currentCollum - square))
                    break
            for square in range(1, right + 1):
                if squareCheck(currentRow, currentCollum + square):
                    legalMoves.append((currentRow, currentCollum + square))
                elif friendlyPiece("white", currentRow, currentCollum + square) == "enemy":
                    legalMoves.append((currentRow, currentCollum + square))
                    break
            up = currentRow
            down = 7 - currentRow
            for square in range(1, up + 1):
                if squareCheck(currentRow - square, currentCollum):
                    legalMoves.append((currentRow - square, currentCollum))
                elif friendlyPiece("white", currentRow - square, currentCollum) == "enemy":
                    legalMoves.append((currentRow - square, currentCollum))
                    break
            for square in range(1, down + 1):
                if squareCheck(currentRow + square, currentCollum):
                    legalMoves.append((currentRow + square, currentCollum))
                elif friendlyPiece("white", currentRow + square, currentCollum) == "enemy":
                    legalMoves.append((currentRow + square, currentCollum))
                    break
    if piece == "b4":
            left = currentCollum
            right = 7 - currentCollum
            for square in range(1, left + 1):
                if squareCheck(currentRow, currentCollum - square):
                    legalMoves.append((currentRow, currentCollum - square))
                elif friendlyPiece("black", currentRow, currentCollum - square) == "enemy":
                    legalMoves.append((currentRow, currentCollum - square))
                    break
            for square in range(1, right + 1):
                if squareCheck(currentRow, currentCollum + square):
                    legalMoves.append((currentRow, currentCollum + square))
                elif friendlyPiece("black", currentRow, currentCollum + square) == "enemy":
                    legalMoves.append((currentRow, currentCollum + square))
                    break
            up = currentRow
            down = 7 - currentRow
            for square in range(1, up + 1):
                if squareCheck(currentRow - square, currentCollum):
                    legalMoves.append((currentRow - square, currentCollum))
                elif friendlyPiece("black", currentRow - square, currentCollum) == "enemy":
                    legalMoves.append((currentRow - square, currentCollum))
                    break
            for square in range(1, down + 1):
                if squareCheck(currentRow + square, currentCollum):
                    legalMoves.append((currentRow + square, currentCollum))
                elif friendlyPiece("black", currentRow + square, currentCollum) == "enemy":
                    legalMoves.append((currentRow + square, currentCollum))
                    break

    # Bishops
    if piece == "3":
        directions = [
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]

        for rowCheck, collumCheck in directions:
            for square in range (1, 8):
                checkedRow = currentRow + (rowCheck * square)
                checkedCollum = currentCollum + (collumCheck * square)
                
                if not (0 <= checkedRow < 8 and 0 <= checkedCollum < 8):
                    break

                if squareCheck(checkedRow, checkedCollum):
                    legalMoves.append((checkedRow, checkedCollum))
                elif friendlyPiece("white", checkedRow, checkedCollum) == "enemy":
                    legalMoves.append((checkedRow, checkedCollum))
                    break
                else:
                    break
    if piece == "b3":
            directions = [
                (-1, -1),
                (-1, 1),
                (1, -1),
                (1, 1)
            ]
    
            for rowCheck, collumCheck in directions:
                for square in range (1, 8):
                    checkedRow = currentRow + (rowCheck * square)
                    checkedCollum = currentCollum + (collumCheck * square)
                    
                    if not (0 <= checkedRow < 8 and 0 <= checkedCollum < 8):
                        break
    
                    if squareCheck(checkedRow, checkedCollum):
                        legalMoves.append((checkedRow, checkedCollum))
                    elif friendlyPiece("black", checkedRow, checkedCollum) == "enemy":
                        legalMoves.append((checkedRow, checkedCollum))
                        break
                    else:
                        break

    # Queens
    if piece == "5":
        directions = [
                    (-1, -1),
                    (-1, 1),
                    (1, -1),
                    (1, 1)
                ]
        
        for rowCheck, collumCheck in directions:
            for square in range (1, 8):
                checkedRow = currentRow + (rowCheck * square)
                checkedCollum = currentCollum + (collumCheck * square)
                        
                if not (0 <= checkedRow < 8 and 0 <= checkedCollum < 8):
                    break
        
                if squareCheck(checkedRow, checkedCollum):
                    legalMoves.append((checkedRow, checkedCollum))
                elif friendlyPiece("white", checkedRow, checkedCollum) == "enemy":
                    legalMoves.append((checkedRow, checkedCollum))
                    break
                else:
                    break

        left = currentCollum
        right = 7 - currentCollum
        for square in range(1, left + 1):
            if squareCheck(currentRow, currentCollum - square):
                legalMoves.append((currentRow, currentCollum - square))
            elif friendlyPiece("white", currentRow, currentCollum - square) == "enemy":
                legalMoves.append((currentRow, currentCollum - square))
                break
        for square in range(1, right + 1):
            if squareCheck(currentRow, currentCollum + square):
                legalMoves.append((currentRow, currentCollum + square))
            elif friendlyPiece("white", currentRow, currentCollum + square) == "enemy":
                legalMoves.append((currentRow, currentCollum + square))
                break
        up = currentRow
        down = 7 - currentRow
        for square in range(1, up + 1):
            if squareCheck(currentRow - square, currentCollum):
                legalMoves.append((currentRow - square, currentCollum))
            elif friendlyPiece("white", currentRow - square, currentCollum) == "enemy":
                legalMoves.append((currentRow - square, currentCollum))
                break
        for square in range(1, down + 1):
            if squareCheck(currentRow + square, currentCollum):
                legalMoves.append((currentRow + square, currentCollum))
            elif friendlyPiece("white", currentRow + square, currentCollum) == "enemy":
                legalMoves.append((currentRow + square, currentCollum))
                break
    if piece == "b5":
        left = currentCollum
        right = 7 - currentCollum
        for square in range(1, left + 1):
            if squareCheck(currentRow, currentCollum - square):
                legalMoves.append((currentRow, currentCollum - square))
            elif friendlyPiece("black", currentRow, currentCollum - square) == "enemy":
                legalMoves.append((currentRow, currentCollum - square))
                break
        for square in range(1, right + 1):
            if squareCheck(currentRow, currentCollum + square):
                legalMoves.append((currentRow, currentCollum + square))
            elif friendlyPiece("black", currentRow, currentCollum + square) == "enemy":
                legalMoves.append((currentRow, currentCollum + square))
                break
        up = currentRow
        down = 7 - currentRow
        for square in range(1, up + 1):
            if squareCheck(currentRow - square, currentCollum):
                legalMoves.append((currentRow - square, currentCollum))
            elif friendlyPiece("black", currentRow - square, currentCollum) == "enemy":
                legalMoves.append((currentRow - square, currentCollum))
                break
        for square in range(1, down + 1):
            if squareCheck(currentRow + square, currentCollum):
                legalMoves.append((currentRow + square, currentCollum))
            elif friendlyPiece("black", currentRow + square, currentCollum) == "enemy":
                legalMoves.append((currentRow + square, currentCollum))
                break
        directions = [
                    (-1, -1),
                    (-1, 1),
                    (1, -1),
                    (1, 1)
                    ]
                        
        for rowCheck, collumCheck in directions:
            for square in range (1, 8):
                checkedRow = currentRow + (rowCheck * square)
                checkedCollum = currentCollum + (collumCheck * square)
                                        
                if not (0 <= checkedRow < 8 and 0 <= checkedCollum < 8):
                    break
                        
                if squareCheck(checkedRow, checkedCollum):
                    legalMoves.append((checkedRow, checkedCollum))
                elif friendlyPiece("black", checkedRow, checkedCollum) == "enemy":
                    legalMoves.append((checkedRow, checkedCollum))
                    break
                else:
                    break

    # Knights
    if piece == "2":
        movement = [
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1)
            ]
        for rowCheck, collumCheck in movement:
            checkedRow = currentRow + rowCheck
            checkedCollum = currentCollum + collumCheck
            if  7 >= checkedRow >= 0 and 7 >= checkedCollum >= 0:
                if squareCheck(checkedRow, checkedCollum):
                    legalMoves.append((checkedRow, checkedCollum))
                elif friendlyPiece("white", checkedRow, checkedCollum) == "enemy":
                    legalMoves.append((checkedRow, checkedCollum))
    if piece == "b2":
            movement = [
                (-2, -1),
                (-2, 1),
                (-1, -2),
                (-1, 2),
                (1, -2),
                (1, 2),
                (2, -1),
                (2, 1)
                ]
            for rowCheck, collumCheck in movement:
                checkedRow = currentRow + rowCheck
                checkedCollum = currentCollum + collumCheck
                if  7 >= checkedRow >= 0 and 7 >= checkedCollum >= 0:
                    if squareCheck(checkedRow, checkedCollum):
                        legalMoves.append((checkedRow, checkedCollum))
                    elif friendlyPiece("black", checkedRow, checkedCollum) == "enemy":
                        legalMoves.append((checkedRow, checkedCollum))

    # Kings
    if piece == "6":
        movement = [
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1)
        ]
        for rowCheck, collumCheck in movement:
            checkedRow = currentRow + rowCheck
            checkedCollum = currentCollum +collumCheck
            if  7 >= checkedRow >= 0 and 7 >= checkedCollum >= 0:
                if squareCheck(checkedRow, checkedCollum):
                    legalMoves.append((checkedRow, checkedCollum))
                elif friendlyPiece("white", checkedRow, checkedCollum) == "enemy":
                    legalMoves.append((checkedRow, checkedCollum))
    if piece == "b6":
            movement = [
                (-1, 0),
                (-1, 1),
                (0, 1),
                (1, 1),
                (1, 0),
                (1, -1),
                (0, -1),
                (-1, -1)
            ]
            for rowCheck, collumCheck in movement:
                checkedRow = currentRow + rowCheck
                checkedCollum = currentCollum +collumCheck
                if  7 >= checkedRow >= 0 and 7 >= checkedCollum >= 0:
                    if squareCheck(checkedRow, checkedCollum):
                        legalMoves.append((checkedRow, checkedCollum))
                    elif friendlyPiece("black", checkedRow, checkedCollum) == "enemy":
                        legalMoves.append((checkedRow, checkedCollum))

    # Pawns
    if piece == "1":
        attackDirrection = [
            (-1, 1),
            (-1, -1)
        ]

        if currentRow > 0 and squareCheck(currentRow - 1, currentCollum):
            legalMoves.append((currentRow - 1, currentCollum))
            if currentRow == 6:
                if squareCheck(currentRow - 2, currentCollum):
                    legalMoves.append((currentRow - 2, currentCollum))

        for rowCheck, collumCheck in attackDirrection:
            checkedRow = currentRow + rowCheck
            checkedCollum = currentCollum + collumCheck
            if 7 >= checkedRow >= 0 and 7 >= checkedCollum >= 0:

                if (checkedRow, checkedCollum) == enPassantTarget:
                    if squareCheck(checkedRow, checkedCollum):
                        if board[currentRow][checkedCollum] == "b1":
                            legalMoves.append((checkedRow, checkedCollum))

                elif not squareCheck(checkedRow, checkedCollum):
                    if friendlyPiece("white", checkedRow, checkedCollum) == "enemy":
                        legalMoves.append((checkedRow, checkedCollum))

    # Pawns
    if piece == "b1":
        attackDirrection = [
            (1, 1),
            (1, -1)
        ]

        if currentRow < 7 and squareCheck(currentRow + 1, currentCollum):
            legalMoves.append((currentRow + 1, currentCollum))
            if currentRow == 1:
                if squareCheck(currentRow + 2, currentCollum):
                    legalMoves.append((currentRow + 2, currentCollum))

        for rowCheck, collumCheck in attackDirrection:
            checkedRow = currentRow + rowCheck
            checkedCollum = currentCollum + collumCheck
            if 7 >= checkedRow >= 0 and 7 >= checkedCollum >= 0:

                if (checkedRow, checkedCollum) == enPassantTarget:
                    if squareCheck(checkedRow, checkedCollum):
                        if board[currentRow][checkedCollum] == "1":
                            legalMoves.append((checkedRow, checkedCollum))

                elif not squareCheck(checkedRow, checkedCollum):
                    if friendlyPiece("black", checkedRow, checkedCollum) == "enemy":
                        legalMoves.append((checkedRow, checkedCollum))

    if (destinationRow, destinationCollum) in legalMoves:
        return(True)
    else:
        return(False)
    
def pieceMove(currentRow, currentCollum, destinationRow, destinationCollum):
    global turn
    global enPassantTarget
    if board[currentRow][currentCollum] != "0":
        if turn == "white":
            if not "b" in board[currentRow][currentCollum]:
                if legalMove(currentRow, currentCollum, destinationRow, destinationCollum):
                    piece = board[currentRow][currentCollum]

                    # Checks if the move is an En Passant
                    if piece == "1" and (destinationRow, destinationCollum) == enPassantTarget and squareCheck(destinationRow, destinationCollum):
                        board[currentRow][destinationCollum] = "0"
                    if piece == "1":
                        if abs(destinationRow - currentRow) == 2:
                            enPassantTarget = ((currentRow + destinationRow) // 2, currentCollum)
                        else:
                            enPassantTarget = None
                    else:
                        enPassantTarget = None

                    # Moves The Piece
                    board[currentRow][currentCollum] = "0"
                    board[destinationRow][destinationCollum] = piece
                    turn = "black"
        elif turn == "black":
            if "b" in board[currentRow][currentCollum]:
                if legalMove(currentRow, currentCollum, destinationRow, destinationCollum):
                    piece = board[currentRow][currentCollum]

                    # Checks if the move is an En Passant
                    if piece == "b1" and (destinationRow, destinationCollum) == enPassantTarget and squareCheck(destinationRow, destinationCollum):
                        board[currentRow][destinationCollum] = "0"

                    if piece == "b1":
                        if abs(destinationRow - currentRow) == 2:
                            enPassantTarget = ((currentRow + destinationRow) // 2, currentCollum)
                        else:
                            enPassantTarget = None
                    else:
                        enPassantTarget = None

                    # Moves The Piece
                    board[currentRow][currentCollum] = "0"
                    board[destinationRow][destinationCollum] = piece
                    turn = "white"
            


while running:
    mouseX, mouseY = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Piece Movement
        if event.type == pygame.MOUSEBUTTONDOWN:
            button = event.button
            if button == 1:
                if clickNum == 0:
                    if board[math.floor(mouseY / 40)][math.floor(mouseX / 40)] != "0":
                        startX = mouseX
                        startY = mouseY
                        clickNum = 1
                
                elif clickNum == 1:
                    pieceMove(math.floor(startY / 40), math.floor(startX / 40), math.floor(mouseY / 40), math.floor(mouseX / 40))
                    clickNum = 0
    # Board Drawing
    squareWhite = True
    for index, row in enumerate(board):
        for squareIndex, square  in enumerate(row):
            if index % 2 == 0:    
                if squareWhite == True:
                    pygame.draw.rect(screen, (232, 235, 239), (40 * squareIndex, 40 * index, 40, 40))
                    squareWhite = False
                else:
                    pygame.draw.rect(screen, (105,146,62), (40 * squareIndex, 40 * index, 40, 40))
                    squareWhite = True
            else:
                if squareWhite == True:
                    pygame.draw.rect(screen, (105,146,62), (40 * squareIndex, 40 * index, 40, 40))
                    squareWhite = False
                else:
                    pygame.draw.rect(screen, (232, 235, 239), (40 * squareIndex, 40 * index, 40, 40))
                    squareWhite = True

    # Piece Placement
    for index, row in enumerate(board):
        for squareIndex, square  in enumerate(row):
            if square == "1":
                screen.blit(whitePawn, (40 * squareIndex, 40 * index))
            elif square == "b1":
                screen.blit(blackPawn, (40 * squareIndex, 40 * index))
            elif square == "2":
                screen.blit(whiteKnight, (40 * squareIndex, 40 * index))
            elif square == "b2":
                screen.blit(blackKnight, (40 * squareIndex, 40 * index))
            elif square == "3":
                screen.blit(whiteBishop, (40 * squareIndex, 40 * index))
            elif square == "b3":
                screen.blit(blackBishop, (40 * squareIndex, 40 * index))
            elif square == "4":
                screen.blit(whiteRook, (40 * squareIndex, 40 * index))
            elif square == "b4":
                screen.blit(blackRook, (40 * squareIndex, 40 * index))
            elif square == "5":
                screen.blit(whiteQueen, (40 * squareIndex, 40 * index))
            elif square == "b5":
                screen.blit(blackQueen, (40 * squareIndex, 40 * index))
            elif square == "6":
                screen.blit(whiteKing, (40 * squareIndex, 40 * index))
            elif square == "b6":
                screen.blit(blackKing, (40 * squareIndex, 40 * index))
    
    
    pygame.display.flip()