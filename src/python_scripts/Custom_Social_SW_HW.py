import os
import time
import tkinter as tk
from tkinter import messagebox
from robodk.robolink import *
from robodk.robomath import *

# Define relative path to the .rdk file
relative_path = "src/roboDK/Assistive_UR5e.rdk"
absolute_path = os.path.abspath(relative_path)

# Start RoboDK with the project file
RDK = Robolink()
RDK.AddFile(absolute_path)

# Retrieve items from the RoboDK station
robot = RDK.Item("UR5e")
base = RDK.Item("UR5e Base")
tool = RDK.Item('Hand')
Init_target = RDK.Item('Init')
Hola1_target = RDK.Item("HOLA 1")
Hola2_target = RDK.Item("HOLA 2")
Posar_ma_target = RDK.Item("posar ma")
Acariciar1_target = RDK.Item("acariciar 1")
Acariciar2_target = RDK.Item("acariciar 2")

# Set robot frame, tool and speed
robot.setPoseFrame(base)
robot.setPoseTool(tool)
robot.setSpeed(50)

# Connect to real robot or simulate
def robot_online(online):
    if online:
        robot.setConnectionParams('192.168.1.5', 30000, '/', 'anonymous', '')
        time.sleep(5)
        success = robot.ConnectSafe('192.168.1.5')
        time.sleep(5)
        status, status_msg = robot.ConnectedState()
        if status != ROBOTCOM_READY:
            raise Exception("Failed to connect: " + status_msg)
        RDK.setRunMode(RUNMODE_RUN_ROBOT)
        print("Connection to UR5e Successful!")
    else:
        RDK.setRunMode(RUNMODE_SIMULATE)
        print("Simulation mode activated.")

# Robot movements
def move_to_init():
    print("Init")
    robot.MoveL(Init_target, True)
    print("Init_target REACHED")

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

def posar_ma():
    print("Posant la mà")
    robot.setSpeed(10)
    robot.MoveL(Posar_ma_target, True)
    print("Mà posada")
    time.sleep(4)

def acariciar():
    print("Acariciant")
    robot.setSpeed(5)
    for i in range(3):
        robot.MoveL(Acariciar1_target, True)
        robot.MoveL(Acariciar2_target, True)
    print("Acariciar FINISHED")

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
    robot_online(False)  # True for real robot, False for simulation
    move_to_init()
    hola()          
    posar_ma()
    acariciar()
    move_to_init()

# Run main and handle closing
if __name__ == "__main__":
    main()
    #confirm_close()
