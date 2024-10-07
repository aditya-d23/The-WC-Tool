import os
import sys

def getSize(file_name):
    return os.path.getsize(file_name)

def number_of_lines():
    with open(r"test.txt",'r',encoding="utf8") as fp:
        lines = sum(1 for line in fp)
        return lines
def number_of_word():
    total_word=0
    with open(r"test.txt",encoding="utf8") as fp:
        data=fp.read()
        line=data.split()
        total_word+=len(line)
    return total_word

def count_char():
    total_char=0
    with open(r"test.txt",encoding="utf8") as fp:
        data=fp.read()
        return len(data)

if __name__ =="__main__":
    arguments=sys.argv[1:]
    if(arguments[0]=='-c'):
        size=getSize(arguments[1])
        print(f'{size} {arguments[1]}')
    elif(arguments[0]=='-l'):
        line=number_of_lines()
        print(f'{line} {arguments[1]}')
    elif(arguments[0]=='-w'):
        word=number_of_word()
        print(f'{word} {arguments[1]}')
    elif(arguments[0]=='-m'):
        character=count_char()
        print(f'{character} {arguments[1]}')
    else:
        line=number_of_lines()
        word=number_of_word()
        size=getSize(arguments[0])
        print(f'{line} {word} {size} {arguments[0]}')

