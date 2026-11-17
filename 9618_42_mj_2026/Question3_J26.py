StartLinkedList = 2
StartEmptyList = 7

LinkedList = []
LinkedList.append([9512, 5])
LinkedList.append([5541, 3])
LinkedList.append([1999, 0])
LinkedList.append([6651, -1])
LinkedList.append([-1, 6])
LinkedList.append([5612, 1])
LinkedList.append([-1, -1])
LinkedList.append([-1, 4])

def PrintListItems():
    pointer = StartLinkedList
    while pointer != -1:
        print("data :",LinkedList[pointer][0])
        pointer = LinkedList[pointer][1]

def PrintEmptyList():
    pointer = StartEmptyList
    while pointer != -1:
        print("index of empty list :", pointer)
        pointer = LinkedList[pointer][1]

def AddItem(data):
    global StartEmptyList
    global StartLinkedList
    if StartEmptyList != -1:
        newPointer = StartEmptyList
        LinkedList[newPointer][0] = data
        StartEmptyList = LinkedList[newPointer][1]
        LinkedList[newPointer][1] = -1
        pointer = StartLinkedList
        while True:
            if LinkedList[pointer][1] != -1:
                pointer = LinkedList[pointer][1]
            else:
                break
        LinkedList[pointer][1] = newPointer


def main():
    print("Linked list")
    PrintListItems()
    print("Empty list")
    PrintEmptyList()
    AddItem(8451)
    print("Linked list")
    PrintListItems()
    print("Empty list")
    PrintEmptyList()

main()