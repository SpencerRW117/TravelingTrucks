#Spencer Watkins 005887959
from datetime import datetime, timedelta
import distance_manager
import read_data

truck1 = read_data.getTruck(1)
truck2 = read_data.getTruck(2)
truck3 = read_data.getTruck(3)
packageHashTable = distance_manager.packageHashTable
truck1Dist = distance_manager.truckDeliverPackages(truck1.packages, distance_manager.hub1)
truck2Dist = distance_manager.truckDeliverPackages(truck2.packages, distance_manager.hub2)
truck3Dist = distance_manager.truckDeliverPackages(truck3.packages, distance_manager.hub3)
total = truck1Dist + truck2Dist + truck3Dist

#Print the header
print("#########################################")
print("C950 Package Routing Project")
print("Spencer Watkins, ID: 005887959")
print("#########################################")
print("TRUCK 1 DISTANCE: ", "%.2f" %truck1Dist)
print("TRUCK 2 DISTANCE: ", "%.2f" %truck2Dist)
print("TRUCK 3 DISTANCE: ", "%.2f" %truck3Dist)
print("TOTAL ROUTE DISTANCE: ", "%.2f" % total)

#Get the user choice
user_choice = input("""
Please select an option:
    1. Info for all packages at a selected time
    2. Info for a single package ID at a selected time
    0. Quit
""")
#The main loop for the program. 
while user_choice != 0:
    #Get time-based status of all records, O(n) for looping through the whole hash table
    if user_choice == '1':
        userTime = input("Enter a time in format (HH:MM:SS): \n")
        (hrs, mins, secs) = userTime.split(':')
        convertedUserTime = timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

        for x in range(1, 41):
            pack = packageHashTable.search(str(x))
            startTime = pack.start
        
            currTime = pack.currTime
        
            if startTime >= convertedUserTime:
                pack.status = "STATUS: At the hub, leaves at - "
                print(pack.id, pack.address, pack.city, pack.zip, pack.deliv_time, pack.size, pack.status, pack.start)
            elif startTime <= convertedUserTime:

                if convertedUserTime < currTime:
                    pack.status = "STATUS: En route, left hub at - "
                    print(pack.id, pack.address, pack.city, pack.zip, pack.deliv_time, pack.size, pack.status, pack.start)
                else:
                    pack.status = "STATUS: Delivered at - "
                    print(pack.id, pack.address, pack.city, pack.zip, pack.deliv_time, pack.size, pack.status, pack.currTime)
    #Get a single ID and return time-based information, O(1) accessing and modification                    
    elif user_choice == '2':
        chosenPack = input("Please enter a valid package ID (numbered between 1 - 40): \n")
        userTime = input("Enter a time in format (HH:MM:SS): \n")
        pack = packageHashTable.search(str(chosenPack))
        
        (hrs, mins, secs) = userTime.split(':')
        convertedUserTime = timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
        startTime = pack.start
        
        currTime = pack.currTime
    
        if startTime >= convertedUserTime:
            pack.status = "STATUS: At the hub, leaves at - "
            print(pack.id, pack.address, pack.city, pack.zip, pack.deliv_time, pack.size, pack.status, pack.start)
        
        elif startTime <= convertedUserTime:

            if convertedUserTime < currTime:
                pack.status = "STATUS: En route, left hub at - "
                print(pack.id, pack.address, pack.city, pack.zip, pack.deliv_time, pack.size, pack.status, pack.start)
            else:
                pack.status = "STATUS: Delivered at - "
                print(pack.id, pack.address, pack.city, pack.zip, pack.deliv_time, pack.size, pack.status, pack.currTime)
    #Exit the program
    elif user_choice == '0':
        exit()
    #Error check
    else:
        print("Invalid input")
        exit()

