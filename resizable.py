#All the imports
import pygame
import time
from pygame.locals import *
from pygame import gfxdraw

#Initialization of pygame
pygame.init()

#Color definitions
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

#Defining default display width and height
display_width = 1000
display_height = 600

#Initialization of the default window 
screen = pygame.display.set_mode((display_width,display_height))

#Setting the window title
pygame.display.set_caption('Project :- Resizable Window')

#Loading the images from the system
circle1 = pygame.image.load("circle.png")
click_circle = pygame.image.load("click_circle.png")
hover_circle = pygame.image.load("hover_circle.png")
square1 = pygame.image.load("square.png")
click_square = pygame.image.load("click_square.png")
hover_square = pygame.image.load("hover_square.png")
bg = pygame.image.load("bg.png")
menu_bg = pygame.image.load("menu_bg.png")

#Usage of the System Font 
font = pygame.font.SysFont("verdana", 70)

#Variable for frames per second
FPS = 15

#Variable for accessing a clock() function 
clock = pygame.time.Clock()

#Function defintion of mid point circle algorithm
def mid_point_circle(screen, xc, yc, r, color):

    p=1.25-r
    x=0
    y=r
    
    while(x<=y):

        if(p<0):
            x=x+1
            p=p+2*x+1
        else:
            x=x+1
            y=y-1
            p=p+2*x-2*y+10
            
        gfxdraw.pixel(screen, xc+x, yc+y, color)
        gfxdraw.pixel(screen, xc-y, yc-x, color)
        gfxdraw.pixel(screen, xc+y, yc-x, color)
        gfxdraw.pixel(screen, xc-y, yc+x, color)
        gfxdraw.pixel(screen, xc+y, yc+x, color)
        gfxdraw.pixel(screen, xc-x, yc-y, color)
        gfxdraw.pixel(screen, xc+x, yc-y, color)
        gfxdraw.pixel(screen, xc-x, yc+y, color)

#Function for bresenham's line drawing algorithm
def bresenham_line(screen, x1, y1, x2, y2, color):

    x = int(x1)
    y = int(y1)

    gfxdraw.pixel(screen, x, y, color)

    dx = x2-x1
    dy = y2-y1

    p = 2*dy - dx

    while(dx == 0 and y<=y2):

        gfxdraw.pixel(screen, x, y, color)
        y += 1

    while(x<=x2 and y<=y2 and dx != 0):

        if(p<0):

            gfxdraw.pixel(screen, x+1, y, color)
            p = p + 2*dy
            x+=1

        else:

           gfxdraw.pixel(screen, x, y, color)
           p = p + 2*dy - 2*dx
           x+=1
           y+=1

#Function for drawing a square on the screen using bresenham_line function
def sq_bres(screen, x, y, side, color):

    bresenham_line(screen, x, y, x+int(side), y, color)
    bresenham_line(screen, x, y, x, y+int(side), color)
    bresenham_line(screen, x+int(side), y, x+int(side), y+int(side), color)
    bresenham_line(screen, x, y+int(side), x+int(side), y+int(side), color)

#Function for display a particular message on the screen
    #and for centering it according to the given coordinates
def message_to_screen(msg, color, x_displace = 0, y_displace = 0):

    #Creating the surface object
    textSurf = font.render(msg, True, color)
    #For getting the boundary rectangle of the text
    textRect = textSurf.get_rect()
    #For centering the text
    textRect.center = (int(display_width/2) + x_displace), (int(display_height/2) + y_displace)

    #Displaying the text on the screen
    screen.blit(textSurf, textRect)

