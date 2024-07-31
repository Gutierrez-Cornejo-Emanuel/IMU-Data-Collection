import matplotlib.pyplot as plt
import csv

def main():
    filename = "Sim_Turbulence.csv"
    f = open(filename, "r", newline='')
    reader = csv.DictReader(f)

    times = []
    AccsY = []
    AccsZ = []
    AccsX = []
    GyrsX = []
    GyrsY = []
    GyrsZ = []
    dx_Acc = []
    dx_sums = []
    sdx_Acc = []
    for line in reader:
        times.append(float(line['Time']))
        AccsX.append(float(line['AccX']))
        AccsY.append(float(line['AccY']))
        AccsZ.append(float(line['AccZ']))
        GyrsX.append(float(line['GyrX']))
        GyrsY.append(float(line['GyrY']))
        GyrsZ.append(float(line['GyrZ']))

    for i in range(len(GyrsX)):
        if i == 0:
            dx_Acc.append(GyrsX[i]/ times[i])
            dx_sums.append(GyrsX[i] / times[i])
        else:
            dx_Acc.append((GyrsX[i] - GyrsX[i - 1])/ (times[i] - times[i - 1]))
            #dx_sums.append(sum(dx_Acc[max(0, i - 4):i + 1]))
            dx_sums.append(sum([abs(n) for n in GyrsX[max(0, i - 3):i + 1]]))
            

    """
    for i in range(len(GyrsX)):
        if i == 0:
            sdx_Acc.append(dx_Acc[i]/ times[i])
        else:
            sdx_Acc.append(dx_Acc[i] - dx_Acc[i - 1]/ times[i] - times[i - 1])
"""
    print(dx_Acc)



    plt.gca().set_aspect('equal')
    f = plt.figure(1)
    plt.xlabel("Time (s)")
    plt.ylabel("Acceleration (m/s^2)")
    plt.plot(times, AccsX)
    plt.plot(times, AccsY)
    plt.plot(times, AccsZ)

    f2 = plt.figure(2)
    plt.xlabel("Time (s)")
    plt.ylabel("Angular Velocity Around Axis (deg/s)")
    plt.plot(times, GyrsX, label="Angular Velcity Around X")
    plt.plot(times, GyrsY, label="Angular Velcity Around Y")
    #plt.plot(times, GyrsZ, label="Angular Velcity Around Z")
    #plt.plot(times, dx_Acc, label="Rate of Change of Velocity Around X")
    plt.plot(times, dx_sums, label="Velocity Sum from last 2 seconds (approx)")
    #plt.plot(times, sdx_Acc, label="Second Rate of Change of Velocity Around X")


    #Stability Metric

    for i in range(len(dx_sums)):
        if dx_sums[i] > 80:
            plt.plot(times[i],0,'ro')
        elif dx_sums[i] > 40:
            plt.plot(times[i],0,'yo')
        else:
            plt.plot(times[i],0,'go')
        



    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()


