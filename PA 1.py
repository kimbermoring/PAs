# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 10:35:21 2024

@author: KLMoring
"""
import random 
from tabulate import tabulate
import time

def one_dimension(steps):
    
    particle_location_x = 0 # intialize the location of the particle
    count = 0 
    
    for value in range(steps): 
        step = random.choice(['left','right'])
        if step == 'left' :
            particle_location_x -= 1 
        elif step == 'right': 
            particle_location_x +=1 

        if particle_location_x == 0:
            count += 1
            break
    
    return count

def two_dimensions(steps): 
    
    particle_location_x = 0
    particle_location_y = 0
    count = 0 
    
    for value in range(steps): 
        step = random.choice(['left','right','up', 'down'])
        if step == 'left' :
            particle_location_x -= 1 
        elif step == 'right': 
            particle_location_x += 1 
        elif step == 'up': 
            particle_location_y += 1 
        elif step == 'down' : 
            particle_location_y -= 1
        
        if particle_location_x == 0 and particle_location_y == 0:
            count += 1
            break
    
    return count

def three_dimensions(steps): 
    
    particle_location_x = 0
    particle_location_y = 0
    particle_location_z = 0 
    count = 0 
        
    for value in range(steps): 
        step = random.choice(['left','right','up', 'down', 'out', 'in'])
        if step == 'left' :
            particle_location_x -= 1 
        elif step == 'right': 
            particle_location_x += 1 
        elif step == 'up': 
            particle_location_y += 1 
        elif step == 'down' : 
            particle_location_y -= 1
        elif step == 'out': 
            particle_location_z += 1 
        elif step == 'in': 
            particle_location_z -=1 
        
        if particle_location_x == 0 and particle_location_y == 0 and particle_location_z == 0:
            count += 1
            break

    return count

def main(): 
    
    NUM_MOVES = [20, 200, 2000, 20000, 200000, 2000000]
    probability_1D = []
    probability_2D = [] 
    probability_3D = []
    
# 1-d 
    for nums in NUM_MOVES:
       total_count = 0
       for value in range(1,101): 
            total_count += one_dimension(nums)
            prob_1D = total_count
       probability_1D.append(prob_1D)

# 2-d
    for nums in NUM_MOVES:
      total_count = 0 
      for value in range(1,101): 
            total_count += two_dimensions(nums)
            prob_2D = total_count
      probability_2D.append(prob_2D)
     
# 3-d
    start_time = time.time()
    
    for nums in NUM_MOVES:
      total_count = 0 
      for value in range(1,101): 
            total_count += three_dimensions(nums)
            prob_3D = total_count
      probability_3D.append(prob_3D)
      
    end_time = time.time() 
    elapsed_time = end_time - start_time

# Dimensions table 
    data_dimensions = [
            ['1D', f'{probability_1D[0]}', f'{probability_1D[1]}', f'{probability_1D[2]}', f'{probability_1D[3]}', f'{probability_1D[4]}', f'{probability_1D[5]}'], 
            ['2D', f'{probability_2D[0]}', f'{probability_2D[1]}', f'{probability_2D[2]}', f'{probability_2D[3]}', f'{probability_2D[4]}', f'{probability_2D[5]}'], 
            ['3D', f'{probability_3D[0]}', f'{probability_3D[1]}', f'{probability_3D[2]}', f'{probability_3D[3]}', f'{probability_3D[4]}', f'{probability_3D[5]}']
            ]
    
    title_1 = "Percentages of time particle returned to origin:"
    headers = ["Number of steps:", "20", "200", '2,000', '20,000', '200,000', '2,000,000']

    table_1 = tabulate(data_dimensions, headers, tablefmt="grid")
  
    print(f'\n{title_1}')
    print(table_1)
    print()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
# 3D Run time table
    title_2 = 'Run time of particle in 3D:'
    headers = [['Total time (seconds):', f'{elapsed_time:.2f}']]
    
    table_2 = tabulate(headers, tablefmt='grid')
    
    print(title_2)
    print(table_2)

    return probability_1D, probability_2D, probability_3D

main()