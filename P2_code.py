ip_address = 'localhost' # Enter your IP Address here
project_identifier = 'P2B' # Enter the project identifier i.e. P2A or P2B
#--------------------------------------------------------------------------------
import sys
import random
sys.path.append('../')
from Common.simulation_project_library import *

hardware = False
QLabs = configure_environment(project_identifier, ip_address, hardware).QLabs
arm = qarm(project_identifier,ip_address,QLabs,hardware)
potentiometer = potentiometer_interface()
#--------------------------------------------------------------------------------
# STUDENT CODE BEGINS
#---------------------------------------------------------------------------------

container_id = [["red", "small"], ["green", "small"], ["blue", "small"],  ["red", "large"], ["green", "large"], ["blue", "large"]]

#picks up the bin from pick up location, adjusts gripper value based on bin size, lifts bin up
def pick_up(num):
        
        p_coord = [0.591,0.073, 0.017]
        arm.move_arm(p_coord[0], p_coord[1], p_coord[2])
        time.sleep(2)
        
        if num == 1 or num == 2 or num == 3: #small
                arm.control_gripper(37)
                print("small")
        else: #big
                arm.control_gripper(28)
                print("big")
                
        time.sleep(2)
        arm.move_arm(0.406, 0.0, 0.483)
        
#rotates arm base incrementally based on right potentiometer reading as long as left potentiometer is between 0.5 and 1.0 (included)
def rotate_base(num):
        old_reading = potentiometer.right() #save initial potentiometer value

        #runs while the left potentiometer is in desired threshold
        while 0.5 <= potentiometer.left() <= 1.0:
                if potentiometer.right != 0.5:
                        #rotates the base in constant/small degrees based on the change in potentiometer values
                        arm.rotate_base((potentiometer.right()- old_reading)*1200)
                        old_reading = potentiometer.right()

                        #continuously checks if the bin is in range of the corresponding autoclave
                        red = arm.check_autoclave('red')
                        green = arm.check_autoclave('green')
                        blue = arm.check_autoclave('blue')
                        
                # returns True if the arm is facing the correct box for a given id  
                if red == True and (num ==1 or num ==4):
                        print("Base position has reached red")
                        return True
                if green == True and (num ==2 or num ==5):
                        print("Base position has reached green")
                        return True
                if blue == True and (num==3 or num==6):
                        print("Base position has reached blue")
                        return True

#drops off the container to position 1 or position 2 and opens/closes autoclave drawer as needed
#left potentiometer must be greater than 0.5 to operate
def drop_off(num):
        
        bin_colour = container_id[num-1][0]
        bin_size = container_id [num-1][1]
        input_left = potentiometer.left()
        
        if 0.5 < input_left < 1.0:
                if num == 1: #small red 
                        arm.move_arm(-0.0,0.634, 0.355)

                if num ==2: #small green
                        arm.move_arm(-0.624, 0.266, 0.356)

                if num ==3: #small blue
                        arm.move_arm(-0.023, -0.65, 0.308)
                time.sleep(1)
                        
        elif input_left == 1.0:
                 arm.activate_autoclaves()
                 if num ==4: #large red
                         arm.move_arm(-0.0,0.42, 0.15)

                 if num ==5: #large green
                         arm.move_arm(-0.46,0.150, 0.13)

                 if num ==6: #large blue
                         arm.move_arm(-0.0,-0.42, 0.15)

                 arm.open_autoclave(bin_colour)
                 time.sleep(1)
                 
        arm.control_gripper(-37)
        time.sleep(2)
        arm.home()
        arm.open_autoclave(bin_colour, False)
        print(bin_colour, "has been dropped off")

#generates random container IDs and returns new list
def random_num_generator():
        Id_List = [1,2,3,4,5,6]
        Id = random.sample(Id_List,6)
        print(Id)
        return Id

#checks if all 6 bins have been dropped off based on list length
def cont_terminate(dropped_cont_ids):
        if len(dropped_cont_ids) == 6:
                print("Program is finished!")
                exit()
        else:
                print("continue program")
                
        
        
def main():
        dropped_cont_ids = []
        Id = random_num_generator()
        for num in Id:
                arm.spawn_cage(num)
                time.sleep(2)
                pick_up(num)
                time.sleep(2)

                #runs until rotate base returns True
                while rotate_base(num) != True:
                        rotate_base(num) 
                        time.sleep(4)
                drop_off(num)
                #keeps track of which containers have been dropped off by adding num to list
                dropped_cont_ids.append(num)
                cont_terminate(dropped_cont_ids)
        
main()
        
#---------------------------------------------------------------------------------
# STUDENT CODE ENDS
#---------------------------------------------------------------------------------



# reminder rotate base might have an error so test really well.
# continue / terminate function.
# more comments
# double check but I think we are not allowed to have more functions than the required ones.
# left potentiometer controls the drop off location hint the threshholds, right controls the rotate base function, both at 0.5 spawn new container.


                          
    

