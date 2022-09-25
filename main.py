# python3 converter.py
##Bradley Schaefer Sept 8/9
"""
needs to have exception handeling but shows concepts such as
basic function definitions
dictionaries
utilizing built in python functions
loops and minor exeption handeling
lots of logic and arithmetic usage
"""
##WIP HEX, OCT, BIANARY, DECIMAL Converter

"""
Prompt user to the type of input
1:Binary
2:Decimal
3.Octal
4:Hexadecimal
enter value:
Promp user for the type of output
print Output

create method to go up and down and return a normal number
1.binary to decimal
2.decimal to octal
3.octal to hex
4.hex to octal
5.octal to decimal
6.decimal to binary
"""

def Type_Of_Input():    #returns type of input that comes from the user
    print("Welcome to the Converter Program!!\n")
    for i in range (1,10,1):    #runs loop starting at 1 until 10 increasing by 1
        try:
            typeOfIn = int(input("Please choose what base your input it:\n1. Binary\n2. Octal\n3. Decimal\n4. Hexadecimal\n>"))
            if (typeOfIn >= 1 and typeOfIn <= 4):
                return typeOfIn
            else:
                print("Error! Retry!\n")
        except:
            print("Big Error Please Try Again!\n")
    print("You need to learn how to read")
    exit()  #exits the program if the user messes up more than 10 times
    
def Type_Of_Output():   #returns the type of output that comes from the user
    for i in range (1,10,1):
        try:
            typeOfOut = int(input("Please Enter disired Output:\n1. Binary\n2. Octal\n3. Decimal\n4. Hexadecimal\n>"))
            if (typeOfOut >= 1 and typeOfOut <= 4):
                return typeOfOut
            else:
                print("Error! Retry!\n")
        except:
            print("Big Error Please Try Again!\n")
    print("You need to learn how to read")
    exit()  #if attemped 10 times exits the program

def To_Decimal(input, base):    #changes any number into decimal number
    hex_to_num_dictionary = { #Easily Change between Hex and Decimal for arithhmetic
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15
    }

    arrayOfInput = (list(input))    #Change input to array
    arrayOfInput.reverse()  #To align correct index with digit

    output = 0
    for index in range(len(arrayOfInput)-1, -1, -1):
        arrayOfInput[index] = hex_to_num_dictionary.get(arrayOfInput[index], arrayOfInput[index])
        output += int(arrayOfInput[index]) * base ** index
        #print("Index = ", index, "Output += ", arrayOfInput[index], " * ", base, " ** ", index)    #TestCase

    return output

def From_Decimal(quotent, base):    #Changes decimal number into any number with different base
  
    num_to_hex_dictionary = {
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F'
    }
    remainer = []
    output = 0
    
    while quotent != 0:
        #print(int((((quotent / base) - (quotent // base)) * base)))    #TestCase
        remainer.insert(0, int((((quotent / base) - (quotent // base)) * base)) )
        quotent = quotent // base

    if (base == 16):
        index = 0
        for val in remainer:
            remainer[index] = num_to_hex_dictionary.get(val, val)
            #print(remainer[index]) #TestCase
            index += 1
    print("Output = ", end = "")
    
    for ele in remainer:    #string loop that turns the array into a string
        output += ele
    return output
        
##Main
base_dictionary = { #Hashmap to easily define base from input
    1:2,    #Binary
    2:8,    #Octal
    3:10,   #Decimal
    4:16    #Hexadecimal
}

typeOfIn = Type_Of_Input()   #Get typeOfI

typeOfOut = Type_Of_Output()

inputNum = input("Please Enter Number: ")

#print("typeOfIn = ", typeOfIn, "\ntypeOfOut = ", typeOfOut, "\ninputNum = ", inputNum)  #TestCase Now have typeOfIn, typeOfOut, and inputNum
outputNum = 0
if (typeOfIn == 3):    #Decimal to Anything
    outputNum = From_Decimal(int(inputNum), base_dictionary.get(typeOfOut))
elif (typeOfOut == 3):    #Anything to Decimal
    outputNum = To_Decimal(inputNum, base_dictionary.get(typeOfIn))
else:
    outputNum = From_Decimal(To_Decimal(inputNum, base_dictionary.get(typeOfIn)), base_dictionary.get(typeOfOut))

print(outputNum)
print("Program has exited!!!")