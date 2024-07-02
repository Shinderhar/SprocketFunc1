import json
import os

def lsum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return (sum)

def do1(file_path):
    with open(file_path, 'r+') as filer:
        data = json.load(filer)
        for mesh in data["meshes"]:
            mesh["meshData"]["gridSize"] = 0
            for face in mesh["meshData"]["mesh"]["faces"]:
                face["t"] = [1] * len(face["t"])
        filer.seek(0)
        filer.write(json.dumps(data, indent=4))
        filer.truncate()
    print("Success! Grid size set to 0, all thicknesses to 1mm. Enjoy your sprocketing  ")
    input("press Enter to continue")

def do2(file_path):
    valtochange = int(input("Enter the thickness value you want to change:"))
    valchangeto = int(input("Enter the thickness value you want to set:"))
    with open(file_path, 'r+') as filer:
        data = json.load(filer)
        for mesh in data["meshes"]:
            mesh["meshData"]["gridSize"] = 0
            for face in mesh["meshData"]["mesh"]["faces"]:
                if lsum(face["t"])/len(face["t"]) == valtochange:
                    face["t"] = [valchangeto] * len(face["t"])
        filer.seek(0)
        filer.write(json.dumps(data, indent=4))
        filer.truncate()
    print("Success! Grid size set to 0, faces with thicknesses equal to " + str(valtochange) + " are set to " + str(valchangeto))
    input("press Enter to continue")

file_path = str(input("input path to your blueprint(with .blueprint extension): "))
print("blueprint path set as:  " + file_path)
print()
while True:
    os.system('cls')
    print("blueprint path set as:  " + file_path)
    print("PLEASE MAKE BACKUPS BEFORE ALTERING YOUR BLUEPRINTS")
    print()
    print("0 - Exit")
    print("1 - Change all thicknesses in the entire blueprint to 1mm and disable grid snap")
    print("2 - Change all specific thicknesses across the blueprint to a desired value")
    print("3 - Change the blueprint you want to edit")
    checker = str(input("Enter the menu option: "))
    match checker:
        case "0":
            break
        case "1":
            try:
                do1(file_path)
            except Exception:
                input("an error has occurred, press Enter to continue")
        case "2":
            print("warning - this might work in a very junky way if the faces with different desired thicknesses are connected, and i don't want to fix it for now =(")
            try:
                do2(file_path)
            except Exception:
                input("an error has occurred, press Enter to continue")
        case "3":
            file_path = str(input("input path to your new blueprint(with .blueprint extension): "))
            print("blueprint path set as:  " + file_path)
        case _:
            print("wrong input")
            input("press Enter to continue")







