import pygame 

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT) )
pygame.display.set_caption("two player chess game")
font = pygame.font.Font("freesansbold.ttf", 50)
timer = pygame.time.Clock()
fps = 60

white_pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook" , "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
black_pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook" , "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []
turn_step = 0 # 0 for white turn 1 for white turn when a piece is selected ,  2 for black turn , 3 for black turn when a piece is selected
valid_moves = []
selection = 100

black_queen = pygame.image.load("assets/images/black queen.png")
black_queen =  pygame.transform.scale(black_queen, (80 , 80 ) )
black_queen_small = pygame.transform.scale(black_queen, (45, 45 ) )

black_king = pygame.image.load("assets/images/black king.png")
black_king =  pygame.transform.scale(black_king, (80 , 80 ))
black_king_small = pygame.transform.scale(black_king, (45, 45 ))

black_rook = pygame.image.load("assets/images/black rook.png")
black_rook =  pygame.transform.scale(black_rook, (80 , 80 ))    
black_rook_small = pygame.transform.scale(black_rook, (45, 45 ))

black_bishop = pygame.image.load("assets/images/black bishop.png")
black_bishop =  pygame.transform.scale(black_bishop, (80 , 80 ))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45 ))

black_knight = pygame.image.load("assets/images/black knight.png")
black_knight =  pygame.transform.scale(black_knight, (80 , 80 ))
black_knight_small = pygame.transform.scale(black_knight, (45, 45 ))

black_pawn = pygame.image.load("assets/images/black pawn.png")
black_pawn =  pygame.transform.scale(black_pawn, (65 , 65 ))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45 ))


white_queen = pygame.image.load("assets/images/white queen.png")
white_queen =  pygame.transform.scale(white_queen, (80 , 80 ))
white_queen_small = pygame.transform.scale(white_queen, (45, 45 ))

white_king = pygame.image.load("assets/images/white king.png")
white_king =  pygame.transform.scale(white_king, (80 , 80 ))
white_king_small = pygame.transform.scale(white_king, (45, 45 ))

white_rook = pygame.image.load("assets/images/white rook.png")
white_rook =  pygame.transform.scale(white_rook, (80 , 80 ))
white_rook_small = pygame.transform.scale(white_rook, (45, 45 ))

white_bishop = pygame.image.load("assets/images/white bishop.png")
white_bishop =  pygame.transform.scale(white_bishop, (80 , 80 ))    
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45 ))

white_knight = pygame.image.load("assets/images/white Knight.png")
white_knight =  pygame.transform.scale(white_knight, (80 , 80 ))
white_knight_small = pygame.transform.scale(white_knight, (45, 45 ))

white_pawn = pygame.image.load("assets/images/white pawn.png")
white_pawn =  pygame.transform.scale(white_pawn, (65 , 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45 ))

white_images = [white_pawn , white_queen  , white_king , white_knight , white_rook , white_bishop]
white_images_small = [white_pawn_small , white_queen_small  , white_king_small , white_knight_small , white_rook_small , white_bishop_small]
black_images = [black_pawn , black_queen  , black_king , black_knight , black_rook , black_bishop]
black_images_small = [black_pawn_small , black_queen_small  , black_king_small , black_knight_small , black_rook_small , black_bishop_small]
piece_list = ["pawn" , "queen", "king", "knight", "rook", "bishop"]

def draw_board():
    square_size = 100
    for row in range(8):
        for column in range(8):
            if ( row + column) % 2 == 1:
                pass
            else :
                pygame.draw.rect(screen, "lightgray", (column * square_size, row * square_size, square_size, square_size))
    pygame.draw.rect(screen, "gray", (0, 800, WIDTH, 100))  
    pygame.draw.rect(screen, "gold", (0, 800, WIDTH, 100) , 5)       
    pygame.draw.rect(screen, "gold", (800, 0, 200 ,  HEIGHT) , 5)            
    status_text =["White : select a piece to move " , "White : select a destination to move the piece" , "Black : select a piece to move " , "Black : select a destination to move the piece"]
    screen.blit(font.render(status_text[turn_step], True, "black"), (10, 810))
    for i in range(9):
        pygame.draw.line(screen, "black", (i * square_size, 0), (i * square_size, HEIGHT - 100), 2)
        pygame.draw.line(screen, "black", (0, i * square_size), (WIDTH - 200, i * square_size), 2)

