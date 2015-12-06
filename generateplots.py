'''
This file generates the plots for iscA1 + GCaMP6s, iscA2 + GCaMP6s, GCaMP6s
'''

import numpy as np
from numpy.random import beta
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# example data
time = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121]
timen = np.asarray(time)
isca1stirrer= [1, 1.10784159, 1.16046019, 1.21189766, 1.21382326, 1.21508274, 1.21436134, 1.17295416, 1.17333483, 1.1758013, 1.17708836, 1.17780704, 1.18029204]
isca1stirrern= np.asarray(isca1stirrer)

magnetite = [1, 1.03772408, 1.04632509, 1.11510793, 1.11970712, 1.11974094, 1.12132168, 1.12378636, 1.12325885, 1.12158663, 1.11960619, 1.12097975, 1.12028494]
magnetiten = np.asarray(magnetite)

isca125mt = [1, 1.02798305, 1.02628365, 1.02429018, 1.02233299, 1.02817278, 1.02582055, 1.0236002, 1.0225945, 1.02157973, 1.01900259, 1.01836676, 1.01579926]
isca125mtn = np.asarray(isca125mt)

isca15mt = [1, 1.03782482, 1.04201476, 1.04264287, 1.04435157, 1.04756605, 1.12004213, 1.05199454, 1.12239534, 1.1227841, 1.12419464, 1.19799139, 1.20159806]
isca15mtn = np.asarray(isca15mt)

isca10mt = [1, 1.00859029, 0.99969209, 0.99292463, 0.98907731, 0.98585464, 0.98202777, 0.97882958, 0.97639513, 0.97348178, 0.97084601, 0.9667248, 0.96381978]
isca10mtn = np.asarray(isca10mt)

gcamp6s = [1, 0.98366689, 0.98321808, 0.98445209, 0.9852469, 0.98600452, 0.9841695, 0.98632643, 0.98513609, 0.9763677, 0.97281497, 0.96687059, 0.96668399]
gcamp6sn = np.asarray(gcamp6s)

fig = plt.figure(1)
plt.errorbar(timen, isca1stirrern, yerr=.005, label='IscA1 + GCaMP6s - (Stirrer) 1mT')
plt.errorbar(timen, magnetiten, yerr=.005, label='IscA1 + GCaMP6s - (Magnetite) 1mT')
plt.errorbar(timen, isca125mtn, yerr=.005, label='IscA1 + GCaMP6s - 0.25mT')
plt.errorbar(timen, isca15mtn, yerr=.005, label='IscA1 + GCaMP6s - 0.5mT')
plt.errorbar(timen, isca10mtn, yerr=.005, label='IscA1 + GCaMP6s - 0mT')
plt.errorbar(timen, gcamp6sn, yerr=.005,label='GCaMP6s Only - 1mT')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.xlim(0, 130)
plt.ylim(.95, 1.25)

plt.xlabel('Time (seconds)')
plt.ylabel('Flurorescence Fold Change')
plt.title('Magnetic Response Fold-Change - IscA1 + GCaMP6s Sensor (Normalized Whole Frame Fluorescence)') # subplot 211 title

plt.show()
