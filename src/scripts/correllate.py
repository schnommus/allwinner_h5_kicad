#!/bin/python3

# Correllate pin types from a different part of the datasheet against the pin names

import csv

with open('allwinner_h5_toconvert1.csv') as csvfile2:
    pins_reader = csv.DictReader(csvfile2)
    for pin_row in pins_reader:
        pin_type = "unspecified"
        pin_style = ""
        with open('functions.csv') as csvfile1:
            functions_reader = csv.DictReader(csvfile1)
            for function_row in functions_reader:
                pin_clean1 = ''.join(c for c in pin_row['Name'] if c.isalpha())
                pin_clean2 = pin_row['Name'].strip()
                row_clean = function_row['Name'].split('[')[0]
                row_clean2 = function_row['Name'].strip()
                #print("!! {}, {}".format(pin_clean, row_clean))
                if pin_clean1 == row_clean or \
                   pin_clean2 == row_clean2:
                    t = function_row['Type'].strip()
                    if t == 'I/O':
                        pin_type = 'bidirectional'
                    elif t == 'O':
                        pin_type = 'output'
                    elif t == 'I':
                        pin_type = 'input'
                    elif t == 'A I/O':
                        pin_type = 'bidirectional'
                        pin_style = 'analog'
                    elif t == 'AI':
                        pin_type = 'input'
                        pin_style = 'analog'
                    elif t == 'AO':
                        pin_type = 'output'
                        pin_style = 'analog'
                    elif t == 'AOD':
                        pin_type = 'open_collector'
                        pin_style = 'analog'
                    elif t == 'P':
                        pin_type = 'power_in'
                    elif t == 'G':
                        pin_type = 'gnd'

            if pin_type == "unspecified":
                if 'GPIO' in pin_row['Unit']:
                    pin_type = 'bidirectional'
                if 'VCC' in pin_row['Name'] or 'VDD' in pin_row['Name']:
                    pin_type = 'power_in'
                if 'GND' in pin_row['Name']:
                    pin_type = 'gnd'
                    #print(pin_row['Name'] + " " + function_row['Name'] + " " + pin_type)
            print("{},{},{},{},{}".format(pin_row['Pin'], pin_row['Unit'], pin_row['Name'], \
                  pin_type, pin_style))

