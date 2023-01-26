#basic games and built on top of this
import turtle 
import winsound

#Create a window
wn = turtle.Screen() #Turtle allows to create a new screen instance
wn.title("Basic Pong") #Title of the screen, in turn the game
wn.bgcolor("black") #changes the bacground color of the window to black
wn.setup(width =800, height=600) #Sets the window dimensions to 800x600
wn.tracer(0) #Stops the window from updating and speeds up the game as well

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle() #paddle A is created. turtle is the module name and Turtle is a Class
paddle_a.speed(0) #Speed of the animation, maximum speed is set in this case
paddle_a.shape("square") #Shape of the paddle object
paddle_a.color("white") #Color of the paddle
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #Default shape size is 20x20 pixels, this streches the paddle width 5 times and keeps lenght same
paddle_a.penup() #draw a line as they move, not needed here
paddle_a.goto(-350, 0) #initial position of the paddle on the screen

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0) 

#Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)

#Ball Movement in X and Y direction
ball.dx = 0.75 #d means delta or change
ball.dy = -0.75 #every time ball moves, it moves by 2 pixels

#Pen
pen = turtle.Turtle()
pen.speed(0) #Animation speed of the object
pen.color("white")
pen.penup() #this is to avoid a line being drawn whenever the pen moves
pen.hideturtle() #Hides the pen 
pen.goto(0, 260) #Moves the pen to the coordinates
pen.write("Player A: 0  Player B: 0", align= "Center", font=("Courier", 20, "normal")) #Inputs the player scores, aligns them to centre and uses the font family and the size given

#Paddle movement functions
def paddle_a_up():
    y = paddle_a.ycor() #Gets the current y-axis coordinate of the paddle A
    y += 25 #Adds 20 pixels distance to paddle A if we press up key
    paddle_a.sety(y) #sets the new position of paddle a to new y coordinate depending on the press up key

def paddle_a_down():
    y = paddle_a.ycor()
    y -=25
    paddle_a.sety(y)  

def paddle_b_up():
    y = paddle_b.ycor()
    y +=25
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -=25
    paddle_b.sety(y)    


#Keyboard binding
  #For Paddle A up
wn.listen() #Makes the window listen to any keyboard inputs
wn.onkeypress(paddle_a_up, "w") #calls the function paddle_a-up and sets the position of paddle a up by 20 pixels when w key is pressed
wn.onkeypress(paddle_a_down, "s") 
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    wn.update() #Updates the screen every time the loop runs

    #Move the ball
    ball.setx(ball.xcor() + ball.dx) #Ball will start at (0,0) start, then be moving in increment of 2 pixels in x axis every cycle
    ball.sety(ball.ycor() + ball.dy)

    #Border checking 
    if(ball.ycor() > 290): #Since screen height is 300, if balls present y coordinate is greater than 290 then:
        ball.sety(290)
        ball.dy *= -1 #Revereses the direction of the ball

    if(ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -1     

    if(ball.xcor() > 390):
        ball.goto(0,0) #ball will start again in the centre if it touches the x direction borders
        ball.dx *= -1
        score_a += 1 #Player a will get a point if ball goes off the right side of the screen
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align= "Center", font=("Courier", 20, "normal"))
        

    if(ball.xcor() < -390):
        ball.goto(0,0)
        ball.dx *= -1  
        score_b += 1 #Player b will get a point if ball goes off the left side of the screen
        pen.clear() #Clears the values before updating
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align= "Center", font=("Courier", 20, "normal")) 
         

    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1    
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) #Adds sound from .wav file and syncs the sound when colliding with the borders
        #If the balls present coordinate is near the paddle 

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1  
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        #Sucessfully created Pong game
        #Sucessfully added to Github repo

        




      

   






