import os
import easygui;

# path = "C:\\a"

# entities = [["student", "admin"], ["don", "contribution"]]
from easygui import boolbox, multenterbox


def replaceInFile(path, fromString, toString):
    files = getFiles(path)
    for filein in files:
        f = open(filein, 'r')
        filedata = f.read()
        f.close()

        newdata = filedata.replace(fromString, toString)

        f = open(filein, 'w')
        f.write(newdata)
        f.close()


def getDirectories(path):
    directories = []
    for r, d, f in os.walk(path):
        for directory in d:
            directories.append(os.path.join(r, directory))
    return directories


def getFiles(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
    return files


def replaceOsList(files, fromString, toString):
    print("Replacing folders and files names from " + fromString + " to " + toString)
    for index, f in enumerate(files):
        if f[len(path):].__contains__(fromString):
            new_file_name = path + f[len(path):].replace(fromString, toString)
            os.rename(f, new_file_name)
            files[index] = new_file_name
            print(new_file_name)


def updateDirectories(path, fromString, toString):
    directories = getDirectories(path)
    replaceOsList(directories, fromString, toString)


def updateFiles(path, fromString, toString):
    files = getFiles(path)
    replaceOsList(files, fromString, toString)


# r=root, d=directories, f =

def run(fromString, toString):
    updateDirectories(path, fromString, toString)
    updateFiles(path, fromString, toString)
    replaceInFile(path, fromString, toString)


def cap(word):
    if (len(word)):
        return word[0].upper() + word[1:]
    return ""


def gg():
    for entity in entities:
        fromString = entity[0]
        toString = entity[1]
        if (len(fromString)):
            fromStrings = [fromString, fromString.lower(), cap(fromString)]
            toStrings = [toString, toString.lower(), cap(toString)]
            for i in range(0, 3):
                run(fromStrings[i], toStrings[i])
        else:
            print("Cant replace to " + toString + " if there is no value ");
            break;


def setEntities():
    msg = "Replace what ?"
    title = "Rename"
    fieldNames = ["From", "To"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg, title, fieldNames)
    print(fieldValues)
    while 1:
        if fieldValues == None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
        if errmsg == "": break  # no problems found
        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
    print("Reply was:", fieldValues);
    return fieldValues;


path = "";
entities = [];
message = "Chose folder"
title = ""
if boolbox(message, title, ["Import", "Cancel"]):
    # path = easygui.diropenbox("Pick a folder", "xd", "C:\\Users\\Ibrahima\\git");
    while boolbox("Add replacement", "Add replacement", ["Add", "Cancel"]):
        entities.append(setEntities());
    gg();
else:
    pass
