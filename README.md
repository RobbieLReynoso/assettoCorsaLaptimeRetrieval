# Assetto Corsa Laptime Data
This repository contains two Python scripts. The purpose of the main.py script is to read a .JSON file created by a server, extract necessary information from the .JSON file, and ultimately add it to an Excel spreadsheet for long-term tracking. The learnFTP.py automatically retrieve these .JSON files to be able to be read.

## Main Goal
The main goal for this project was to learn Python in a way that I would stick with. Sim-racing is a hobby of mine, so learning Python in a way that allowed me to apply my learnings to something I deeply enjoyed was important to me.

### Secondary Goals
One way to get better as a Sim-racer is to track your lap-times, and see small yet noticeable improvements over time. The data extracted also contained information about what car, track, and sector I was in at the time of the completion of a lap, which allowed to to create a database containing a bunch of metadata regarding lap-times, and extract information regarding how I could improve.

### Roadblocks
I was able to get pretty far with this project, but due to the circumstances of life, being a full-time student, etc, it never saw completion. The biggest issue I ran into was an apparent encoding issue. The server hosting the racing sessions seemed to encode the .JSON in a very strange way I, and many others were unable to figure out. However, a manual copy and paste would fix this issue, and because I had this as a simpler workaround, I never fixed the decoding issue 
