# badCovidReporter

A little thing I made to report daily stats to my team. It grabs each of our state's Tested, Positive, Deaths from [this site](coronavirusapi.com/states.csv) to Covid-19 and sends a mail to our mailbox.

I set up two cron jobs to run the shell script. The python just selects for the rows I want and prints out a pretty picture.
