"""Bitmap Message (barebones version)
by Al Sweigart al@inventwithpython.com
Displays a text message according to the provided bitmap image."""
import sys, pyperclip

bitmap = """
        ********
     ********
   ********
  ********
   ********
     ********
        ********
       ********
     ********
********************
********************
**************************
********************    **
********************    **
********************    **
*************************
********************
 ******************
"""

print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
print('Enter the message to display with the bitmap.')
message = input('> ')

# create a shaped massage out of msg:
shapedMsg = """ """
# Loop over each line in the multi-line bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i in range(len(line)):
        if line[i] == ' ':
            # add an empty space since there's a space in the bitmap:
            shapedMsg += ' '
        else:
            # append character from the message:
            shapedMsg += message[i % len(message)]
    # end the line:
    shapedMsg += '\n'
# copy to clipboard to use elsewhere
pyperclip.copy(shapedMsg)
