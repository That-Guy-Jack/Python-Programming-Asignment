#initalise default variable values
#Nodal Distance Meters
DND = 200
#Transmission Rate mbps
DTR = 5
#Packet Size Bits
DPB = 1000
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

#Put main code in one loop to allow sctipt to run multiple times
def main():
    while True:
        #Take user input or use defaults set above
        ND = int(input("Nodal Distance in Meters (200): ") or DND )
        S = int(input("Amount of stations (10): ") or DS )
        TR = int(input("Enter Transmission Rate in Mbps (5): ") or DTR )
        PB = int(input("Enter Packet Size in bits (1000): ") or DPB )
        PS = int(input("Enter Propergation Speed (200000000): ") or DPS )

        #Math Time
 
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


if __name__ == '__main__':
    main()