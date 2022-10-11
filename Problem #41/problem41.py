#taking inputs
flights = input("Enter list of flights: ")
start = input("Enter Starting Airport: ")

#refining inputs
flights = flights.split()

#creatin variables
pair = []
flight = []
buff = []
itenary = []
itenary.append(start)

#filling variables + refining
for i in flights:
    for j in i:
        if j.isalpha():
            pair.append(j)
        
        if len(pair) == 2:
            flight.append(pair)
            pair = []

#algorithm
while len(flight) != 0:
    #taking all possible routes
    for i in flight:
        if i[0] == start:
            buff.append(i)

    #processing routes
    if len(buff) == 0:
        break
    elif len(buff) > 1:
        it = buff[0]
        
        #comparing destinations lexically
        for i in buff:
            if ord(i[1]) < ord(it[1]):
                it = i

        #updating itenary
        itenary.append(it[1])
    elif len(buff) == 1:
        it = buff[0]
        
        #updating itenary
        itenary.append(it[1])
    
    #initializing for next iteration
    buff = []
    flight.remove(it)
    start = it[1]
    it = []

#Generating output
if len(itenary) == 1:
    print('Null')
else:
    print(itenary)
