import os
import pathlib

os.system('cls')

print('1. Get information and display to screen')
print('2. Call user created functions')
print('3. Write List of files to file')
print('4. Read specified file')

inpNumber = eval(input('Enter a number of task to do:'))

if inpNumber == 1:
    companyName = "Dunwoody College"
    programName = "Computer Networking"
    uName = os.environ['username']
    classFirst = input("Provide the name of your first class: ")
    classSecond = input("Provide the name of your second class: ")
    print("Logged on as " + uName + " at " + companyName + " in department: " + programName)
    print("My first class is " + classFirst + " and my second class is " + classSecond)

elif inpNumber == 2:
    def GetState():
        nameState = input('Name a state?')
        return nameState;
    def FormatState(nameState):
        if len(nameState) < 8:
            leftState = nameState.ljust(8)
            return nameState;
        return nameState;
    state = GetState()
    newState = FormatState(state)
    print("State was " + state + "and now it is " + newState)

elif inpNumber == 3:
    file = input("What do you want to name the file you are creating?")
    fList = []
    for p in pathlib.Path('.').iterdir():
        if p.is_file():
            fList.append(p)
    with open(file, "w") as fileWrite:
        fileWrite.write("These are my files:\n")
        for f in fList:
            fileWrite.write(f.name)
            fileWrite.write("\n")

elif inpNumber == 4:
    readFile = input("The name of the file you want to read:")
    with open(readFile, "r+") as fileRead:
        print(fileRead.read())