def draw_pieces():
    for i in range(len(white_pieces)):
        if white_pieces[i] == "pawn":
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 15 , white_locations[i][1] * 100 + 15))
        else :
            screen.blit(white_images[piece_list.index(white_pieces[i])], (white_locations[i][0] * 100 + 15 , white_locations[i][1] * 100 + 15))
        if turn_step < 2 : 
            if selection == i : 
         
              pygame.draw.rect(screen, (255, 0, 0), (white_locations[i][0] * 100, white_locations[i][1] * 100, 100, 100) , 1)
        
   
    for i  in range(len(black_pieces)):
        if black_pieces[i] == "pawn":
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 15 , black_locations[i][1] * 100 + 15))
        else :
            screen.blit(black_images[piece_list.index(black_pieces[i])], (black_locations[i][0] * 100 + 15 , black_locations[i][1] * 100 + 15))
        if turn_step > 1 :
            if selection == i : 
                pygame.draw.rect(screen, (255, 0, 0), (black_locations[i][0] * 100, black_locations[i][1] * 100, 100, 100) , 1)

def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        if piece == 'queen':
            moves_list = check_queen(location, turn)
        if piece == 'knight':
            moves_list = check_knight(location, turn) 
        
        if piece == 'king':
            moves_list = check_king(location, turn)
        
        if piece == 'rook':
            moves_list = check_rook(location, turn)
        
        if piece == 'bishop':
            moves_list = check_bishop(location, turn) 
        all_moves_list.append(moves_list)
        
       
    return all_moves_list

def check_pawn(position , color ):
    moves_list = []
    (x , y )= position
    if color == "white" :
        if (x, y + 1) not in white_locations and (x, y + 1) not in black_locations:
            moves_list.append((x, y + 1))
        if (x+1 , y + 1) in black_locations:
            moves_list.append((x+1, y + 1))       
        if (x - 1, y + 1) in black_locations:
            moves_list.append((x - 1, y + 1))
        if y== 1 and (x, y + 2) not in white_locations and (x, y + 2) not in black_locations:
            moves_list.append((x, y + 2))
    else :
        if (x, y - 1) not in white_locations and (x, y - 1) not in black_locations:
            moves_list.append((x, y - 1))
        if (x + 1, y - 1) in white_locations:
            moves_list.append((x + 1, y - 1))       
        if (x - 1, y - 1) in white_locations:
            moves_list.append((x - 1, y - 1))
        if y == 6 and (x, y - 2) not in white_locations and (x, y - 2) not in black_locations:
            moves_list.append((x, y - 2))
    
    return moves_list    
def check_queen(position, color):
    if color == "black":
        friends_locations = black_locations
        enemies_locations = white_locations
    else:
        friends_locations = white_locations
        enemies_locations = black_locations

    moves_list = []
    x, y = position
   
    directions = [( 1 , 0 ) , ( -1  , 0 ) , (0 ,  1 ) , ( 0,  -1) , (1 , 1 ) , ( -1 , 1 ) , ( -1 , -1 ) , ( 1 , -1 )]
    
    for dx ,  dy in directions :
        for i in range(1 , 8 ) :
            new_x = x  + dx * i 
            new_y = y + dy * i 
 
            if not (0 <= new_x < 8 and 0 <= new_y < 8):
                break

            if ( new_x , new_y ) in enemies_locations :
                moves_list.append((new_x , new_y))
                break 
            if ( new_x , new_y ) in friends_locations :
                break 
            moves_list.append((new_x , new_y ))
    return moves_list        
 
def check_king(position, color):
        moves_list = []
        (x, y) = position
        if color == "white":    
            friends_locations = white_locations
       
        else :
            friends_locations = black_locations
            
        if (x + 1, y) not in friends_locations:
            moves_list.append((x + 1, y))
        if (x - 1, y) not in friends_locations:
            moves_list.append((x - 1, y))
        if (x, y + 1) not in friends_locations:
            moves_list.append((x, y + 1))
        if (x, y - 1) not in friends_locations:
            moves_list.append((x, y - 1))
        if (x + 1, y + 1) not in friends_locations:
            moves_list.append((x + 1, y + 1))
        if (x - 1, y - 1) not in friends_locations:
            moves_list.append((x - 1, y - 1))
        if (x + 1, y - 1) not in friends_locations:
            moves_list.append((x + 1, y - 1))
        if (x - 1, y + 1) not in friends_locations:
            moves_list.append((x - 1, y + 1))
        return moves_list

def check_rook(position, color):
    if color == "black":
        friends_locations = black_locations
        enemies_locations = white_locations
    else:
        friends_locations = white_locations
        enemies_locations = black_locations

    moves_list = []
    x, y = position
   
    directions = [( 1 , 0 ) , ( -1  , 0 ) , (0 ,  1 ) , ( 0,  -1) ]
    
    for dx ,  dy in directions :
        for i in range(1 , 8 ) :
            new_x = x  + dx * i 
            new_y = y + dy * i 
 
            if not (0 <= new_x < 8 and 0 <= new_y < 8):
                break

            if ( new_x , new_y ) in enemies_locations :
                moves_list.append((new_x , new_y))
                break 
            if ( new_x , new_y ) in friends_locations :
                break 
            moves_list.append((new_x , new_y ))
    return moves_list   
 
