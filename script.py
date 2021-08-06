import os
import easygui;
import re;

# path = "C:\\a"

# entities = [["student", "admin"], ["don", "contribution"]]
from easygui import boolbox, multenterbox


def replace_folders(search, replace, path):
    dirs = []
    for r, d, f in os.walk(path, topdown=False):
        for dir in d:
            dirname = os.path.join(r, dir)
            replaceFromAbsolute(dirname, search, replace)

    print(dirs)


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
        filename = f.split("\\")[-1];
        print(f.split("\\")[-1]);
        if filename.__contains__(fromString):
            new_file_name = path[:len(filename)] + "\\" + filename.replace(fromString, toString)
            os.rename(f, new_file_name)
            files[index] = new_file_name
            print(new_file_name)


def replaceFromAbsolute(f, fromString, toString):
    filename = f.split("\\")[-1];
    print(f.split("\\")[-1]);
    if filename.__contains__(fromString):
        new_file_name = path[:len(filename)] + "\\" + filename.replace(fromString, toString)
        if (not os.path.exists(new_file_name)):
            os.rename(f, new_file_name)
            print(new_file_name)


def updateDirectories(path, fromString, toString):
    for f in os.listdir(path):
        old = f
        f = f.replace(" ", "_")
        f = re.sub(r'[^a-zA-Z0-9-_]', '', f)
        if old != f:
            os.rename(old, "hd")
            print("renamed " + old + " to " + f)
        if os.path.isdir(f):
            os.chdir(f)
            updateDirectories(".")
            os.chdir("..")


def updateFiles(path, fromString, toString):
    files = getFiles(path)
    replaceOsList(files, fromString, toString)


# r=root, d=directories, f =

def run(fromString, toString):
    replaceInFile(path, fromString, toString)
    updateFiles(path, fromString, toString)
    replace_folders(fromString, toString, path)


def cap(word):
    if (len(word)):
        return word[0].upper() + word[1:]
    return ""


def mapEntities(path, entities):
    if (len(entities)):
        for entity in entities:
            fromString = entity[0];
            toString = entity[1];
            if (len(fromString)):
                fromStrings = [fromString, fromString.lower(), cap(fromString)]
                toStrings = [toString, toString.lower(), cap(toString)]
                for i in range(0, 3):
                    replace_folders(fromStrings[i], toStrings[i], path)
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


path = "C:\\a";
entities = [["l", "jm"]];
message = "Chose folder"
title = ""
if boolbox(message, title, ["Import", "Cancel"]):
    path = easygui.diropenbox("Pick a folder", "xd", "C:\\Users\\Ibrahima\\git");
    while boolbox("Add replacement", "Add replacement?", ["Add", "No"]):
        entities.append(setEntities());
    mapEntities(path, entities);
else:
    pass

"""
Usage: python script.py search_string replace_string dir
Eg. python batchreplace.py galleries productions /Sites/cjc/application/modules/productions/
And it will search recursively in dir
and replace search_string in contents
and in filenames.
Case-sensitive
"""

from sys import argv
