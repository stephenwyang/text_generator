# Text Generator (Sudoku Square)
This repository contains a simple text generator to create sudoku-style squares.

In order to run, install all needed libraries and create the necessary folders, change the specifications, and then run this command in the command prompt
```
python generator.py
```
## Prereqs
1) Make sure PIL (or Pillow) is installed as a library, this may be a bit finnicky to work with
2) Please create a res folder (with subfolders id1 to id9)
3) Either create a fonts folder to keep the fonts, or find where it is located in the system to change the code on line 62 in order for it to work.
## Changeable items
Line 62 - Change what font we want to use, as well as the size

Line 63 - Change what font color to use

Line 64 - Change the amount of images we want to generate per number

Line 59 - createRandomLoc, turn to False if you want it in the center instead of randomly around the square
## Possible future changes
Instead of having the user download fonts and put them in a folder try to have the program either scan the computer to find where the font files are located, or 