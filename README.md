WordCount:

A program to count the frequency of words in a large text file

We will be using texts from https://www.gutenberg.org/


Myan02 -> Michael Baburyan

AndresR20 -> Andres Rodriguez

Things to do to correctly run the program:

1. Create a text file to store 'War and Peace' in order to be able to read the file and extract its contents. We got the text file straight from the website you provided us with. You can of course use any file you want, just make sure in the ListSplit() function when you call ReadFile(), that the file name is actually the directory with the specific text file you want to read from, in our case it was "war and peace.txt" because the file was already in our IDE directory.  

2. At the bottom of the program, you will see a write() function with another open() function that allows us to write the contents of our final dict into a new text file for easy access. You can do this by either creating an empty text file and then adding the directory of that text file into the open() function, or simply adding a directory and making a name for a new text file to be created. As seen in our video demo, we had the directory "C:\\\Users\\\babur\\\Desktop\\\text\\\result.txt" but the file result.txt did not exist in that folder. This is fine as it ends up creating a file to hold the dictionary. 

3. When adding a directory, make sure to use two slashes (\\\ instead of simply \\) as one of the is an escape character. Just a heads up to make sure everything works perfectly :)

Doing these three things will ensure you get the correct output given 8 processes. If you want to change the number of processes used, you can follow the video demo and edit the commented lines as we did. 

The link to the 'War and Peace' text: 
https://www.gutenberg.org/cache/epub/2600/pg2600.txt
