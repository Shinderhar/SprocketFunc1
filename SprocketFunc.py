import json


file_path = str(input("input path to your blueprint(with .blueprint extension): "))
with open(file_path, 'r+') as filer:
    data = json.load(filer)
    for mesh in data["meshes"]:
        mesh["meshData"]["gridSize"] = 0
        for face in mesh["meshData"]["mesh"]["faces"]:
            face["t"] = [1]*len(face["t"])
    filer.seek(0)
    filer.write(json.dumps(data, indent = 4))
    filer.truncate()
print("Success! Grid size set to 0, all thicknesses to 1mm. Enjoy your sprocketing  ")
input("press Enter to exit")


