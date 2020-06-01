import json

def fileSearch(fileToSearch, filesObj):
    folder = json.loads(filesObj)
    fileLocList = list()
    __fileSearchRecur(fileLocList, fileToSearch, folder, "", 0)
    return [e[1] for e in sorted(fileLocList)]

# Loc stands for Location
def __fileSearchRecur(fileLocList, fileToSearch, subFolder, subFolderLoc, subFolderDepth):
    for e in subFolder.keys():
        if e == "_files":
            if fileToSearch in subFolder[e]:
                fileLocList.append((subFolderDepth, subFolderLoc + "/" + fileToSearch))
        else:
            __fileSearchRecur(fileLocList, fileToSearch, subFolder[e], subFolderLoc + "/" + e, subFolderDepth + 1)