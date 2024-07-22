# Glenn Truett 
# 4-20-24 
# PythonI Final 
# This program will have a GUI that when activated will display a number on a seven segment display 
 
import RPi.GPIO as GPIO   # this sets up the pins on the rapberry pi as GPIOs (General-Purppose Input/Output) 
import time               # this library allows me to have a clock so that I can make delays in the code. 
import tkinter as tk 
 
GPIO.setmode(GPIO.BCM)    # This is the set up for the mode of the GPIO. 
GPIO.setwarnings(False)   # There were warnings the messed with how the program opperates. this line turns off the warnings 
 
#Define LED pins 
led_pins = [5,6,15,17,22,25,26,27] 
 
#these next two lines set up the led_pins as OUTPUTS. 
for pin in led_pins: 
    GPIO.setup(pin, GPIO.OUT) 
    
# the following function makes all the LED's on the Seven Segment Display turn off. 
def defaultState(): 
    for pin in led_pins: 
        GPIO.output(pin, False) 
        
# the following function allows the LEDs on the seven segement display to light up to make a number Zero. 
def numZero(): 
    defaultState() 
    GPIO.output(5, True) 
    GPIO.output(6, True) 
    GPIO.output(22, True) 
    GPIO.output(27, True) 
    GPIO.output(17, True) 
    GPIO.output(25, True) 
 
# the following function allows the LEDs on the seven segement display to light up to make a number One. 
def numOne(): 
    defaultState() 
    GPIO.output(6,True) 
    GPIO.output(22,True) 
    
# the following function allows the LEDs on the seven segement display to light up to make a number Two. 
def numTwo(): 
    defaultState() 
    GPIO.output(5, True) 
    GPIO.output(6, True) 
    GPIO.output(15, True) 
    GPIO.output(17, True) 
    GPIO.output(27, True) 
 
#the following function allows the LEDs on the seven segement display to light up to make a number three. 
def numThree(): 
    defaultState() 
    GPIO.output(5, True) 
    GPIO.output(6, True) 
    GPIO.output(22, True) 
    GPIO.output(27, True) 
    GPIO.output(15, True) 
    
#the following function allows the LEDs on the seven segement display to light up to make a number four. 
def numFour(): 
    defaultState() 
    GPIO.output(6, True) 
    GPIO.output(22, True) 
    GPIO.output(25, True) 
    GPIO.output(15, True) 
    
def numFive(): 
    defaultState() 
    GPIO.output(5, True) 
    GPIO.output(25, True) 
    GPIO.output(22, True) 
    GPIO.output(27, True) 
    GPIO.output(15, True) 
    
# the following function allows the LEDs on the seven segement display to light up to make a number Six. 
def numSix(): 
    defaultState() 
    GPIO.output(5, True) 
    GPIO.output(15, True) 
    GPIO.output(22, True) 
    GPIO.output(27, True) 
    GPIO.output(17, True) 
    GPIO.output(25, True) 
    
    # the following function allows the LEDs on the seven segement display to light up to make a number Seven. 
def numSeven(): 
    defaultState() 
    GPIO.output(5, True) 
    GPIO.output(6, True) 
    GPIO.output(22, True) 
    
# the following function allows the LEDs on the seven segement display to light up to make a number Eight. 
def numEight(): 
    defaultState() 
    GPIO.output(5, True) 
    GPIO.output(6, True) 
    GPIO.output(22, True) 
    GPIO.output(27, True) 
    GPIO.output(17, True) 
    GPIO.output(25, True) 
    GPIO.output(15, True) 
    
# the following function allows the LEDs on the seven segement display to light up to make a number Nine. 
def numNine(): 
    defaultState() 
    GPIO.output(5, True) 
    GPIO.output(6, True) 
    GPIO.output(22, True) 
    GPIO.output(27, True) 
    GPIO.output(15, True) 
    GPIO.output(25, True) 
    
def randomStuff(): 
    for i in range(20): 
        defaultState() 
        GPIO.output(5,True) 
        time.sleep(0.05) 
        defaultState() 
        GPIO.output(6,True) 
        time.sleep(0.05) 
        defaultState() 
        GPIO.output(22,True) 
        time.sleep(0.05) 
        defaultState() 
        GPIO.output(27,True) 
        time.sleep(0.05) 
        defaultState() 
        GPIO.output(17,True) 
        time.sleep(0.05) 
        defaultState() 
        GPIO.output(15,True) 
        time.sleep(0.05) 
        defaultState() 
        GPIO.output(25,True) 
        time.sleep(0.05) 
        defaultState() 
    
    
    
    
def countDown(): 
    defaultState() 
    numNine() 
    time.sleep(1) 
    defaultState() 
    numEight() 
    time.sleep(1) 
    defaultState() 
    numSeven() 
    time.sleep(1) 
    defaultState() 
    numSix() 
    time.sleep(1) 
    defaultState() 
    numFive() 
    time.sleep(1) 
    defaultState() 
    numFour() 
    time.sleep(1) 
    defaultState() 
    numThree() 
    time.sleep(1) 
    defaultState() 
    numTwo() 
    time.sleep(1) 
    defaultState() 
    numOne() 
    time.sleep(1) 
    defaultState() 
    numZero() 
    time.sleep(1) 
    defaultState() 
    
 
def button_nothing(): 
   defaultState() 
    
def button_zero(): 
    numZero() 
    
def button_one(): 
    numOne() 
    
def button_two(): 
    numTwo() 
 
def button_three(): 
    numThree() 
    
def button_four(): 
    numFour() 
    
def button_five(): 
    numFive() 
    
def button_six(): 
    numSix() 
    
def button_seven(): 
    numSeven() 
    
def button_eight(): 
    numEight() 
    
def button_nine(): 
    numNine() 
    
def button_count_down(): 
    countDown() 
    
def button_random_stuff(): 
    randomStuff() 
    
    
 
def main(): 
    
    root = tk.Tk() # Create the main window 
    
    # Set the window size 
    root.geometry("600x600") # 1 inch = 100 pixels (approximately) 
    
    #create buttons 
    tk.Button(root, text="Nothing", command=button_nothing).pack(expand=True, fill='both') 
    tk.Button(root, text="Zero", command=button_zero).pack(expand=True, fill='both') 
    tk.Button(root, text="One", command=button_one).pack(expand=True, fill='both') 
    tk.Button(root, text="Two", command=button_two).pack(expand=True, fill='both') 
    tk.Button(root, text="Three", command=button_three).pack(expand=True, fill='both') 
    tk.Button(root, text="Four", command=button_four).pack(expand=True, fill='both') 
    tk.Button(root, text="Five", command=button_five).pack(expand=True, fill='both') 
    tk.Button(root, text="Six", command=button_six).pack(expand=True, fill='both') 
    tk.Button(root, text="Seven", command=button_seven).pack(expand=True, fill='both') 
    tk.Button(root, text="Eight", command=button_eight).pack(expand=True, fill='both') 
    tk.Button(root, text="Nine", command=button_nine).pack(expand=True, fill='both') 
    tk.Button(root, text="Count Down", command=button_count_down).pack(expand=True, fill='both') 
    tk.Button(root, text="Random", command=button_random_stuff). pack(expand=True, fill='both') 
    
    
    root.mainloop() # Start the event loop 
                              
    
 
if __name__=="__main__": 
    
    main()                                                                                     

 