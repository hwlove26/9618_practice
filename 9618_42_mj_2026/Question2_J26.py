class Avatar:
    def __init__(self, name, glasses, hair, age):
        self.__TheName = name #private, string
        self.__Glasses = glasses #private, boolean
        self.__Hair = hair #private, string
        self.__Age = age #private, integer

    def GetName(self):
        return self.__TheName

    def GetAge(self):
        return self.__Age
        
    def MeetCritera(self, isGlasses, hairColour):
        if isGlasses == self.__Glasses and hairColour == self.__Hair:
            return True
        else:
            return False

AvailableAvatars = []
SelectedAvatars = []
def LoadAvatars():
    global AvailableAvatars
    try:
        file = open("AvatarFile.txt", "r")
        for line in file:
            seperatedLine = (line.strip()).split(" ")
            if seperatedLine[1] == "True":
                seperatedLine[1] = True
            else:
                seperatedLine[1] = False
            AvailableAvatars.append(Avatar(seperatedLine[0], bool(seperatedLine[1]), seperatedLine[2], seperatedLine[3]))
        file.close()
    except e:
        print("cannot read file")

def EnterChoices():
    global AvailableAvatars, SelectedAvatars
    while True:
        choice = input("wearing glasses?(yes or no)")
        if choice == "yes":
            glasses = True
            break
        elif choice == "no":
            glasses = False
            break
        else:
            print("invalid input")
    while True:
        colours = ["black", "blonde", "brown", "pink", "red", "green"]
        choice = input("what is hair colour?(black, blonde, brown, pink, red or green")
        if choice in colours:
            colour = choice
            break
        else:
            print("invalid input")
    SelectedAvatars = []
    for avatar in AvailableAvatars:
        if avatar.MeetCritera(glasses, colour):
            SelectedAvatars.append(avatar)
        

def main():
    global AvailableAvatars, SelectedAvatars
    LoadAvatars()
    EnterChoices()
    print(len(SelectedAvatars))
    for avatar in SelectedAvatars:
        print("name :", avatar.GetName())
        print("age :", avatar.GetAge())
    

main()
