import csv
from datetime import datetime, timedelta
from read_data import Package, Truck
import read_data

distanceTable = []
addressList = []
distanceCSV= csv.reader(open("distanceCSV.csv"), delimiter=',')
addressCSV = csv.reader(open("addressCSV.csv"))
packageHashTable = read_data.getPackageTable()
#Reads in the distance table, O(n)
for row in distanceCSV:
    distanceTable.append(row)
#Reads in the address table, O(n)
for row in addressCSV:
    addressList.append(row)

#Set initial departure times for each truck, O(3n) --> O(n), where n is the number of packages on each truck. 
first_truck_departure = timedelta(hours=8, minutes=00, seconds=00)
second_truck_departure = timedelta(hours=9, minutes=10, seconds=00)
third_truck_departure = timedelta(hours=11, minutes=00, seconds=00)
hub1 = Package(0, "4001 South 700 East", "Salt Lake City", "UT", "84107", "EOD", "00", "None")
hub1.start = first_truck_departure
hub1.currTime = first_truck_departure
hub2 = Package(0, "4001 South 700 East", "Salt Lake City", "UT", "84107", "EOD", "00", "None")
hub2.start = second_truck_departure
hub2.currTime = second_truck_departure
hub3 = Package(0, "4001 South 700 East", "Salt Lake City", "UT", "84107", "EOD", "00", "None")
hub3.start = third_truck_departure
hub3.currTime = third_truck_departure
truck1 = read_data.getTruck(1)
truck2 = read_data.getTruck(2)
truck3 = read_data.getTruck(3)
for p in truck1.packages:
    tempP = p
    tempP.start = first_truck_departure
    packageHashTable.modify(p.id, tempP)
for p in truck2.packages:
    tempP = p
    tempP.start = second_truck_departure
    packageHashTable.modify(p.id, tempP)
for p in truck3.packages:
    tempP = p
    tempP.start = third_truck_departure
    packageHashTable.modify(p.id, tempP)
truck1.packages.insert(0, hub1)
truck2.packages.insert(0, hub2)
truck3.packages.insert(0, hub3)

#Grabs the distance between two addresses from the 2d distanceTable array, O(1) for direct index accessing
def distanceBetween(address1, address2):
    index1 = addressList.index([address1])
    index2 = addressList.index([address2])
    distance = distanceTable[index1][index2]
    #The table is bidirectional, so we can swap the indeces and get the right float
    if distance == '':
        distance = distanceTable[index2][index1]

    return float(distance)
#Gets the closest location from the current stop, O(n), where n is the number of packages remaining on the truck. 
def minDistance(currAddr, remainingPackages):
    if len(remainingPackages) == 0:
        return [0.0, None, 0]
    retDist = 50.0
    retPack = remainingPackages[0]
    retTime = 0
    for p in remainingPackages:
        tempDist = distanceBetween(currAddr.address, p.address)
        if tempDist <= retDist:
            retDist = tempDist
            retPack = p
            retTime = (retDist / 18) * 60 
    return [retDist, retPack, retTime]

#A recursive solution to deliver all packages. O(n^2) because it calls minDistance(which is O(n)), for n recursive calls. 
#This solution implements a greedy algorithm that determines the next stop by simply choosing the closest one (the one with minimum distance)
def truckDeliverPackages(packages, currAddr):
    remainingPackages = packages
    tempReplacePack = currAddr
    remainingPackages.remove(currAddr)
    
    minDistanceRet = minDistance(currAddr, remainingPackages)
    tempReplacePack.currTime = tempReplacePack.currTime + timedelta(minutes = minDistanceRet[2])
    tempReplacePack.status = "STATUS: Delivered at - " + str(tempReplacePack.currTime)
    
    packageHashTable.modify(currAddr.id, tempReplacePack)
   
    if len(remainingPackages) == 0:
        return minDistanceRet[0]
    
    nextStop = minDistanceRet[1]
    distanceToNext = minDistanceRet[0]
   
    for p in remainingPackages:
        p.currTime = p.start + timedelta(minutes=minDistanceRet[2])
        p.status = "STATUS: On truck at - " + currAddr.address + " At time - " + str(p.currTime)
        packageHashTable.modify(p.id, p)
        
    return distanceToNext + truckDeliverPackages(remainingPackages, nextStop)




