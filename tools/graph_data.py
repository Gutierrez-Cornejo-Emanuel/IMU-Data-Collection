import matplotlib.pyplot as plt
import csv

def main():
    filename = "outdoors_bump.csv"
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
    dy_sums = []
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
            dx_sums.append(GyrsX[i])
            dy_sums.append(GyrsY[i])
        else:
            dx_Acc.append((GyrsX[i] - GyrsX[i - 1])/ (times[i] - times[i - 1]))
            #dx_sums.append(sum(dx_Acc[max(0, i - 4):i + 1]))
            dx_sums.append(sum([abs(n) for n in GyrsX[max(0, i - 3):i + 1]]))
            dy_sums.append(sum([abs(n) for n in GyrsY[max(0, i - 3):i + 1]]))

            

    """
    for i in range(len(GyrsX)):
        if i == 0:
            sdx_Acc.append(dx_Acc[i]/ times[i])
        else:
            sdx_Acc.append(dx_Acc[i] - dx_Acc[i - 1]/ times[i] - times[i - 1])
"""
    print(dx_Acc)



    plt.gca().set_aspect('equal')
    plt.rcParams.update({'font.size': 22})
    f = plt.figure(1)
    plt.xlabel("Time (s)")
    plt.ylabel("Acceleration (m/s^2)")
    plt.plot(times, AccsX)
    plt.plot(times, AccsY)
    plt.plot(times, AccsZ)

    f2 = plt.figure(2)
    plt.ylim((-100, 100))
    plt.xlabel("Time (s)")
    plt.ylabel("Angular Velocity Around Axis (deg/s)")
    plt.plot(times, GyrsX, label="Angular velocity around X")
    plt.plot(times, GyrsY, label="Angular velocity around Y")
    #plt.plot(times, GyrsZ, label="Angular Velcity Around Z")
    #plt.plot(times, dx_Acc, label="Rate of Change of Velocity Around X")
    #plt.plot(times, dx_sums, label="Sum of absolute velocity around X Axis (Last 2 seconds)")
    #plt.plot(times, dy_sums, label="Sum of absolute velocity around Y Axis (Last 2 seconds)")

    #plt.plot(times, sdx_Acc, label="Second Rate of Change of Velocity Around X")

    #Legend (only one point gets a label)
    label_g = True
    label_r = True
    label_y = True

    #Stability Metric

    for i in range(len(dx_sums)):
        if dx_sums[i] > 80 or dy_sums[i] > 80:
            plt.plot(times[i],0,'ro', label=("Unstable" if label_r else None), markersize=5)
            label_r = False
        elif dx_sums[i] > 40 or dy_sums[i] > 40:
            plt.plot(times[i],0,'yo', label=("Caution" if label_y else None), markersize=5)
            label_y = False
        else:
            plt.plot(times[i],0,'go', label=("Stable" if label_g else None), markersize=5)
            label_g = False
        



    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()


