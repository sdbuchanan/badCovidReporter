#!/usr/bin/python3
import pandas
import csv
import datetime

DESIRED_ROWS = {0,7,11,20,24}
now = datetime.datetime.now()

with open('states.csv') as input_file:
	reader = csv.reader(input_file)

	desired_rows = [row for row_number, row in enumerate(reader) if row_number in DESIRED_ROWS]

df = pandas.DataFrame(desired_rows)

#print("  .oooooo.     .oooooo.   oooooo     oooo ooooo oooooooooo.             .o   .ooooo.   ")
#print(" d8P'  `Y8b   d8P'  `Y8b   `888.     .8'  `888' `888'   `Y8b          o888  888' `Y88. ")
#print("888          888      888   `888.   .8'    888   888      888          888  888    888 ")
#print("888          888      888    `888. .8'     888   888      888          888   `Vbood888 ")
#print("888          888      888     `888.8'      888   888      888 8888888  888        888' ")
#print("`88b    ooo  `88b    d88'      `888'       888   888     d88'          888      .88P'  ")
#print(" `Y8bood8P'   `Y8bood8P'        `8'       o888o o888bood8P'           o888o   .oP'     ") 


print('----------------------------------')
print(df)
print('----------------------------------')
print('Last updated:')
print(now.strftime("%H:%M:%S %m-%d-%Y"))