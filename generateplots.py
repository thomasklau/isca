'''
This file generates the plots for a given data file.

Data Format:
Graph title
X-Axis label
Y-Axis label
    [Y Trial Data]
    [Y Trial Std]
    Y Trial Label
    (x numTrials)
'''

import numpy as np
from numpy.random import beta
import matplotlib.pyplot as plt
import sys

plt.style.use('ggplot')

# constant time data
time = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121]
timen = np.asarray(time)

if len(sys.argv) == 0:
    print 'Error: No file specified!'
    exit()

fp = open(sys.argv[1])
lines = fp.readlines()

title = lines[0]
xaxis = lines[1]
yaxis = lines[2]

plt.title(title) # subplot 211 title
plt.xlabel(xaxis)
plt.ylabel(yaxis)

if len(lines) % 3 != 0:
    print 'Error: Malformed Data input file. Please refer to the template!'
    exit()
    
lineCounter = 3;
while 'true':
    if lineCounter == len(lines):
        break
    data = lines[lineCounter].split()
    data = map(float, data)
    stddata = lines[lineCounter+1].split()
    stddata = map(float,stddata)
    triallabel = lines[lineCounter+2]
    lineCounter += 3
    
    plt.errorbar(timen, data, yerr=.005, label=triallabel)

fig = plt.figure(1)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.xlim(0, 130)
plt.ylim(.95, 1.25)

plt.show()
