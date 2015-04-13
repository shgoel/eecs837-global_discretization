from random import randint
# function to get user input regardless of python version
def randomLERS(count):
    file = open("sample1.lers", "w")
    file.write("< a a a a x x d d a a x >\n[ height weight noise price ]\n! comment\n")
    for i in range(0,count):
        attributes = [randint(10,20)+float(randint(0,99))/100, randint(20,30)+float(randint(0,99))/100, randint(30, 40)+float(randint(0,99))/100]
        
        temp = randint(0, 4)
        if temp == 0:
            decision = "low"
        elif temp == 1:
            decision = "med"
        elif temp == 2:
            decision = "very_low"
        elif temp == 3:
            decision = "very_high"
        else:
            decision = "high"
        file.write(str(attributes[0]) + " " + str(attributes[1]) + " " + str(attributes[2]) + " " + decision + "\n")
    file.close()


def get_user_input(message):
    try:
        # python 2.x function
        user_input = raw_input(message)
    except:
        # python 3.x function
        user_input = input(message)
    return user_input


# function to get filename from user (if none specified) and then open a file
def openfile(path=""):
    if path == "":
        # Get filename from user
        user_input = get_user_input("Filename? ")
    else:
        user_input = path

    
    while True:
        try:
            # try to open file
            file = open(user_input, "r")
            break
        except:
            # if file doesn't open, re-prompt for filename and try to open again
            print("\nerror: File not found")
            user_input = get_user_input("Filename? ")
            
    return file

