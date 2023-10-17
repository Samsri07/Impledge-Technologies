# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 17:38:59 2023

@author: Samarth
"""
import time
def myfun(content):
    compound_words = []
    largest = ""
    second_largest = ""
    
    for word in content:
        if any(part in word for part in content if part != word):
            compound_words.append(word)
    
    for word in compound_words:
        if len(word) > len(largest):
            second_largest = largest
            largest = word
        elif len(word) > len(second_largest) and len(largest) != len(word):
            second_largest = word
    
    return largest, second_largest
def compound(content):
    for word in FileContent:
        first = content[:word]
        second = content[word:]
    if first in content and second in content:
        return 1
    else:
        return 0
    
beg = time.time()
FileContent = input("Enter input file path:")
try:
    sf=open(FileContent,"r")
    FileContent = sf.read()
    FileContent.lower()
    
except FileNotFoundError as e:
    print(e)

content = FileContent.split()
print("The list is:",content)
largest,second_largest = myfun(content)
end = time.time()
process_time = end - beg
if largest:
    print(largest)
if second_largest:
    print(second_largest)
OutputFile = input("Enter output file path:")
try:
    of = open(OutputFile,'w')
    OutputFile = of.write("The outputs are:\n")
    OutputFile = of.write(f"largest  = {largest}\n")
    OutputFile = of.write( f"second_largest= {second_largest}\n")
    OutputFile = of.write( f"process_time = {process_time}\n")
except FileNotFoundError as e:
    print(e)
print("Outputs written in output file successfully")
