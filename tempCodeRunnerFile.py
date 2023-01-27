firstnum = float(input("FIRST NUM: "))
act = int(input ("NUMBER OF ACTIONS: "))
if (act > 0):
    i = 0
    for i in range(act):
        secondnum = float(input("SECOND NUM: "))
        print ("ACTIONS: ADDITION - 1, SUBTRACTION - 2, DIVISION - 3, Multi - 4")
        act = input("CHOOSE ACTION: ")
        if (act == "1" or act == "2" or act == "3" or act == "4"):
            if (act == "1"):
                firstnum +=secondnum
                print (f"VALUE: {firstnum}")
            if (act == "2"):
                firstnum = firstnum-secondnum
                print (f"VALUE: {firstnum}")
            if (act == "3"):
                if (secondnum == 0):
                    print("DIVISION ON ZERO")
                else:
                    firstnum = firstnum/secondnum
                    print (f"VALUE: {firstnum}")
            if (act == "4"):
                firstnum = firstnum*secondnum
                print (f"VALUE: {firstnum}")
        else: 
            print("ERROR, WRITE CORRECT ACTION")
print (f"FINAL VALUE: {firstnum}")
