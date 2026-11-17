array = []
headPointer = -1
tailPointer = -1

for i in range(10):
    array.append(-1)

def Enqueue(newItem):
    global array
    global headPointer
    global tailPointer
    if tailPointer >= 9:
        return False
    else:
        if headPointer == -1:
            headPointer = 0
        tailPointer += 1
        array[tailPointer] = newItem
        return True

def Dequeue():
    global headPointer
    global tailPointer
    global array
    if headPointer > tailPointer or headPointer <= -1:
        return -1
    else:
        headPointer += 1
        return array[headPointer-1]

def main():
    global array
    for i in range(6):
        if not Enqueue(int(input("please input integer"))):
            print("queue is full")
    for i in range(4):
        print(Dequeue())


main()
