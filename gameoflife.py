import pygame
import time
import random
import copy

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('GAME OF LIFE')

state = 'waiting'
list_key = []
list_value = []
list_value_duplicate = []
run = True
while run :
    screen.fill((0,150,150))
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_p :
                state = 'start populate'
            if event.key == pygame.K_SPACE :
                for i in range (50) :
                    for j in range (50) :
                        list_key.append([i,j])
                        if i == 0 or i ==  49 : 
                            list_value.append(0)
                        elif j == 0 or j == 49 :
                            list_value.append(0)
                        else :
                            if random.random() > 0.5 :
                                value = 1
                                list_value.append(value) 
                            else :
                                value = 0
                                list_value.append(value)  
    if state == 'start populate' :
        list_value_duplicate = copy.deepcopy(list_value)
        for i in list_key :
            if i[0] != 0 and i[1] != 0 and i[0] != 49 and i[1] != 49  :
                index1 =  list_key.index([i[0]-1,i[1]]) 
                index2 =  list_key.index([i[0]+1,i[1]])
                index3 =  list_key.index([i[0],i[1]-1]) 
                index4 =  list_key.index([i[0]-1,i[1]+1])
                index5 =  list_key.index([i[0]-1,i[1]-1]) 
                index6 =  list_key.index([i[0],i[1]+1])
                index7 =  list_key.index([i[0]+1,i[1]+1]) 
                index8 =  list_key.index([i[0]+1,i[1]-1])
                index9 =  list_key.index([i[0],i[1]])
                near_values = list_value[index1] + list_value[index2] + list_value[index3] +list_value[index4] +list_value[index5] +list_value[index6] +list_value[index7] +list_value[index8]
                if list_value[index9] == 1 :
    
                    if near_values > 3 or near_values< 2 :
                        list_value_duplicate[index9] = 0
                if list_value[index9] == 0 :
    
                    if near_values == 3 :
                        list_value_duplicate[index9] = 1
        list_value = copy.deepcopy(list_value_duplicate)
        time.sleep(0.1)
    for i in range(len(list_key)) :
        x = list_key[i][0]
        y = list_key[i][1]
        color_value = list_value[i] 
        pygame.draw.rect(screen,(0,color_value*150,color_value*150),(x*10,y*10,10,10))
        
    for i in range (50) :
        for j in range (50) :
            pygame.draw.rect(screen,(0,0,0),(i*10,j*10,10,10),1)
    
    pygame.display.flip()