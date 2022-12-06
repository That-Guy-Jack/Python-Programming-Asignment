import matplotlib.pyplot as plt
import numpy as npy
import time
ctime = time.strftime('%H-%M-%S')
date = time.strftime('%Y-%m-%d')
#initalise default variable values
#Nodal Distance Meters
DND = 200
#Transmission Rate mbps
DTR = 5
#Packet Size Bits
PB = 1000
#Propergation speed 2 x 108 m/s (speed of light through copper)
DPS = 200000000
#Default Stations 
DS = 10
#Utilisation 
U = 0
#Throughput
T = 0
# Calculated Transmission time
CTT = 0
#calculated Propergation delay
CPD = 0
#calculated bits per second
CBPS = 0
#calculated distance between end stations
CDBES = 0

# creating an empty list
PSL = []

#Create list for output data into matplotlib
MPLDX = []
MPLDY1 = []
MPLDY2 = []
#Take user input or use defaults set above
ND = int(input("Nodal Distance in Meters (200): ") or DND )

S = int(input("Amount of stations (10): ") or DS )

TR = int(input("Enter Transmission Rate in Mbps (5): ") or DTR )

PS = int(input("Enter Propergation Speed (200000000): ") or DPS )

try:
    PSL = []
    print("")
    print("Insert a non interger to start calculations!")
    print("")
    while True:
	    PSL.append(int(input("Enter Packet Size in bits: ")))

# if the input is not-integer, just print the list
except:
    print("List of packet sizes: ", str(PSL))
    print("")
    print("Entries in list " + str(len(PSL)))
    print("")

    
#loop for amount of entries in PSL
loop = len(PSL)
count = 0
while loop != 0:
    CL = PSL[count]
    PB = CL
    print("Current packet Size: " + str(PB))

    print("Calculating Distance between end stations: ")
    CDBES = ND * (S - 1)
    print("Calculated Distance between end stations: " + str(CDBES) + "Meters")

    print("Calculating propergation delay: ")
    CPD = CDBES/PS
    print("Calculated propergation delay: " + str(CPD) + " Seconds")

    print("Calculating transmission time: ")
    CTT = ( (PB + 8 + 14 + 4) / PB) / TR
    print("Calculated transmission time: " + str(CTT) + " Seconds")

    print("Calculating Utililisation: ")
    CU = CPD / CTT
    print("Calculated Utililisation: " + str(CU) + "%")

    print("Converting Transmission rate to Bits/s: ")
    CTR = TR * 1000000  
    print("Converted Transmission rate: " + str(CTR) + " Bits")

    print("Calculating Throughput: ")
    CBPS = CU * CTR
    print("Calculated Throughput: " + str(CBPS) + " Bits/s") 

    print("Converting Throughput to Megabits/s: ")
    T = CBPS/1000000
    print("Calculated Throughput: " + str(T) + " MBits/s") 
    MPLDY1.append(T)
    MPLDY2.append(CU)
    MPLDX.append(PB)
    print("")
    print("Loops Remaining: " + str(loop))
    print("")
    print("Throughput Y Data Generated so far: " + str(MPLDY1))
    print("")
    print("Utililisation Y Data Generated so far: " + str(MPLDY2))
    loop = loop -1
    count = count +1



# plot Packetsize (Bits) VS Throughput (Mbit/s)
fig, ax = plt.subplots()
ax.set_xlabel("Packet Size (Bits)")
ax.set_ylabel("Calculated Throughput (Mbit/s)")
ax.set_title("Packetsize (Bits) VS Throughput (Mbit/s)")
ax.plot(PSL,MPLDY1)
plt.savefig('exported-data/generated-Packetsize-vs-Throughput-at-' + ctime + "-on-" + date + '.png')


# plot Packetsize (Bits) VS Utililisation (Mbit/s)
fig, ax = plt.subplots()
ax.set_xlabel("Packet Size (Bits)")
ax.set_ylabel("Calculated Utililisation (%)")
ax.set_title("Packetsize (Bits) VS Utililisation (%)")
ax.plot(PSL,MPLDY2)
plt.savefig('exported-data/generated-Packetsize-vs-Utililisation-at-' + ctime + "-on-" + date + '.png')