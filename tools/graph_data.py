import matplotlib.pyplot as plt
import csv

def main():
    filename = "Sim_Turbulence2.csv"
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
        else:
            dx_Acc.append(GyrsX[i] - GyrsX[i - 1]/ times[i] - times[i - 1])
    for i in range(len(GyrsX)):
        if i == 0:
            sdx_Acc.append(dx_Acc[i]/ times[i])
        else:
            sdx_Acc.append(dx_Acc[i] - dx_Acc[i - 1]/ times[i] - times[i - 1])

    print(dx_Acc)



    plt.gca().set_aspect('equal')
    f = plt.figure(1)
    plt.plot(times, AccsX)
    plt.plot(times, AccsY)
    plt.plot(times, AccsZ)

    f2 = plt.figure(2)
    plt.plot(times, GyrsX, label="Angular Velcity Around X")
    plt.plot(times, GyrsY, label="Angular Velcity Around Y")
    plt.plot(times, GyrsZ, label="Angular Velcity Around Z")
    plt.plot(times, dx_Acc, label="Rate of Change of Velocity Around X")
    plt.plot(times, sdx_Acc, label="Second Rate of Change of Velocity Around X")


    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()


