class ToyRecord:
    def __init__(self, name, numBricks, diff, category):
        self.ToyName = name
        self.NumberBricks = numBricks
        self.Difficulty = diff
        self.Category = category

def ReadData(array):
    try:
        file = open("Toys.txt", "r")
        for i in range(16):
            line = file.readline().strip()
            name = line.split(",")[0]
            numBricks = int(line.split(",")[1])
            diff = line.split(",")[2]
            category = line.split(",")[3]
            array.append(ToyRecord(name, numBricks, diff, category))
        file.close()
    except IOError:
        print("File not found")
    return array

def OutputToys(array):
    for i in range(len(array)):
        name = array[i].ToyName
        numBricks = array[i].NumberBricks
        diff = array[i].Difficulty
        category = array[i].Category
        print("name :", name, ", number of bricks :", numBricks, ", difficulty :", diff, ", category:", category)

def SearchToys(array):
    difficulties = ["Easy", "Medium", "Expert"]
    while(True):
        difficulty = input("enter difficulty:")
        if difficulty not in difficulties:
            print("invalid difficulty")
        else:
            break
    targetToys = []
    for i in range(len(array)):
        if array[i].Difficulty == difficulty:
            targetToys.append(array[i])
    return targetToys

def WriteToys(array): #type of array = ToyRecord
    try:
        file = open("SelectedToys.txt", "w")
        for i in range(len(array)):
            string = array[i].ToyName + "," + str(array[i].NumberBricks) + "," + array[i].Difficulty + "," + array[i].Category + "\n"
            file.write(string)
        file.close()
    except:
        print("Cannot write file")


def main():
    Toys = []
    ReadData(Toys)
    OutputToys(Toys)
    searchedToy = SearchToys(Toys)
    WriteToys(searchedToy)

main()