#Function for displaying and handling click events on the buttons
def button(x, y, img, action):

    #Variable for the button width and height
    width = 150
    height = 50

    c = 0

    #Variable for getting the mouse cursor position
    cur = pygame.mouse.get_pos()

    if img == 1:
        imgN = circle1
        img_hover = hover_circle
        img_click = click_circle
        
    elif img == 2:
        imgN = square1
        img_hover = hover_square
        img_click = click_square

    #For checking whether the mouse cursor is on the button or not
    if x + width > cur[0] > x and y + height > cur[1] > y:

        #When the mouse cursor is on the button change the default image to hover image
        screen.blit(img_hover, (x, y))

        #Waiting for an event to happen
        event = pygame.event.wait()
        
        #If the mouse button is pressed
        if event.type == MOUSEBUTTONDOWN:
            screen.fill(white)
            screen.blit(menu_bg, (0,0))
            message_to_screen("MENU",
                              white,
                              0,
                              -100)

            #Changing the hover image to click image on mouse button press
            if img_click == click_circle:
                screen.blit(square1, (x,y+90))
            elif img_click == click_square:
                screen.blit(circle1, (x,y-90))

            #Displaying default image for the button
            screen.blit(img_click, (x,y))

            #Updating the display 
            pygame.display.update()

            #Pause for 0.3 secs
            time.sleep(0.3)

        #Waiting for an event to happen
        event = pygame.event.wait()

        #When the mouse button is released after being pressed
        if event.type == MOUSEBUTTONUP:
            c=1
            screen.fill(white)
            screen.blit(menu_bg, (0,0))
            message_to_screen("MENU",
                                  white,
                                  0,
                                  -100)

            if img_click == click_circle:
                screen.blit(square1, (x,y+90))
            elif img_click == click_square:
                screen.blit(circle1, (x,y-90))

            #Changing the image back to default
            screen.blit(imgN, (x,y))
            
            pygame.display.update()

            time.sleep(0.3)
            
        if c == 1:
            #If circle button is pressed
            if action == "circle":
                    circle()

            #If square button is pressed
            elif action == "square":
                    square()
                    
    else:
        screen.blit(imgN, (x, y))

#Funtion for resizing the square  
def square():

    square = True

    #Changing the display form default mode to resizable mode
    screen = pygame.display.set_mode((display_width,display_height),RESIZABLE)

    #Changing the default background color to white
    screen.fill(white)

    #Variable for calculating default square side 
    a = int(display_width*display_height*4)/(5*(display_width+display_height))

    #Variable for calculating default square position
    x = int((display_width/2) - (a/2))
    y = int((display_height/2) - (a/2))

    #Drawing the square on the screen
    sq_bres(screen , x, y, a, green)

    #Updating the display
    pygame.display.update()

    #Function loop
    while square:

        event = pygame.event.wait()

        #If the close button is pressed on the title bar close everything
        if event.type == pygame.QUIT:
            square = False
            pygame.quit()
            quit()

        #If the window is resized 
        elif event.type == VIDEORESIZE:

            #On resizing change the window to new resized window
            screen=pygame.display.set_mode(event.dict['size'],RESIZABLE)

            screen.fill(white)

            #Calculating the new square side on the basis of current window width and height
            a = (event.dict['size'][0]*event.dict['size'][1]*4)/(5*(event.dict['size'][0]+event.dict['size'][1]))

            #Calculating the new coordinates of the square
            x=event.dict['size'][0]/2 - (a/2)
            y=event.dict['size'][1]/2 - (a/2)

            #Displaying the square at the new position
            sq_bres(screen , x, y, a, green)
            
            pygame.display.update()

        #Setting frames per sec 
        clock.tick(FPS)

#Funtion for resizing the circle
def circle():

    circle = True

    screen = pygame.display.set_mode((display_width,display_height),RESIZABLE)

    screen.fill(white)

    #Calculating the default radius 
    radius = int((display_width*display_height)/3000)

    #Drawing the circle on the screen
    mid_point_circle(screen, int(display_width/2), int(display_height/2), radius, red)
    
    pygame.display.update()

    #Funtion Loop
    while circle:

        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            circle = False
            pygame.quit()
            quit()

        elif event.type == VIDEORESIZE:

            screen = pygame.display.set_mode(event.dict['size'],RESIZABLE)
            screen.fill(white)

            #Calculating the new radius for the circle
            radius = int((event.dict['size'][0]*event.dict['size'][1])/3000)

            #Calculating the new coordinates for the circle
            x = int(event.dict['size'][0]/2)
            y = int(event.dict['size'][1]/2)

            #Drawing the new circle at the new position
            mid_point_circle(screen, x, y, radius, red)

            pygame.display.update()

        clock.tick(FPS)

#Funtion for the menu screen or splash screen
def menu():

    menu = True

    #Menu Loop
    while menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            screen.fill(white)

            #Setting background for menu screen 
            screen.blit(menu_bg, (0,0))

            #Displaying message on the screen
            message_to_screen("MENU",
                              white,
                              0,
                              -100)

            #Displaying the buttons on the screen
            button(int(display_width/2) - 75, int(display_height/2) - 10, 1, "circle")
            button(int(display_width/2) - 75, int(display_height/2) + 80, 2, "square")

            pygame.display.update()

#Function for the splash screen 
def main():

    main = True

    #Main Loop
    while main:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)

        #Setting background image for the screen
        screen.blit(bg, (0,0))

        pygame.display.update()

        #Pause for 2 secs
        time.sleep(2)

        #Calling the menu function
        menu()

    clock.tick(FPS)

#Splash screen function call
main()
