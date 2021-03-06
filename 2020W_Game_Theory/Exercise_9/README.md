# 2020W Game Theory Exercise 9

**Task**

Schreiben Sie ein Programm zur Bestimmung von Nash-Gleichgewichten für eine Auszahlungsmatrix mit 5 Zeilen und 5 Spalten. Füllen Sie die Matrix 100mal mit Zufallszahlen, und ermitteln Sie die relative Häufigkeit der Fälle, wo (a) kein NashGleichgewicht existiert, (b) genau ein Nash-Gleichgewicht existiert, (c) mehr als ein Nash-Gleichgewicht existiert.

**Implementation and Prerequisites**

The Exercise was implemented using python 3.7.4. At least this python version must be available and set up on the system. Furthermore, the python libraries `pandas` and `numpy` must be installed. (Easily done with `pip install pandas` and `pip install numpy` for example.)

It will generate a random payoff matrix and identify all Nash-Equilibriums. This is repeated a specific amount of times and the final results calcucalated - how often no Nash-Equilibrium was found, how often one Nash-Equilibrium was found, and how often more than one Nash-Equilibrium was found. The results are exported in log files with the naming *YYYYmmDDHHMMSS-NashEquilibrium.log*. All randomly created payoff matrix and their Nash Equilibriums are exported and the final counts at the bottom of the file.

**How to run**

The Script can be started over a command line with `python NashEquilibriumMatrix.py`.

Following optional parameter are possible:
**--run**: Number of runs, default is 100
**--a**: Number of strategy choices for A, default is 5
**--b**: Number of strategy choices for B, default is 5
**--min**: Payoff matrix minimum values, default is 0
**--max**: Payoff matrix maximum values, default is 100

This means `python NashEquilibriumMatrix.py --run 33 --a 10 --b 8 --min 5 --max 22` will create a 10x8 payoff matrix filled with values between 5 and 22 and runs 33 time.

**Result**

If run with the default values (5x5 matrix, 100 times, random values between 0 and 100), it seems that in around 25% of the cases no Nash-Equilibrium was found, in around 50% of the cases one Nash-Equilibrium was found, and in around 25% of the cases more than one Nash-Equilibrium was found.
