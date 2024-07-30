import csv

def main():

    #8gs / s^2
    MAX_RANGE_ACC = 8

    # 125 degrees/s
    MAX_RANGE_ANGULAR_VEL = 125

    NUM_RESOLUTION_TICS = 32768

    filename = "../ROBOT_imu_databnf.csv"
    f = open(filename, "r", newline='')
    reader = csv.DictReader(f)

    fieldnames = ["Time", "AccX", "AccY", "AccZ", "GyrX", "GyrY", "GyrZ"]
    g = 9.81
    wf = open("bnf.csv", "w", newline='')
    writer = csv.DictWriter(wf, fieldnames=fieldnames)
    writer.writeheader()
    for line in reader:
        new_line = {}
        new_line["Time"] = line["Time"]
        new_line["AccX"] = int(line["AccX"]) * MAX_RANGE_ACC / NUM_RESOLUTION_TICS * g
        new_line["AccY"] = int(line["AccY"]) * MAX_RANGE_ACC / NUM_RESOLUTION_TICS * g
        new_line["AccZ"] = int(line["AccZ"]) * MAX_RANGE_ACC / NUM_RESOLUTION_TICS * g
        new_line["GyrX"] = int(line["GyrX"]) * MAX_RANGE_ANGULAR_VEL / NUM_RESOLUTION_TICS
        new_line["GyrY"] = int(line["GyrY"]) * MAX_RANGE_ANGULAR_VEL / NUM_RESOLUTION_TICS
        new_line["GyrZ"] = int(line["GyrZ"]) * MAX_RANGE_ANGULAR_VEL / NUM_RESOLUTION_TICS
        writer.writerow(new_line)

    f.close()
    wf.close()

if __name__=="__main__": 
    main()