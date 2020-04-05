#!/bin/bash
wget -O - -q coronavirusapi.com/states.csv > ~/badCovidReporter/states.csv
python3 ~/badCovidReporter/report.py > ~/badCovidReporter//output.out
mail -s "Some Covid Stats" email@email.com < ~/badCovidReporter/output.out
