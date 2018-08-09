lecture = int(input("Example number : "))
## Example ! Review of Tuples 

if lecture == 1 :
   # Shell vs editor 
   type(5)
   print(3.0-1)


   # Python vs Math(Which one is allowed in Python)
   #x+y = 2
   #x*x = 2
   #2 = x
   xy = 2


   # Bindings (What's printed?)
   
   usa_gold = 46
   uk_gold = 27 
   romania_gold = 1

   total_gold = usa_gold + uk_gold + romania_gold
   print(total_gold)

   romania_gold += 1
   print(total_gold)

if lecture == 2 :

    # Strings (What is the value of variable "u" from the code below?)

    once = "umbr"
    repeat = "ella"
    u = once +(repeat + " ")*4

    print(u)

    # Comparidsons

    pset_time = 15
    sleep_time = 8
    print(sleep_time > pset_time)

    drive = True
    drink = False
    both = drive and drink

    print(both)


    # Branchig 

    x = float(input("Enter for x : "))
    y = float(input("Enter for y : "))

    if x == y :
        if y != 0:
            print("x/y is ", x/y)
    elif x < y:
        print("x is smaller")
    else:
        print("y is smaller")

    # While loops ( what is printed when you type "Right"?)

    n = input("You're in the Lost Forest. Go left or right? ")

    while n == "right" or n == "left" :
        n = input("You're in the Lost Forest. Go left or right?")
    print("You got out of the Lost Forest!")