import os
import time
import socket
import tkinter as tk
from tkinter import messagebox
from math import radians, degrees, pi
import numpy as np
from robodk.robolink import *
from robodk.robomath import *

# Load RoboDK project from relative path
relative_path = "src/roboDK/Assistive_UR5e.rdk"  #demanar a Laia Raja sinó o en Marc
absolute_path = os.path.abspath(relative_path)  #hem de fer que coincideixi amb el path
RDK = Robolink()
RDK.AddFile(absolute_path)

# Robot setup
robot = RDK.Item("UR5e")
base = RDK.Item("UR5e Base")
tool = RDK.Item('Hand')
Init_target = RDK.Item('Init')
Hola1_target = RDK.Item("HOLA 1")
Hola2_target = RDK.Item("HOLA 2")
Posar_ma_target = RDK.Item("posar ma")
Acariciar1_target = RDK.Item("acariciar 1")
Acariciar2_target = RDK.Item("acariciar 2")


robot.setPoseFrame(base)
robot.setPoseTool(tool)
robot.setSpeed(20)

# Robot Constants
ROBOT_IP = '192.168.1.5'
ROBOT_PORT = 30002
accel_mss = 1.2
speed_ms = 0.75
blend_r = 0.0
timej = 6
timel = 4



# URScript commands
set_tcp = "set_tcp(p[0.000000, 0.000000, 0.050000, 0.000000, 0.000000, 0.000000])"

j1, j2, j3, j4, j5, j6 = list(np.radians(Init_target.Joints()))
movej_Init_target = f"movej([{j1},{j2}, {j3}, {j4}, {j5}, {j6}],{accel_mss},{speed_ms},{timej},{blend_r})"  #hem canviat el time1 perque no sabiem quin haviem de posar 

X, Y, Z, Roll, Pitch, Yaw = Pose_2_TxyzRxyz(Hola1_target.Pose())
movel_Hola1_target = f"movel(p[{X}, {Y}, {Z}, {Roll}, {Pitch}, {Yaw}], a={accel_mss}, v={speed_ms}, t={timel}, r={blend_r})"

X, Y, Z, Roll, Pitch, Yaw = Pose_2_TxyzRxyz(Hola2_target.Pose())
movel_Hola2_target = f"movel(p[{X}, {Y}, {Z}, {Roll}, {Pitch}, {Yaw}], a={accel_mss}, v={speed_ms}, t={timel}, r={blend_r})"

X, Y, Z, Roll, Pitch, Yaw = Pose_2_TxyzRxyz(Posar_ma_target.Pose())
movel_Posar_ma_target = f"movel(p[{X}, {Y}, {Z}, {Roll}, {Pitch}, {Yaw}], a={accel_mss}, v={speed_ms}, t={timel}, r={blend_r})"

X, Y, Z, Roll, Pitch, Yaw = Pose_2_TxyzRxyz(Acariciar1_target.Pose())
movel_Acariciar1_Target = f"movel(p[{X}, {Y}, {Z}, {Roll}, {Pitch}, {Yaw}], a={accel_mss}, v={speed_ms}, t={timel}, r={blend_r})"

X, Y, Z, Roll, Pitch, Yaw = Pose_2_TxyzRxyz(Acariciar2_target.Pose())
movel_Acariciar2_Target = f"movel(p[{X}, {Y}, {Z}, {Roll}, {Pitch}, {Yaw}], a={accel_mss}, v={speed_ms}, t={timel}, r={blend_r})"

# Check robot connection
def check_robot_port(ip, port):
    global robot_socket
    try:
        robot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        robot_socket.settimeout(1)
        robot_socket.connect((ip, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
# Send URScript command
def send_ur_script(command):
    robot_socket.send((command + "\n").encode())

def receive_response(t):
    robot

# Wait for robot response
    time.sleep(3)

# Movements
def Init():
    print("Init")
    robot.MoveL(Init_target, True)
    print("Init_target REACHED")
    if robot_is_connected:
        print("Init REAL UR5e")
        send_ur_script(set_tcp)
        receive_response(1)
        send_ur_script(movej_Init_target)
        receive_response(timej)
    else:
        print("UR5e not connected. Simulation only.")

def hola():
    print("Fent HOLA")
    robot.setSpeed(20)  
    robot.MoveL(Hola1_target, True)
    robot.setSpeed(5)  
    for i in range(2):
        robot.MoveL(Hola2_target, True)
        time.sleep(0.5)
        robot.MoveL(Hola1_target, True)
        time.sleep(0.5)
    robot.MoveL(Hola2_target, True)
    robot.setSpeed(20)  
    print("HOLA FINISHED")
    if robot_is_connected:
        print("Hola REAL UR5e")
        send_ur_script(set_tcp)
        receive_response(1)
        send_ur_script(movel_Hola1_target)
        receive_response(timel)
        send_ur_script(movel_Hola2_target)
        receive_response(timel)
        send_ur_script(movel_Hola1_target)
        receive_response(timel)
        send_ur_script(movel_Hola2_target)
        receive_response(timel)
        send_ur_script(movel_Hola1_target)
        receive_response(timel)
        send_ur_script(movel_Hola2_target)
        receive_response(timel)

def posar_ma():
    print("Posant la mà")
    robot.setSpeed(10)
    robot.MoveL(Posar_ma_target, True)
    print("Mà posada")
    time.sleep(4)
    if robot_is_connected:
        print("posar ma REAL UR5e")
        send_ur_script(set_tcp)
        receive_response(1)
        send_ur_script(movel_Posar_ma_target)
        receive_response(timel)

def acariciar():
    print("Acariciant")
    robot.setSpeed(5)
    for i in range(3):
        robot.MoveL(Acariciar1_target, True)
        robot.MoveL(Acariciar2_target, True)
    print("Acariciar FINISHED")
    if robot_is_connected:
        print("Acariciar REAL UR5e")
        send_ur_script(set_tcp)
        receive_response(1)
        send_ur_script(movel_Acariciar1_Target)
        receive_response(timel)
        send_ur_script(movel_Acariciar2_Target)
        receive_response(timel)
        send_ur_script(movel_Acariciar1_Target)
        receive_response(timel)
        send_ur_script(movel_Acariciar2_Target)
        receive_response(timel)
        send_ur_script(movel_Acariciar1_Target)
        receive_response(timel)
        send_ur_script(movel_Acariciar2_Target)
        receive_response(timel)

# Confirmation dialog to close RoboDK
def confirm_close():
    root = tk.Tk()
    root.withdraw()
    response = messagebox.askquestion(
        "Close RoboDK",
        "Do you want to save changes before closing RoboDK?",
        icon='question'
    )
    if response == 'yes':
        RDK.Save()
        RDK.CloseRoboDK()
        print("RoboDK saved and closed.")
    else:
        RDK.CloseRoboDK()
        print("RoboDK closed without saving.")

# Main function
def main():
    global robot_is_connected
    robot_is_connected = check_robot_port(ROBOT_IP, ROBOT_PORT)
    Init()
    hola()          
    posar_ma()
    acariciar()
    Init()
    if robot_is_connected:
        robot_socket.close()

# Run and close
if __name__ == "__main__":
    main()
    #confirm_close()
    
