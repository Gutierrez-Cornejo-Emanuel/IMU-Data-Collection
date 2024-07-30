#!/usr/bin/env python3

from sbp.client.drivers.pyserial_driver import PySerialDriver
from sbp.client import Handler, Framer
from sbp.navigation import SBP_MSG_BASELINE_NED, MsgBaselineNED, SBP_MSG_POS_LLH, MsgPosLLH
from sbp.imu import SBP_MSG_IMU_RAW, MsgImuRaw, SBP_MSG_IMU_AUX, MsgImuAux
from sbp.mag import SBP_MSG_MAG_RAW, MsgMagRaw
import argparse
import pdb;
import time

import threading

import numpy as np

# Set local variables
g_value = 9.81
imu_scale_flag = 0
imu_res = np.iinfo(np.int16).max
facc_scale = 0.00
gyr_scale = 0.00

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
    start = time.time()
    print(msg)
    
# Callback for IMU aux data
def cb_SBP_MSG_IMU_AUX(msg_imu_aux, **source):
    msg = MsgImuAux(msg_imu_aux)
    print('imu_aux message recieved')
    print(msg)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--port",
        default=['COM6'],
        nargs=1,
        help="specify the serial port to use.")
    args = parser.parse_args()

    driver = PySerialDriver(args.port[0])
    framer = Framer(driver.read, None, verbose=False)
    source = Handler(framer)
    start = time.time()
    source.add_callback(cb_SBP_MSG_POS_LLH,msg_type=SBP_MSG_POS_LLH)
    source.add_callback(cb_SBP_MSG_BASELINE_NED,msg_type=SBP_MSG_BASELINE_NED)
    source.add_callback(cb_SBP_MSG_IMU_RAW,msg_type=SBP_MSG_IMU_RAW)
    source.add_callback(cb_SBP_MSG_IMU_AUX,msg_type=SBP_MSG_IMU_AUX)
    source.start()
    try:
        while(True):
            continue
    except KeyboardInterrupt:
        pass
    source.stop()


if __name__ == "__main__":
    main()