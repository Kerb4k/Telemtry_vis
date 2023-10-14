
import cantools
import csv
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



    bit_start = signals[id][signal_name].start
    bit_length = signals[id][signal_name].length
    factor = signals[id][signal_name].scale

    telemtry = []

    for row in data:
        try:
            if row[2] == str(id):
                CAN_message = 0
                
                for i in range(int(row[4])):                    
                    CAN_message = merge(CAN_message, int(row[5+i]))
                
                telemtry.append(signal_message(CAN_message, bit_start, bit_length, factor))
                
        except: 
            pass
    return telemtry
           
   

def get_column(data, column):
    column_list = []
    for row in data:
        column_list.append(row[column])
    return column_list

def main():
    
    #filename = input("Enter the filename: ")
    filename = "logfile001.csv" 
    signals = load_dbc_file("CAN0.dbc")
    data = read_data(filename)
    print(print_data(data, signals, 1314, 'IVT_Voltage1'))
    
main()
   