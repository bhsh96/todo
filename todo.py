import subprocess
import time

menu = "\na) add\n"\
        "b) edit\n"\
        "c) del\n"\
        "d) exit"


list = []
def read():
    global list
    with open('/home/bhyung/Desktop/i/todo/list.txt','r+') as f:
        list = f.readlines()
        if len(list) == 0:
            print("todo empty!")
        else:
            show(list)

def show(page):
    i=1
    for l in page:
        print(i,". ", l.rstrip(), sep='')
        i = i+1

def add(task):
    with open('/home/bhyung/Desktop/i/todo/list.txt','a') as f:
        f.write(task + "\n")
        
def edit(num):
    try:
        global list
        num = int(num)
        if num <= 0 or num > len(list):
            raise ValueError()
        print(list[num-1],end="")
        new_task = input()
        list[num-1] = new_task

        with open('/home/bhyung/Desktop/i/todo/list.txt','w') as f:
            for l in list:
                f.write(l)
    except ValueError:
        clear()
        print("Please enter a valid number!\n")
        return 1

def remove(num):
    try:
        global list
        num = int(num)
        if num <= 0:
            raise ValueError()
        del list[num-1]
        with open('/home/bhyung/Desktop/i/todo/list.txt','w') as f:
            for l in list:
                f.write(l)
    except ValueError:
        clear()
        print("Please enter a valid number!\n")
        return 1

def confirm():
    print("Are you sure? (y/n)")
    conf = input()
    if conf == "y" or conf == "Y" or conf == "":
        return
    else:
        clear()
        main()

def clear():
    subprocess.Popen("clear")
    time.sleep(0.01)


clear()
def main():
    while(True):
        subprocess.Popen(['cat','/home/bhyung/Desktop/i/todo/asciiart.txt'])
        time.sleep(0.01)
        read()
        print("\n"+menu)
        text = input()

        if text == "a":
            print("New task: ",end="")
            task = input()
            confirm()
            add(task)

        elif text == "b":
            print("Edit task: ",end="")
            num = input()
            confirm()
            result = edit(num)
            if result == 1:
                continue

        elif text == "c":
            print("Remove task: ",end="")
            num = input()
            confirm()
            result = remove(num)
            if result == 1: 
                continue

        elif text == "d":
            confirm()
            clear()
            exit()

        else:
            clear()
            print("Please input valid number!\n")
            continue 

        clear()

main()
