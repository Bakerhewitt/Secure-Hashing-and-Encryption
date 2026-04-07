# Secure Hashing and Encryption
The two programs in this repository are demonstrations of Hashing and Encyrption/Decryption using a preset key.
The Hashing program is very basic, and allows for a user input string or file hashing, depending on user choice.
The Encryption/Decryption program is similarly basic, and the key variable is preset and non-randomized. This app displays the input > encryption > decryption. 

## How It's Made:
Tech used: Python in Visual Studio Code

The Hashing program started with the _stringhash_ function, which was very straightforward. I worked with a couple variations of _filehash_ before settling on the current version, which Visual Studio Code helped to debug.

The Encryption Program was initially built with a random key variable, but I was having issues getting it to properly encrypt the entire string. It was just encrypting one or two letters each time. I opted to use a preset key instead, to see if the substitution was working, which it was. This is NOT a secure encryption progrm and should not be used as such.

## Lessons Learned:
Hashing is fairly straight forward for string inputs, but file sourcing is more complicated. I had some issues with inputting the filename, and learned about .strip(' " ') in my Google searches of the error codes. Very helpful tool!
The other lesson I learned is not to wait until the last minute to finish my assignments, as I did not have time to finish the 3rd app for this assignment, which was meant to simulate a digital signature. (Pardon my sarcasm I am tired)
