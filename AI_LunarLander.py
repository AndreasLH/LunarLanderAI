# Lunar Lander: AI-controlled play

# Instructions:
#   Land the rocket on the platform within a distance of plus/minus 20, 
#   with a horizontal and vertical speed less than 20
#
# Controlling the rocket:
#    arrows  : Turn booster rockets on and off
#    r       : Restart game
#    q / ESC : Quit

from LunarLander import *
import time

env = LunarLander()
env.reset()
exit_program = False
frames_passed = 0
fps = 30
counter = 0
fails = 0
temp_reward = 0
total_fuel= 0
temp_time =0
total_time = 0
average_fuel = 0
average_time = 0

while not exit_program:
    env.render()
    (x, y, xspeed, yspeed), reward, done = env.step((boost, left, right)) 

    # Process game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                exit_program = True
            if event.key == pygame.K_UP:
                boost = True
            if event.key == pygame.K_DOWN:
                boost = False
            if event.key == pygame.K_RIGHT:
                left = False if right else True
                right = False
            if event.key == pygame.K_LEFT:
                right = False if left else True
                left = False
            if event.key == pygame.K_r:
                boost = False        
                left = False
                right = False
                env.reset()

    # INSERT YOUR CODE HERE
    #
    # Implement a Lunar Lander AI 
    # Control the rocket by writing a list of if-statements that control the 
    # three rockets on the lander 
    #
    # The information you have available are x, y, xspeed, and yspeed
    # 
    # You control the rockets by setting the variables boost, left, and right
    # to either True or false
    #
    # Example, to get you started. If the rocket is close to the ground, turn
    # on the main booster
    
    #yspeed er positiv nedad
    #xspeed er positiv til højre
    #x er 0 midt på landingsplads, positiv til højre og negativ til venstre
    #y er 0 nede på landingsplatformen
    værdi = 1
    #starter booster når højden kommer under 185
    if y < 185:
        boost = True
    #forhindrer gør at den lander med specificeret hastighed
    #hurtig værdi = 10, præcis =1
    if y < 50 and yspeed < værdi:
        boost = False       
    #forhindrer at den flyver opad i starten
    if y > 40 and yspeed < 0:
        boost = False
    #hvis den er til venstre
    if x < 0:
        left = True
        right = False
    #til højre
    if x > 0:
        right = True
        left = False
    #tillader at den max flyver til siden med hastighed 25 eller flyver den forbi   
    if xspeed > 25 :
        left = False
    if xspeed < -25 :
        right = False
    # gør den mere præcis ved landingen
    #hurtig = 10, præcis 1
    if y < 65 and xspeed > værdi :
        left = False
    if y < 65 and xspeed < -værdi :
        right = False
    #restarter automatisk efter 0.8s   
    
    frames_passed += 1
    
    
    if done == True and reward > 1:
        counter += 1
        temp_time = temp_time + frames_passed/fps
        temp_reward = reward + temp_reward
        reward = round(reward, 4)
        tid = round(frames_passed/fps,3)
        print("Fuel: " + str(reward))
        print("Time: " + str(tid))
        frames_passed = 0
        start_time = 0
        env.reset()
        
        if counter == 50:
            exit_program = True
            
    if done == True and reward ==0:
        counter += 1
        frames_passed = 0
        fails += 1
        env.reset()
    if counter == 50:
        exit_program = True     
    if done == True and exit_program == True:
        countavg = counter - fails
        total_fuel = temp_reward + reward
        total_time = temp_time + frames_passed/fps
        average_fuel = total_fuel/countavg
        average_time = total_time / countavg
        
        print("fail " + str(fails))

        print("average fuel: " + str(round(average_fuel,4)))
        print("average time: " + str(round(average_time,4)))
     
    # Modify and add more if-statements to make the rocket land safely
    # END OF YOUR CODE

env.close()