def check_bishop(position, color):
    if color == "black":
        friends_locations = black_locations
        enemies_locations = white_locations
    else:
        friends_locations = white_locations
        enemies_locations = black_locations

    moves_list = []
    x, y = position
   
    directions = [(1 , 1 ) , ( -1 , 1 ) , ( -1 , -1 ) , ( 1 , -1 )]
    
    for dx ,  dy in directions :
        for i in range(1 , 8 ) :
            new_x = x  + dx * i 
            new_y = y + dy * i 
 
            if not (0 <= new_x < 8 and 0 <= new_y < 8):
                break

            if ( new_x , new_y ) in enemies_locations :
                moves_list.append((new_x , new_y))
                break 
            if ( new_x , new_y ) in friends_locations :
                break 
            moves_list.append((new_x , new_y ))
    return moves_list  
def check_knight(position, color):  
    (x , y ) = position
    moves_list = [] 
    if color == "white":
        friends_locations = black_locations
    else :
        friends_locations = white_locations
        
    if (x + 2, y + 1) not in friends_locations :
        moves_list.append((x + 2, y + 1))   
    if (x + 2, y - 1) not in friends_locations :
        moves_list.append((x + 2, y - 1))
    if (x - 2, y + 1) not in friends_locations :
        moves_list.append((x - 2, y + 1))
    if (x - 2, y - 1) not in friends_locations :
        moves_list.append((x - 2, y - 1))
    if (x + 1, y + 2) not in friends_locations :
        moves_list.append((x + 1, y + 2))
    if (x + 1, y - 2) not in friends_locations :
        moves_list.append((x + 1, y - 2))
    if (x - 1, y + 2) not in friends_locations :
        moves_list.append((x - 1, y + 2))
    if (x - 1, y - 2) not in friends_locations :
         moves_list.append((x - 1, y - 2))
    return moves_list
    
def draw_valid_moves(moves):
    
   for move in range(len(moves)):
        pygame.draw.circle(screen, "red", (moves[move][0] * 100 + 50, moves[move][1] * 100 + 50), 10)
    
def draw_check( ):
    if turn_step  > 1  :
        for option in white_options:
            for move in option:
                if move == black_locations[4]:
                   if counter < 30 :
                       pygame.draw.rect(screen ,"red", (black_locations[4][0] * 100, black_locations[4][1] *100 , 100, 100) , 5 )
    else :
        for option in black_options:
           for move in option:
              if move == white_locations[4]:
                  if counter < 30 :
                       pygame.draw.rect(screen ,"red", (white_locations[4][0] * 100, white_locations[4][1] *100 , 100, 100) , 5 )       

        
def draw_captured():
    
    if captured_pieces_black :
        for i, piece in enumerate(captured_pieces_black):
            x = 8 * 100 + 15
            y = i * 50 + 15 
            screen.blit(white_images_small[piece_list.index(captured_pieces_black[i])], (x, y))
           
    if captured_pieces_white  :
      
        for i, piece in enumerate(captured_pieces_white):
            x = 9 * 100 + 15
            y = i * 50 + 15 
            screen.blit(black_images_small[piece_list.index(captured_pieces_white[i])], (x, y))
           


def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 100])
    screen.blit(font.render("game over", True, "white "), (250, 210))
    small_font = pygame.font.SysFont(None, 40)  

   
    text = small_font.render("Press enter to restart", True, "white")

   
    screen.blit(text, (250, 270))
   





black_options = check_options(black_pieces, black_locations, "black")
white_options = check_options(white_pieces, white_locations, "white")
winner = ""
counter = 0 
run  = True
game_over = False




while run:  
    
    screen.fill("darkgray")
    draw_board() 
    draw_pieces()
    draw_captured()
    draw_valid_moves(valid_moves)
    draw_check( )
    
    if counter < 60  :
        counter = counter + 1 
    else :
        counter = 0 
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            mouse_x, mouse_y = event.pos
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    
                    valid_moves = white_options[selection]
                    
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        if black_pieces[black_piece]== "king" :
                            winner ="white"
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    turn_step = 2
                    black_options = check_options(black_pieces, black_locations, "black")
                    white_options = check_options(white_pieces, white_locations, "white")
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    valid_moves = black_options[selection] 
                    
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        if black_pieces[white_piece]== "king" :
                            winner ="black"
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    turn_step = 0
                    black_options = check_options(black_pieces, black_locations, "black")
                    white_options = check_options(white_pieces, white_locations, "white")
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RETURN:
                winner = ""
                game_over = False 
                
                white_pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook" , "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
                black_pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook" , "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                            (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                            (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0 
                valid_moves = []
                selection = 100
                black_options = check_options(black_pieces, black_locations, "black")
                white_options = check_options(white_pieces, white_locations, "white")
    
    if winner !=  "" :
        draw_game_over()
        game_over = True 
    pygame.display.update()

pygame.quit()