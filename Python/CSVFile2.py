file = open("Addressbook.csv", "r")
line = file.readline()
SearchValue = input("Do you want to search by Name/Address/City/Phone Number?: ")
ScoreFound = 0

if SearchValue == "Name":
    SearchName = str(input("Enter Name: "))
    while (line):
        data =line.split(",")
        if data[0] == SearchName:
            print("Name: ",data[0])
            print("Address: ",data[1])
            print("City: ",data[2])
            print("Phone Number: ",data[3])
            ScoreFound = 1
        line=file.readline()
    if ScoreFound == 0:
        print("None Found")
elif SearchValue == "Address":
    SearchAddress = str(input("Enter Address: "))
    while(line):
        data =line.split(",")
        if data[1] == SearchAddress:
            print("Name: ",data[0])
            print("Address: ",data[1])
            print("City: ",data[2])
            print("Phone Number: ",data[3])
            ScoreFound = 1
        line=file.readline()
    if ScoreFound == 0:
        print("None Found")
        
elif SearchValue == "City":
    SearchCity = str(input("Enter City: "))
    while(line):
        data =line.split(",")
        if data[2] == SearchCity:
            print("Name: ",data[0])
            print("Address: ",data[1])
            print("City: ",data[2])
            print("Phone Number: ",data[3])
            ScoreFound = 1
        line=file.readline()
    if ScoreFound == 0:
        print("None Found")


elif SearchValue == "Phone Number":
    SearchPhone = input("Enter Phone Number: ")
    while(line):
        data =line.split(",")
        if data[3] == SearchPhone:
            print("Name: ",data[0])
            print("Address: ",data[1])
            print("City: ",data[2])
            print("Phone Number: ",data[3])
            ScoreFound = 1
        line=file.readline()
    if ScoreFound ==0:
        print("None Found")

else:
    print("Not a correct value")
