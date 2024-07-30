#!/usr/bin/env python3



from sbp.client.drivers.pyserial_driver import PySerialDriver

from sbp.client import Handler, Framer

from sbp.navigation import MsgUtcTimeGnss, SBP_MSG_UTC_TIME_GNSS, SBP_MSG_BASELINE_NED, MsgBaselineNED, SBP_MSG_POS_LLH, MsgPosLLH

from sbp.imu import SBP_MSG_IMU_RAW, MsgImuRaw, SBP_MSG_IMU_AUX, MsgImuAux

from sbp.mag import SBP_MSG_MAG_RAW, MsgMagRaw

import argparse

import pdb;


import threading


import numpy as np
import csv
import time



# Set local variables

g_value = 9.81

imu_scale_flag = 0

imu_res = np.iinfo(np.int16).max

facc_scale = 0.00

gyr_scale = 0.00



def cb_SBP_MSG_UTC_TIME_GNSS(msg_utc, **source):

    msg = MsgUtcTimeGnss(msg_utc)

    print('utc time recieved')

    print(msg)



# Callback for LLH data

def cb_SBP_MSG_POS_LLH(msg_llh, **source):

    msg = MsgPosLLH(msg_llh)

    print('lat lon message recieved')

    print(msg)



# Callback for NED data

def cb_SBP_MSG_BASELINE_NED(msg_ned, **source):

    msg = MsgBaselineNED(msg_ned)

    print('ned message recieved')

    print(msg)



# Callback for IMU raw data

def cb_SBP_MSG_IMU_RAW(msg_imu_raw, **source):

    msg = MsgImuRaw(msg_imu_raw)

    print('imu message recieved')

    print(msg)

    

# Callback for IMU aux data

def cb_SBP_MSG_IMU_AUX(msg_imu_aux, **source):

    msg = MsgImuAux(msg_imu_aux)

    print('imu_aux message recieved')

    print(msg)



def main():

    parser = argparse.ArgumentParser()
    f = open("ROBOT_imu_databnf.csv", "w", newline="")
    fieldnames = ["Time", "AccX", "AccY", "AccZ", "GyrX", "GyrY", "GyrZ"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    parser.add_argument(

        "-p",

        "--port",

        default=['COM6'],

        nargs=1,

        help="specify the serial port to use.")

    args = parser.parse_args()



    # Open a connection to Piksi using the default baud rate (1Mbaud)
    start = time.time()
    with PySerialDriver(args.port[0], baud=115200) as driver:

        with Handler(Framer(driver.read, None, verbose=True)) as source:

            try:

                for msg, metadata in source.filter(SBP_MSG_IMU_RAW):

                    print(msg)
                    writer.writerow({"Time" : time.time() - start,
                                     "AccX": msg.acc_x,
                                     "AccY": msg.acc_y,
                                     "AccZ": msg.acc_z,
                                     "GyrX": msg.gyr_x,
                                     "GyrY": msg.gyr_y,
                                     "GyrZ": msg.gyr_z})


            except KeyboardInterrupt:

                pass





if __name__ == "__main__":

    main()