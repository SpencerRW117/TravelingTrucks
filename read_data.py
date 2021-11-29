import csv
import datetime
from HashContainer import HashContainer

#Defines a truck class with an ID number and a list of packages. 
class Truck:
    def __init__(self, truckNum):
        self.truckNum = truckNum
        self.packages = []

#Defines a package class to be stored in the packages list of the Truck class
class Package:
    def __init__(self, id, address, city, state, zip, deliv_time, size, note):
        self.id = id
        self.address = address 
        self.city = city 
        self.state = state
        self.zip = zip
        self.deliv_time = deliv_time
        self.size = size
        self.note = note
        self.start = ""
        self.currTime = self.start
        self.status = "STATUS: HUB"
    
#Reads data from the packages class, loads them into the appropriate trucks as well as into the Hash Table. 
#O(n), where n is the number of records in the packageCSV file
with open('packageCSV.csv') as packageCSV:
    readPackage = csv.reader(packageCSV, delimiter=',')

    packageTable = HashContainer()
    truck1 = Truck(1)
    truck2 = Truck(2)
    truck3 = Truck(3)
    
    for row in readPackage:
        newPack = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        
        if newPack.deliv_time != "EOD":
            if "Must" in newPack.note or "None" in newPack.note:
                truck1.packages.append(newPack)
        if "Can" in newPack.note:
            truck2.packages.append(newPack)
        if "Wrong" in newPack.note:
            newPack.address = "410 S State St"
            newPack.zip = "84111"
            truck3.packages.append(newPack)
        if "Delayed" in newPack.note:
            truck2.packages.append(newPack)
        if newPack not in truck1.packages and newPack not in truck2.packages and newPack not in truck3.packages:
            if len(truck2.packages) > len(truck3.packages):
                truck3.packages.append(newPack)
            else:
                truck2.packages.append(newPack)

        storeKey = newPack.id
        storeVal = [newPack.id, newPack.address, newPack.city, 
            newPack.state, newPack.zip, newPack.deliv_time, 
            newPack.size, newPack.note, newPack.start, newPack.currTime, 
            newPack.status]
        
        packageTable.insert(storeKey, storeVal)

#O(1), a simple accessor to return the Hash Table storing the packages. 
def getPackageTable():
    return packageTable
#O(1), a simple accessor to return a specific truck: 1, 2, or 3
def getTruck(truckNum):
    if truckNum == 1:
        return truck1
    elif truckNum == 2:
        return truck2
    elif truckNum == 3:
        return truck3
    else:
        return None
    

        
        
        
            



