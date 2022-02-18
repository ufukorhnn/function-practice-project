import simplejson
import os
from typing import Dict,List

def DisplayMenu() -> None:
    print("1.Show All Data")
    print("2 Find Data")
    print("3 Add Data")
    print("4 Delete a Data")
    print("5 Exit")

def MenuLoop() -> str:
    while True:
        DisplayMenu()
        option:str = input("Choose (1-5): ")
        print("\n")
        if option.isdigit() and 1 <= int(option) <= 5:
            break
    return option

def MainLoop() -> None:
    while True:
        option:str = MenuLoop()
        if option == "1":
            ListRecords()
        elif option == "2":
            SearchRecord()
        elif option == "3":
            AddRecord()
        elif option == "4":
            DeleteRecord()
        elif option == "5":
            break


def ListRecords() -> None:
    recordsList:List[Dict[str,str]] = ReadFile()
    print(f"Number of records: {len(recordsList)}\n")
    count:int = 1
    if len(recordsList) == 0:
        print("Contacts is empty")
    for record in recordsList:
        print(f"{count}. {record.get('name', ' ')} {record.get('surName', ' ')} {record.get('telNumber', ' ')}")
        count +=1
    print()


def SearchRecord() -> None:
    print("Finding contact page")
    name:str = input("name: ")
    surName:str = input("surname: ")
    recordslist:list = SearchRecordFromFile(name, surName)
    if recordslist:
        for record in recordslist:
            print(f"Phone No:{record.get('telNumber')}")
        print("\n")
    else:
        print(f"{name} {surName} User not registered.\n")


def AddRecord() -> None:
    print("Add new contact: ")
    name:str = input("Name: ")
    surName:str = input("Surname: ")
    telNumber:str = input("Phone No: ")
    print(f"New data: {name} {surName} - {telNumber}")
    
    if AreYouSure():
        AddRecordToFile(name, surName, telNumber)
        print("Successfully added.")


def DeleteRecord() -> None:
    print("Delete Operation")
    name:str = input("Name: ")
    surName:str = input("Surname:")
    recordsList:list = SearchRecordFromFile(name, surName)
    if recordsList:
        for record in recordsList:
            print(f"{record.get('telNumber')}")
        print("\n")
        if AreYouSure():
            DeleteRecordFromFile(recordsList)
            print("Successfully deleted\n")
    else:
        print(f"{name} {surName} user not found.\n\n")

def AreYouSure() -> bool:
    while True:
        answer:str = input("Are u sure? Y/N: ")
        print()
        if answer.upper() == "Y":
            return True
        elif answer.upper() == "N":
            return False


def ReadFile() -> list:
    recordsList:list = []
    if os.path.isfile("data.txt"):
        
        with open("data.txt", "r") as fileObject:
                recordsList = simplejson.load(fileObject)

    return recordsList


def WriteFile(recordsListParam : list) -> None:
    with open("data.txt", "w") as fileObject:
        simplejson.dump(recordsListParam, fileObject)


def SearchRecordFromFile(nameParam : str, surNameParam : str) -> list:
    recordsList:list = ReadFile()
    responseList:list = []
    for record in recordsList:
        if record.get("name").upper() == nameParam.upper() and \
                record.get("surName").upper() == surNameParam.upper():
            responseList.append(record)
    return responseList


def AddRecordToFile(nameParam : str, surNameParam : str, telNumberParam : str) -> None:
    recordsList:list = ReadFile()
    recordDict:Dict[str,str] = dict(name = nameParam, surName = surNameParam, telNumber = telNumberParam)
    recordsList.append(recordDict)
    WriteFile(recordsList)


def DeleteRecordFromFile(recordsListParam : list) -> None:
    recordsList:list = ReadFile()
    for record in recordsList:
        for recordForDelete in recordsListParam:
            if record.get("name") == recordForDelete.get("name") and \
                record.get("surName") == recordForDelete.get("surName"):
                recordsList.remove(recordForDelete)
    WriteFile(recordsList)


if __name__ == "__main__":
    MainLoop()
