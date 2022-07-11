DOCUMENTATION
DESCRIPTION:
A space war game which is challenging and entertaining which consist of a hero spaceship and enemies with astroids as the play time increases the speed of the game also increases ,which makes the game tough
FORMAT:
The game is made using a module called pygame in python the dimensions of its terminal is 800,600 pixel
DETAILS:
•	Firstly a game window is made using pygame.display.set_mode(800,600) where 800,600 are the dimensions of the game terminal in pixels
•	Downloaded required pictures for google in png form and sound effects in wav and mp3 form
•	To load image pygame.image.load is used and to display screen.blit() is used
•	 Adjusted the so downloaded hero spaceship pic in the game terminal and in the while run loop added if conditions with event keydown for the movement of the spaceship in left right forward and backward directions while a speed of 2pixels for one loop run and stops if the same key if released for which if conditions are given with keyup event is space is clicked (K_SPACE) it shoots a bullet
•	Imported random module and used randint the create 3 asteroids(pictures collected from google) at different x axis positions and took a variable called speed+=1/10000 where speed increases by 1/10000 per loop run till speed>=2.7 once it is 2.7 it becomes constant (it is controlled by an if condition)and the y axis of the asteroid increases by speed(pixels) for every loop run ,so as the time goes on the game appears going speed which increases the toughness levels once any asteroid crosses the frame size of 675 or if it collides with the spaceship bullet or spaceship it resets and starts from next random position
•	 3 enemies are created , using randint they are created at different x axis positions, even in the case of enemies a variable spe+=1/50000 is taken which increases by 1/50000 per loop run till spe>=2 once it is 2 it becomes constant(controlled by if)and the y axis of the enemy increases by spe (pixels) for every loop run,so as the time goes on the enemy movements speed in y axis increases which makes the game tough and the enemies move left and right(giving few if conditions) in x-axis direction also with 0.9 pixels per loop  once any enemy crosses the frame size of 675 or if it collides with the spaceship bullet or spaceship it resets and starts form next random position . they shoot bullets form a particular position once the their bullet reaches 620 pixels or collides with the spaceship then they stoot other 
•	To verify collision math distance formulae sqrt(math.pow(x2-x1,2)+math.pow(y2-y1),2) is used and using if it collision limit is given the check whether collision occurred or no
•	Using freesansbold.ttf and font.render displayed score and health where are the score and health is ensured with a score and health variable if the enemy bullet collide the spaceship then health-=10 if asteroid or enemy collides the spaceship health-=20. If spaceship bullet collides the enemy then score+=10
•	Using if conditions few cases are arranged if p is pressed game gets paused(K_p) and if s is clicked the game starts(K_s)
•	Used QUIT event to check whether the game is quit or not
•	If health<=0 then it displayes Game over and Your score : score(used font.render and used freesansbold.ttf font)
•	If r is pressed the the game reset and starts again(K_r)
•	Before starting if h is clicked it displayes the highscore(K_h)
•	 Used a file to store the highscore  initialized the current score to high and checked against the previous highscore reading from the file if high>highscore then high value is written into the file this way it displays the high score.
