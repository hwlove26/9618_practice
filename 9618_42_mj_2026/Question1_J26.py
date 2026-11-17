TheData = ["laptop",
           "tablet",
           "printer",
           "computer",
           "processor",
           "monitor",
           "memory",
           "cable",
           "touchscreen"]

def FindLongestShortest(array):
    longest = array[0]
    shortest = array[0]
    for i in range(1, len(array)):
        if len(array[i]) > len(longest):
            longest = array[i]
        elif len(array[i]) < len(shortest):
            shortest = array[i]
    print("longest string :", longest)
    print("shortest string :", shortest)

def InsertionSort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

def main():
    global TheData
    FindLongestShortest(TheData)
    print("Before sorting")
    print(TheData)
    InsertionSort(TheData)
    print("After sorting")
    print(TheData)


main()
