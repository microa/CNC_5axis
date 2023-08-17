# -*- coding: utf-8 -*-
import serial # Import UART Module
import time
import ast


def crc16(data: str, poly: hex = 0xA001) -> str:
    '''
        CRC-16 MODBUS HASHING ALGORITHM
    '''
    crc = 0xFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            crc = ((crc >> 1) ^ poly
                   if (crc & 0x0001)
                   else crc >> 1)

    hv = hex(crc).upper()[2:]
    blueprint = '0000'
    return (blueprint if len(hv) == 0 else blueprint[:-len(hv)] + hv)

def makeBytes(DID,FID,RIDH,RIDL,RVH,RVL):
    a = DID
    b = FID
    c = RIDH
    d = RIDL
    e = RVH
    f = RVL

    return bytes([a,b,c,d,e,f])

def CRC(DeviceID,FunctionID,RegIDH,RegIDL,RegValH,RegValL):
    CMDBytes = makeBytes(DeviceID,FunctionID,RegIDH,RegIDL,RegValH,RegValL)
    CRCResult = crc16(CMDBytes)

    print("CRC:",CRCResult)

    ts = int(CRCResult,16)
    L = ts & 0x00FF  # Low 8bit
    H = (ts & 0xFF00) >>8
    print (L)
    print (H)

    STR = bytearray(CMDBytes)

    STR.append(L)
    STR.append(H)

    return STR


def hexstrConvert(hexstr0, hexstr1):
    transRCV_H = int(hexstr0)
    transRCV_L = int(hexstr1)

    transRCV = transRCV_H * 256 + transRCV_L
    return transRCV

def readModbus(ser, DeviceID, FunctionID, RegIDH, RegIDL, RegValH, RegValL):
    data = CRC(DeviceID, FunctionID, RegIDH, RegIDL, RegValH, RegValL)

    result = ser.write(data)  # Write Data
    print("Sent: %d bytes,detail: %s" % (result, data))

    # Receive message
    temp = bytes([])

    while True:
        if ser.in_waiting:
            RCV = ser.read(ser.in_waiting)
            #print (RCV)
            probe = crc16(bytes(RCV))
            if (probe == "0000"):  # Exit Mark
                print("Received:%d bytes: %s" % (len(RCV), RCV))
                break
            elif(temp != RCV):
                RCV = temp+ RCV
                temp = RCV
                print ("Reconstruction RCV Result: ", RCV)
                probe = crc16(bytes(RCV))
                if (probe == "0000"):  # Exit Mark
                    print("Received:%d bytes: %s" % (len(RCV), RCV))
                    break


    '''
    while True:
        recv = ser.readline()

        if recv == ''.encode():
            break;
        else:
            RCV = recv
            print("Received: %d bytes,detail: %s" % (len(recv), recv))
    '''
    return RCV


def readData(COMx, DeviceID, FunctionID, RegIDH, RegIDL, RegValH, RegValL):
    ser = serial.Serial(COMx, 9600, timeout=1)

    readModbus(ser, DeviceID, FunctionID, RegIDH, RegIDL, RegValH, RegValL)

    print(ser)

    #time.sleep(0.01)

    ser.close()  # Turn off UART

def Move_Certain_Distance(COMx, axis, distance_mm):

    distance_mm_High8bit = (distance_mm >> 8) & 0xFF  # High 8 bits
    distance_mm_Low8bit = distance_mm & 0xFF  # Low 8 bits

    print(distance_mm_High8bit,distance_mm_Low8bit)

    if axis == "x":
        # write x axis distance-register of relative distance from setted origin:
        readData(COMx, 0x01, 0x06, 0x01, 0x2C, distance_mm_High8bit, distance_mm_Low8bit)
        print("X-axis register write completed.")
        # enable x axis, start moving according to distance-register:
        readData(COMx, 0x01, 0x05, 0x00, 0x01, 0xFF, 0x00)
        print("X-axis start moving...")

    if axis == "y":
        readData(COMx, 0x01, 0x06, 0x01, 0x30, distance_mm_High8bit, distance_mm_Low8bit)
        print("Y-axis register write completed.")
        readData(COMx, 0x01, 0x05, 0x00, 0x02, 0xFF, 0x00)
        print("Y-axis start moving...")

    if axis == "z":
        readData(COMx, 0x01, 0x06, 0x01, 0x32, distance_mm_High8bit, distance_mm_Low8bit)
        print("Z-axis register write completed.")
        readData(COMx, 0x01, 0x05, 0x00, 0x04, 0xFF, 0x00)
        print("Z-axis start moving...")

    if axis == "a":
        readData(COMx, 0x01, 0x06, 0x01, 0x34, distance_mm_High8bit, distance_mm_Low8bit)
        print("A-axis register write completed.")
        readData(COMx, 0x01, 0x05, 0x00, 0x06, 0xFF, 0x00)
        print("A-axis start moving...")

    if axis == "b":
        readData(COMx, 0x01, 0x06, 0x01, 0x36, distance_mm_High8bit, distance_mm_Low8bit)
        print("B-axis register write completed.")
        readData(COMx, 0x01, 0x05, 0x00, 0x08, 0xFF, 0x00)
        print("B-axis start moving...")

def Moving(COMx, axis, Direction, time_s):

    Forward     =   [0x0B, 0x0D, 0x0F, 0x11, 0x13]
    Backward    =   [0x0C, 0x0E, 0x10, 0x12, 0x14]

    axis_num = 0

    if axis == "x":
        axis_num = 0
    if axis == "y":
        axis_num = 1
    if axis == "z":
        axis_num = 2
    if axis == "a":
        axis_num = 3
    if axis == "b":
        axis_num = 4

    if Direction == "forward":
        readData(COMx, 0x01, 0x05, 0x00, Forward[axis_num], 0xFF, 0x00)     #m-axis forward move
        time.sleep(time_s)
        readData(0x01, 0x05, 0x00, 0x0B, 0x17, 0x70)    # x-axis stop

    if Direction == "backward":
        readData(COMx, 0x01, 0x05, 0x00, Backward[axis_num], 0xFF, 0x00)     #m-axis forward move
        time.sleep(time_s)
        readData(0x01, 0x05, 0x00, 0x0B, 0x17, 0x70)    # x-axis stop

def Speed(COMx, axises):

    if axises == "xyz":
        xyz_speed = int(input("x,y,z speed setting(input one number):"))
        xyz_speed_High8bit = (xyz_speed >> 8) & 0xFF  # High 8 bits
        xyz_speed_Low8bit = xyz_speed & 0xFF  # Low 8 bits
        readData(COMx, 0x01, 0x06, 0x01, 0x90, xyz_speed_High8bit, xyz_speed_Low8bit)

    if axises == "ab":
        ab_speed = int(input("a,b speed setting(input one number):"))
        ab_speed_High8bit = (ab_speed >> 8) & 0xFF  # High 8 bits
        ab_speed_Low8bit = ab_speed & 0xFF  # Low 8 bits
        readData(COMx, 0x01, 0x06, 0x01, 0x90, ab_speed_High8bit, ab_speed_Low8bit)


def main():



    Move_Certain_Distance("COM48", "x", 20)
    Moving("COM48", "x", "forward", 2)
    Speed("COM48", "xyz")

    
    print("Press ENTER...")
    input()

if __name__ == '__main__':
    main()
