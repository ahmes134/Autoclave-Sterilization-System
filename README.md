# Autoclave Sterilization System

The purpose of this project was to design a system for securely transferring surgical tools to an autocave for sterilization. There were two subteams for this project, one for modelling the container and another for the programming of the robotic arm. As part of the computing team, I had to write code in python to operate the robotic arm using two virtual potentiometers. The computer program interfaces with Quanser Interactive Labs (Q-labs).

The program allows a user to operate the robotic arm and consists of 4 main functions: pick up, rotate base, drop-off and continue/terminate. Each function takes in the container ID as a parameter to make decisions. The pick-up function uses precise coordinates to move the arm to where the box is spawned and then it adjusts the gripper strength based on the box size, allowing it to lift the box up. The rotate base function utilizes a while loop that allows the user to incrementally turn the arm until it is within the range of the same-coloured autoclave. This function operates based on the potentiometer inputs. The right potentiometer reading is used to move the base relative to the calculated difference of the new and old readings. The left potentiometer allows the user to exit the while loop. Once the arm reaches a close range to the respective autoclave, the function returns “True”, thus, verifying that the box is ready for drop-off. The drop off function uses the container ID to determine the corresponding location and based on the threshold of the left potentiometer, it drops the container in position 1 or controls the autoclave drawer and drops off in position 2. Finally, the continue or terminate function checks the length of the list of dropped off container IDs to determine whether the cycle is completed and terminates the program accordingly.

This project taught me the fundamentals of design and problem-solving. Through this project, I was able to apply my programming skills to a real-life application. My team and I were able to produce code for operating a robotic arm in a way that it utilizes the potentiometers and interfaces with the environment as outlined in the project module. This project allowed me work on my problem-solving and troubleshooting skills.

### Technical Skills

> *Python

> *Autodesk Inventor

> *Granta 

> *Problem-solving

### Non-Technical Skills

> *Communication

> *Team-work
