import pygame

pygame.init()
bg = pygame.image.load("bg.jpg")
red = pygame.transform.scale(pygame.image.load("red.png"), (105, 105))
blue = pygame.transform.scale(pygame.image.load("blue.png"), (105, 105))
window = pygame.display.set_mode((550, 550))
pygame.display.set_caption("Tic Tac Toe v2.1")
pygame.display.set_icon(pygame.image.load("main.png"))
winner_sound = pygame.mixer.Sound("winner.wav")
boing = pygame.mixer.Sound("boing.wav")
music = pygame.mixer.music.load("music.mp3")
font = pygame.font.SysFont("comic", 32)
font2 = pygame.font.SysFont("comic", 50)
version = font.render("v2.1", 1, (255, 255, 255))
spacer = font2.render("Press space to restart!", 1, (0, 0, 0))
window.blit(bg,(0, 0))
pygame.mixer.music.play(-1)

def board():
    global one,two,three,four,five,six,seven,eight,nine
    one = pygame.draw.rect(window, (255,255,255), (25,25,150,150))
    two = pygame.draw.rect(window, (255,255,255), (200,25,150,150))
    three = pygame.draw.rect(window, (255,255,255), (375,25,150,150))
    four = pygame.draw.rect(window, (255,255,255), (25,200,150,150))
    five = pygame.draw.rect(window, (255,255,255), (200,200,150,150))
    six = pygame.draw.rect(window, (255,255,255), (375,200,150,150))
    seven = pygame.draw.rect(window, (255,255,255), (25,375,150,150))
    eight = pygame.draw.rect(window, (255,255,255), (200,375,150,150))
    nine = pygame.draw.rect(window, (255,255,255), (375,375,150,150))

user = 'blue'
winner = False
holder = 0

def counter():
    global n1,n2,n3,n4,n5,n6,n7,n8,n9
    n1 = True
    n2 = True
    n3 = True
    n4 = True
    n5 = True
    n6 = True
    n7 = True
    n8 = True
    n9 = True

def checker():
    global x1,x2,x3,x4,x5,x6,x7,x8,x9,y1,y2,y3,y4,y5,y6,y7,y8,y9
    x1 = False
    x2 = False
    x3 = False
    x4 = False
    x5 = False
    x6 = False
    x7 = False
    x8 = False
    x9 = False
    y1 = False
    y2 = False
    y3 = False
    y4 = False
    y5 = False
    y6 = False
    y7 = False
    y8 = False
    y9 = False

checker()
board()
counter()
running = True
while running:
    window.blit(version, (500, 528))
    if holder == 9:
        window.blit(bg, (0, 0))
        label = font2.render("There is a tie!", 1, (0, 0, 0))
        window.blit(label, (140, 200))
        window.blit(spacer, (80, 250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                window.blit(bg, (0, 0))
                board()
                counter()
                checker()
                holder = 0
                running = True
        if event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                if one.collidepoint(position) and n1:
                    if user == 'blue':
                        window.blit(blue, (50, 50))
                        boing.play()
                        holder += 1
                        user = 'red'
                        y1 = True
                    else:
                        window.blit(red, (50, 50))
                        boing.play()
                        holder += 1
                        user = 'blue'
                        x1 = 1
                    n1 = False
                if two.collidepoint(position) and n2:
                    if user == 'blue':
                        window.blit(blue, (225, 50))
                        boing.play()
                        holder += 1
                        user = 'red'
                        y2 = True
                    else:
                        window.blit(red, (225, 50))
                        boing.play()
                        holder += 1
                        user = 'blue'
                        x2 = 1
                    n2 = False
                if three.collidepoint(position) and n3:
                    if user == 'blue':
                        window.blit(blue, (400, 50))
                        boing.play()
                        holder += 1
                        user = 'red'
                        y3 = True
                    else:
                        window.blit(red, (400, 50))
                        boing.play()
                        holder += 1
                        user = 'blue'
                        x3 = 1
                    n3 = False
                if four.collidepoint(position) and n4:
                    if user == 'blue':
                        window.blit(blue, (50, 225))
                        boing.play()
                        holder += 1
                        user = 'red'
                        y4 = True
                    else:
                        window.blit(red, (50, 225))
                        boing.play()
                        holder += 1
                        user = 'blue'
                        x4 = True
                    n4 = False
                if five.collidepoint(position) and n5:
                    if user == 'blue':
                        window.blit(blue, (225, 225))
                        boing.play()
                        holder += 1
                        user = 'red'
                        y5 = True
                    else:
                        window.blit(red, (225, 225))
                        boing.play()
                        holder += 1
                        user = 'blue'
                        x5 = True
                    n5 = False
                if six.collidepoint(position) and n6:
                    if user == 'blue':
                        window.blit(blue, (400, 225))
                        boing.play()
                        holder += 1
                        user = 'red'
                        y6 = True
                    else:
                        window.blit(red, (400, 225))
                        boing.play()
                        holder += 1
                        user = 'blue'
                        x6 = True
                    n6 = False
                if seven.collidepoint(position) and n7:
                    if user == 'blue':
                        window.blit(blue, (50, 400))
                        boing.play()
                        holder += 1
                        user = 'red'
                        y7 = True
                    else:
                        window.blit(red, (50, 400))
                        boing.play()
                        holder += 1
                        user = 'blue'
                        x7 = True
                    n7 = False
                if eight.collidepoint(position) and n8:
                    if user == 'blue':
                        window.blit(blue, (225, 400))
                        boing.play()
                        holder += 1
                        user = 'red'
                        y8 = True
                    else:
                        window.blit(red, (225, 400))
                        boing.play()
                        holder += 1
                        user = 'blue'
                        x8 = True
                    n8 = False
                if nine.collidepoint(position) and n9:
                    if user == 'blue':
                        window.blit(blue, (400, 400))
                        boing.play()
                        holder += 1
                        user = 'red'
                        y9 = True
                    else:
                        window.blit(red, (400, 400))
                        boing.play()
                        holder += 1
                        user = 'blue'
                        x9 = True
                    n9 = False
                if x1 == x2 == x3 == True or x4 == x5 == x6 == True or x7 == x8 == x9 == True or x1 == x4 == x7 == True or x2 == x5 == x8 == True or x3 == x6 == x9 == True or x1 == x5 == x9 == True or x3 == x5 == x7 == True:
                    winner_sound.play()
                    window.blit(bg, (0, 0))
                    x_winner = font2.render("Congrats Player X, You won!", 1, (0, 0, 0))
                    window.blit(x_winner, (35, 200))
                    window.blit(spacer, (80, 250))
                elif y1 == y2 == y3 == True or y4 == y5 == y6 == True or y7 == y8 == y9 == True or y1 == y4 == y7 == True or y2 == y5 == y8 == True or y3 == y6 == y9 == True or y1 == y5 == y9 == True or y3 == y5 == y7 == True:
                    winner_sound.play()
                    window.blit(bg, (0, 0))
                    y_winner = font2.render("Congrats Player O, You won!", 1, (0, 0, 0))
                    window.blit(y_winner, (35, 200))
                    window.blit(spacer, (80, 250))

    pygame.display.update()
pygame.quit()