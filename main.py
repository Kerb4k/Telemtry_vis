
import cantools
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import os
import platform
from merge_module import merge 
from merge_module import signal_message
# Your rest of the code...


def read_data( filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                data.append(row)
                line_count += 1
        
        return data


def load_dbc_file(filepath):
    # Load the DBC file
    db = cantools.database.load_file(filepath)
    
    signals = {}

    # For demonstration, print all the messages and their signals
    for message in db.messages:
        
        signals[message.frame_id] = {}
       
        for signal in message.signals:
            signals[message.frame_id][signal.name] = signal
        
    return signals

def print_data(data, signals, id, signal_name):
    #print how many elements in the row



    bit_start = signals[id][signal_name].start - 7
    bit_length = signals[id][signal_name].length
    factor = signals[id][signal_name].scale

    telemtry = []
    time_stamp = []

    for row in data:
        try:
            if row[2] == str(id):
                CAN_message = 0
              
                for i in range(int(row[4])):                    
                    CAN_message = merge(CAN_message, int(row[5+i], base= 16))
                #print(hex(CAN_message))
                telemtry.append(signal_message(CAN_message, bit_start, bit_length, int(row[4]), factor))
                time_stamp.append(datetime.strptime(row[14], '%Y-%m-%d %H:%M:%S'))
                
        except IndexError: 
            pass
    return telemtry, time_stamp
           
def plot(telemtry, time_stamp):
    plt.plot(time_stamp, telemtry)
    plt.xlabel('Time')
    plt.ylabel('Signal')
    plt.show()

def clear_terminal():
    system_name = platform.system() # Get the name of the operating system

    if system_name == "Windows":
        os.system('cls')  # Use 'cls' on Windows
    else:
        os.system('clear')  # Use 'clear' on Linux/macOS

def main():
    
    #filename = input("Enter the filename: ")
    filename = "logfile001.csv" 
    signals = load_dbc_file("CAN1.dbc")
    data = read_data(filename)
    telemtry, time_stamp = print_data(data, signals, 1684, 'Brake_Temperature_Front_Left')
    plot(telemtry, time_stamp)
    
def interface():
    
    while True:
        clear_terminal()
        print("1 - Load DBC file")
        print("2 - Load CSV file")
        print("3 - Plot data")
        print("4 - Exit")
        command = input("Enter the command: ") 

        dbc_file = ""
        csv_file = ""
        data = []
        signals = {}
        
        if command == "1":
            clear_terminal()
            dbc_file = input("Enter the DBC file path: ")
            signals = load_dbc_file(dbc_file)
        elif command == "2":
            clear_terminal()
            csv_file = input("Enter the CSV file path: ")
            data = read_data(csv_file)
        elif command == "3":
            clear_terminal()
            id = input("Enter the CAN ID: ")
            signal_name = input("Enter the signal name: ")
            telemtry, time_stamp = print_data(data, signals, int(id), signal_name)
            plot(telemtry, time_stamp)
            if input("Press esc to exit or enter to continue:"):
                pass
        elif command == "4":
            break



main()
   