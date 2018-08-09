example = int(input("Example number : "))
## Example ! Review of Tuples 

if example == 1 :
    # Tuples may have any type of elements
    # Strings , ints, floats , other tuples or other list

    tupA = (1, "apple", 6.00)
    tupB = (tupA, "MIT",[4,5])

    print("tupA is", tupA, "with length", len(tupA))
    print("tupB is", tupB, "with length", len(tupB))

    print("\nIndexing operations")
    print("tupA[0] is ",tupA[0])
    print("tupA[2] is ",tupA[2])
    #print("tupA[3] is ",tupA[3]) # Error Why?
    print("tupB[0] is ",tupB[0])
    print("tupB[0][1] is ",tupB[0][1])
    print("tupB[-1] is ",tupB[-1])

    print("\nSlicing operations")
    print("tupA[0:1] is ",tupA[0:1])
    print("tupA[0:100] is ",tupA[0:100])
    print("tupA[0:2] is ",tupA[0:2])
    print("tupA[:2] is ",tupA[:2])
    print("tupA[1:] is ",tupA[1:])
    print("tupA[:] is ",tupA[:])
    print("tupB[-1:-3] is ",tupB[-1:-3])

    # Iteration through tuple
    print("\nIteration through tupB")
    for item in tupB:
        print(item, "is of tyoe ", type(item))
    
    # this is equivalent to 
    print("\nIteration through tupB")
    for i in(range(len(tupB))):
        print(tupB[i], "is of type", type(tupB[i]))

if example == 2 :
    listA = [0.234, "apple", (1,2), 77]
    listB = [listA, "MIT", [1,2,3]]

    print("listA is", listA, "with length", len(listA))
    print("listB is", listB, "with length", len(listB))

    print("\nIndexing operations")
    print("listA[0] is ",listA[0])
    print("listA[3] is ",listA[3])
    #print("listA[4] is ",listA[4]) # Error Why?
    print("listB[0] is ",listB[0])
    print("listB[0][1] is ",listB[0][1] )
    print("listB[-1] is ",listB[-1])

    print("\nSlicing operations")
    print("listA[0:1] is ",listA[0:1])
    print("listA[0:100] is ",listA[0:100])
    print("listA[0:2] is ",listA[0:2])
    print("listA[:2] is ",listA[:2])
    print("listA[1:] is ",listA[1:])
    print("listA[:] is ",listA[:])
    print("listB[-1:-3] is ",listB[-1:-3])
   
    # Iteration through list
    print("\nIteration through listB")
    for item in listB:
        print(item, "is of tyoe ", type(item))

    # access inner list 
    print("\n Access inner list")
    L = [["MIT","HARVARD"],["Universities"],0]
    print("In list", L)
    print("L[0][1] is ", L[0][1]) #prints Harvard


    print("\n Matrix")
    #Create Matrix
    M = [[0,1], [1,2], [2,3], [3,4]]
    print(M)

# Example 3 List operations
if example == 3 :
    LA = [6.00, "MIT", 600, 600]
    LA.append("Harvard")
    print(LA)

    LA.append(["Yale","Standford"])
    print(LA)

    LA.pop() # pop off the last element
    print(LA)

    LA.pop(0) # pop off element at index 0
    print(LA)

    LA.extend(["Yale","Standford"])
    print(LA)

    LA.remove(600)
    print(LA)

    # lA.remove(500) #Error
    if 600 in LA:
        LA.remove(600)

 