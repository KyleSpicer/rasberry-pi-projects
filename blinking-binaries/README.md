# Blinking Binaries

- Author: Kyle D. Spicer
- Date: December 29th, 2023
- Rasberry Pi Version: 3+
- Python Version: 2.7.13

## Table Of Contents:
1. [Introduction](#introduction)
2. [Physical Components and Setup](#physical-components-and-setup)
3. [How To Run Program](#how-to-run-program)

## **Introduction:**
### Purpose
- To create a basic python script and learn how basic physical components (bread board, leds, resistors, etc.) interact with an active program.

### What Does The Program Do?
- This program will loop from 0 to 255 and display information in the terminal and the binary representation through the LEDs.

- Example of terminal output:
```
Running Blinking Binaries
Displaying: 0, 00000000
Displaying: 1, 00000001
Displaying: 2, 00000010
Displaying: 3, 00000011
```

## **Physical Components and Setup:**  
### Required Components
1. Rasberry Pi 3+
2. 1 x Bread Board
3. 1 x GPIO ribbon cable (connects pi to bread board)
4. 8 x LEDs
5. 8 x resistors
6. 9 x male-to-male cables (8 for leds, 1 for bread board)  

### Setup Images
![Example Image](images/1.jpg)
![Example Image](images/2.jpg)
![Example Image](images/3.jpg)



## **How To Run Program**
1. Ensure the physical components are properly setup and connected.
2. Simply run the script from the terminal and watch the LEDs work their magic.

Example Terminal Execution:
```
python ./blinking-binaries.py
```