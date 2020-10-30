import os
import errno
import sys
import argparse
import logging
import datetime
import math
import numpy as np
import pandas as pd
 
# Creates a payoff matrix of size arg_a x arg_b filled with random integer between arg_min - arg_max
def createPayoffMatrix(arg_a, arg_b, arg_min, arg_max):
  rng = np.random.default_rng()
  df = pd.DataFrame(rng.integers(arg_min, arg_max, size=(arg_b, arg_a)))
  return df

# Returns the max value of the column with index col of dataframe df 
def getMaxOfCol(df, col):
  return df.iloc[:, [col]].max().values.item()

# Returns the max value of the row with index row of dataframe df 
def getMaxOfRow(df, row):
  return df.iloc[[row]].max(axis = 1).values.item()

# Returns a bool whether the given payoff matrix dataframes at index col, row form a nash equilibrium
# "..if the first payoff number, in the payoff pair of the cell, is the maximum of the 
# column of the cell and if the second number is the maximum of the row of the cell - then 
# the cell represents a Nash equilibrium.." - (https://en.wikipedia.org/wiki/Nash_equilibrium#Nash_equilibria_in_a_payoff_matrix)
def isNashEqilibrium(df_a, df_b, col, row):
  if(df_b[col][row]==getMaxOfCol(df_b, col) and df_a[col][row]==getMaxOfRow(df_a, row)):
    return True
  return False

dir_path = os.path.dirname(os.path.realpath(__file__))


# Start of main
# Handling of arguments
arg_run = 100
arg_a = 5
arg_b = 5
arg_min = 0
arg_max = 100
parser = argparse.ArgumentParser()
parser.add_argument("--run", type=int, help="Number of runs")
parser.add_argument("--a", type=int, help="Number of stratey choice for A")
parser.add_argument("--b", type=int, help="Number of stratey choice for B")
parser.add_argument("--min", type=int, help="Payoff matrix minimum values")
parser.add_argument("--max", type=int, help="Payoff matrix maximum values")
args = parser.parse_args()

# Setting up logger
currentDT = datetime.datetime.now()
logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='%d.%m.%Y %H:%M:%S', handlers=[logging.FileHandler(dir_path + "/" + currentDT.strftime("%Y%m%d%H%M%S") + "-NashEquilibrium.log"), logging.StreamHandler()])

# Overwriting parameters
if args.run:
  arg_run = args.run
if args.a:
  arg_a = args.a
if args.b:
  arg_b = args.b
if args.min:
  arg_min = args.min
if args.max:
  arg_max = args.max

# Result Counter  
noNashEq = 0
oneNashEq = 0
moreNashEq = 0

# Number of runs
for i in range(arg_run):
  logging.info('NashEquilibrium Run ' + str(i))
  # Create random payoff matrix
  df_a = createPayoffMatrix(arg_a, arg_b, arg_min, arg_max)
  df_b = createPayoffMatrix(arg_a, arg_b, arg_min, arg_max)

  # Find Nash Equilibriums
  nashCount = 0
  d = []
  # rows
  for x in range(arg_a):
    l = []
    # cols
    for y in range(arg_b):
      df_val = str(df_a[x][y]) + "|" + str(df_b[x][y])
      l.append((df_val))
      if(isNashEqilibrium(df_a, df_b, x, y)):
        nashCount += 1
        logging.info("NashEquilibrium at [" + str(x) + "][" + str(y) + "] - " + df_val)
    d.append(tuple(l))
  df_ab = pd.DataFrame(d)
  logging.info(df_ab.to_string())

  if nashCount == 0:
    noNashEq += 1
  elif nashCount == 1:
    oneNashEq += 1
  elif nashCount > 1:
    moreNashEq += 1

# Store Results
logging.info('Number of runs ' + str(arg_run))  
logging.info('No NashEquilibrium ' + str(noNashEq))
logging.info('One NashEquilibrium ' + str(oneNashEq))
logging.info('More than one NashEquilibrium ' + str(moreNashEq))

