import random

# class for storing (attribute, value) pairs and the (decision, concept) pair
class entry():
    def __init__(self, attributes, decision):
        self.A = {}
        for i in range(0,len(attributes)):
            self.A[i] = attributes[i]
        self.D = decision


# function to get user input regardless of python version
def get_user_input(message):
    try:
        # python 2.x function
        user_input = raw_input(message)
    except:
        # python 3.x function
        user_input = input(message)
    return user_input


# function to get filename from user and then open a file
def openfile():

    # Get filename from user
    user_input = get_user_input("Filename? ")
    while True:
        try:
            # try to open file
            file = open(user_input)
            break
        except:
            # if file doesn't open, re-prompt for filename and try to open again
            print("\nerror: File not found")
            user_input = get_user_input("Filename? ")
            
    return file


# function to partition a set based on concept
def partitionD(entries):
    Dpart = [[0]]
    concepts = [entries[0].D]
    
    # Build partition identifiers
    for i in range(0, len(entries)):
        if not(entries[i].D in concepts):
            Dpart.append([i])
            concepts.append(entries[i].D)
            print(entries[i].D + " (" + str(i) + ") not found")
            
    # Finish populating partition
    for i in range(0, len(entries)):
        for j in range(0, len(Dpart)):
            if not(i in Dpart[j]) and (entries[i].D == concepts[j]):
                Dpart[j].append(i)
        
    print(Dpart)
    return Dpart


# function to partition a set based on attribute 
def partitionAttribute(entries,Attribute):
    print("coming soon")


# function to check consistency between attribute and decision   
def isconsistant(entries):
    print("coming soon")


###################
# Begin execution #
###################
#file = openfile()

#Populate cases
entries = {}
for i in range(0,10):
    attributes = [random.randint(0, 10), random.randint(20,30), random.randint(40, 50)]
    
    temp = random.randint(0, 2)
    if temp == 0:
        decision = "low"
    elif temp == 1:
        decision = "med"
    else:
        decision = "high"
    entries[i] = entry(attributes, decision)

# display decision for each case
strng = ""
for i in range(0,len(entries)):
    strng += str(i) + ": " + entries[i].D + ",    "
print(strng)


# Partition based on decision
Dpart = partitionD(entries)