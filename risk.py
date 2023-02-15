"""

Your name: Vanessa M Diaz
Your e-mail: dreamfreely@icloud.com
Date finished: January 21, 2023
"""

# Step 1
# Collect the user's input. You can either use the
# argparse library for this (recommended) or the
# input() function.

import random
import numpy as np

attackers_remaining = 5
defenders_remaining = 5


while attackers_remaining >1 or defenders_remaining >0:
    
    #die roll
    a_die_1 = random.randint(1,6)
    a_die_2 = random.randint(1,6)
    a_die_3 = random.randint(1,6)
    d_die_1 = random.randint(1,6)
    d_die_2 = random.randint(1,6)
 
    #combining all sets of dice   
    full_a = [a_die_1, a_die_2, a_die_3]
    full_a.sort(reverse=True)
    mid_a = [a_die_1,a_die_2]
    mid_a.sort(reverse=True)
    min_a = [a_die_1]
    full_d = [d_die_1, d_die_2]
    full_d.sort(reverse=True)
    min_d = [d_die_1]
    
    #attacker 3 and defender 2
    if attackers_remaining > 3 and defenders_remaining >= 2:
        if full_a[0]>full_d[0] and full_a[1]>full_d[1] :
            defenders_remaining -= 2
            
        elif full_a[0]<=full_d[0] and full_a[1]<=full_d[1]:
            attackers_remaining -= 2
            
        elif full_a[0]>full_d[0] and full_a[1]<=full_d[1]:
            attackers_remaining -= 1
            defenders_remaining -= 1
         
        elif full_a[0]<=full_d[0] and full_a[1]>full_d[1]:
            attackers_remaining -= 1
            defenders_remaining -= 1
         

    #attacker 2 and defender 2
    elif 2< attackers_remaining <4 and defenders_remaining >= 2:
        if mid_a[0]>full_d[0] and mid_a[1]>full_d[1] :
            defenders_remaining -= 2
           
        elif mid_a[0]<=full_d[0] and mid_a[1]<=full_d[1]:
            attackers_remaining -= 2
         
        elif mid_a[0]>full_d[0] and mid_a[1]<=full_d[1]:
            attackers_remaining -= 1
            defenders_remaining -= 1
        
        elif mid_a[0]<=full_d[0] and mid_a[1]>full_d[1]:
            attackers_remaining -= 1
            defenders_remaining -= 1
        

    #attacker 1 and defender 2
    elif 1< attackers_remaining <3 and defenders_remaining >= 2:
        if min_a[0]>full_d[0]:
            defenders_remaining -= 1
           
        elif min_a[0]<=full_d[0]:
            attackers_remaining -= 1
         

    #attacker 3 and defender 1 
    elif attackers_remaining > 3 and 0<defenders_remaining<2:
        if full_a[0]>min_d[0]:
            defenders_remaining -= 1
          
        elif full_a[0]<=min_d[0]:
            attackers_remaining -= 1
        
        
    #attacker 2 and defender 1
    elif 2< attackers_remaining <4 and 0<defenders_remaining<2:
        if mid_a[0]>min_d[0]:
            defenders_remaining -= 1
          
        elif mid_a[0]<=min_d[0]:
            attackers_remaining -= 1
          
        
    #attacker 1 and defender 1
    elif 1< attackers_remaining <3 and 0<defenders_remaining<2:
        if min_a[0]>min_d[0]:
            defenders_remaining -= 1
      
        elif min_a[0]<=min_d[0]:
            attackers_remaining -= 1
 
    else:
        break
        

         
# Step 3
# Display the output to the user.
# To conform with our grader's required format, we've already 
# done this for you. Just make sure you set the number of 
# attackers remaining to the `attackers_remaining` variable and 
# the number of defenders remaining to the `defenders_remaining`
# variable in Step 2 of this script.


print(f"Attacker: {attackers_remaining} remaining; Defender: {defenders_remaining} remaining")

# Step 4
# Run `python sanity_check.py` to confirm that your script
# handles inputs and outputs correctly

