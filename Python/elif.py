speed = int(input("Enter speed: "))
if speed >= 75:                         #Greater than or equal to 70
    print("Issue fine")
elif speed >= 70:
    print ("Warning")
else:                                   #if the speed does not fit into the specified parameters it prints no acton instead
    print ("No action")
    