# SprocketFunc1
A simple executable that lets you change your sprocket blueprint's thicknesses and set grid size as 0 to make the editing experience simpler
Even if there isn't a chance that the program can corrupt the blueprint, PLEASE make a backup of your creation before applying this to it. I don't want to be responsible for art being destroyed

Sorry for the wacky executable packaging, doing it all properly in one file made windows defender falsely flag it as malware

# How to use:
If you do not have a python IDE or wish to not use it:
1. Download the zip file (code -> download zip) with the project
2. Unpack the zip file into the folder of choice
3. Navigate to the SprocketFunc folder
4. Run the program
5. Inside the console, enter or insert the path to your .blueprint file with the name of the file and the extension. (example: C:\Users\user\Documents\My Games\Sprocket\Factions\Default\Blueprints\Vehicles\Centurion.blueprint)
6. Choose one of the functionalities byt typing in the number(1 - Changing ALL the thicknesses to 1, 2 - changing specific thicknesses to a set number you can input later,  and 3 - changing the path to your blueprint)
7. Press Enter
8. Follow the instructions provided by the program if there are any and press Enter after entering any values
9. If you wish to exit, in the main menu, type 0 or close the window.
10. Enjoy

If you have a python IDE (or do not trust the executable):
1. Download a python IDE or open one of choice
2. Download the SprocketFunc.py file from the project or copy the code into your IDE of choice
3. verify that the code is trustworthy and run it
4. enter or insert the path to your .blueprint file with the name of the file and the extension.(example: C:\Users\user\Documents\My Games\Sprocket\Factions\Default\Blueprints\Vehicles\Centurion.blueprint)
5. Choose one of the functionalities by typing in the number (1 - Changing ALL the thicknesses to 1, 2 - changing specific thicknesses to a set number you can input later,  and 3 - changing the path to your blueprint)
6. press Enter
7. Follow the instructions provided by the program if there are any and press Enter after entering any values
8. If you wish to exit, in the main menu, type 0, or terminate the program
9. Enjoy

#Update 1:
Have added a functionality to change specific thickness values that you will input in the program to a value that you also input (it sets the point thickness values of a face to a specific number, so this could cause some issues)
Have added a functionality to change the blueprint path you inputted to change different blueprints without closing it
Have added a recursive menu to ease the usage of the program
Have added handling of errors, so theoretically the program won't abruptly close itself if the blueprint is entered incorrectly
