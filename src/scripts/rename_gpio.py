#!/bin/python3

# Map nicer GPIO names onto a cleaned-up file

import csv

with open('clean.csv') as csvfile1:
    clean_reader = csv.DictReader(csvfile1)
    for row in clean_reader:
        pin = row["Pin"]
        unit = row["Unit"]
        name = row["Name"]
        tp = row["Type"]
        style = row["Style"]
        with open('gpio_functions.csv') as csvfile2:
            gpio_reader = csv.DictReader(csvfile2)
            for gpio in gpio_reader:
                if gpio["Name"] == name and "GPIO" in unit:
                    name = gpio["Function"]
        print("{},{},{},{},{}".format(pin, unit, name, tp, style))

