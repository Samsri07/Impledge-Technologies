# Impledge Technologies
 I wrote the code using Python in order to solve the problem: 'Find the longest compounded word'
## Features
The code is designed specifically to process an input file and return the longest and second longest compound word present in the input file.
### Overview
The program is a python script that allows a user to input a list consisting of random words, detect compound words out of these random words and display the longest and second longest compound word in an another output file.

## Prerequisites

Before running this program, make sure you have Python 3.7 or higher installed.
## Installation
If Anaconda is installed on your system (laptop), click on Anaconda Prompt
, then write the code given below in Anaconda prompt in order to install the required packages.

```bash
pip install package_name.txt


```
Steps and approach considered in order to solve the problem
---
Firstly, i imported time package in order to calculate processing time for the input file.

Step 1
---
The very first step involves specifying the path of the input file. After the input file is accessed, the contents of the file are read by using read() and stored in 'FileContent' variable.
Then we remove the unnecessary spacing which may be present in the file with the help of split() function and converted into a list.

Step 2
---
The function myfun() is called where it takes a list of words as input and is designed to identify and return the largest and second largest compound words from the input list.
compound_words is initialized as an empty list whereas largest and second_largest are initialized as empty strings.
The for loop in the function iterates through each word which is present in the list.
The function returns largest and second largest compound word present in the list.

Step 3
---
We calculate the processing time by subtracting the values of end and beg.


Step 4
---
Lastly, we open an output file by specifying its path and write the value of the largest compound word, second largest compound word and the processing time in that particular output file.








