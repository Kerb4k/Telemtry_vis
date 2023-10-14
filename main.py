
import cantools
import csv

def load_dbc_file(filepath):
    # Load the DBC file
    db = cantools.database.load_file(filepath)
    
    # For demonstration, print all the messages and their signals
    for message in db.messages:
        print(f"Message Name: {message.name}, ID: {message.frame_id}")
        for signal in message.signals:
            print(f"    Signal Name: {signal.name}")

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

def print_data(data, id):
    #print how many elements in the row
    
    for row in data:
        try:
            if row[2] == str(id):
                print(row)
        except: 
            pass
           
   

def get_column(data, column):
    column_list = []
    for row in data:
        column_list.append(row[column])
    return column_list

def main():
   # filename = input("Enter the filename: ")
    load_dbc_file("CAN0.dbc")
    #data = read_data(filename)
    #print_data(data, 1313)
    
main()
   