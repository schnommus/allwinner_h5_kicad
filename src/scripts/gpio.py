#!/bin/python3

# Convert a slighty broken table of GPIO functions into pin names

import csv

with open('gpios.csv') as csvfile2:
    gpios_reader = csv.DictReader(csvfile2)
    cur_string = None
    last_gpio = None
    for row in gpios_reader:
        name = row["Pin Name"].strip()
        index = row["Function"].strip()
        function = row["Signal Name"].strip().replace('\n','')
        #print("{}, {}, {}".format(name, function, index))

        if index == "0":
            if last_gpio != None and cur_string != None:
                print("{},{}/{}".format(last_gpio, cur_string[:-1], last_gpio))
            cur_string = ""

        if name != '':
            last_gpio = name

        if function != 'Reserved' and \
           function != 'Input' and \
           function != 'Output' and \
           function != 'IO Disable' and \
           function != '':

            cur_string += function + '/'
