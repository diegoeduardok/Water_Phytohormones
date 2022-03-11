import numpy as np
from matplotlib import cm

counts = np.loadtxt("count_mat.dat")
eq     = np.loadtxt("msm_eq_pop.dat")
dat1   = np.load   ("data_x.npy", allow_pickle=True)
dat2   = np.load   ("data_y.npy", allow_pickle=True)

xmax =  4
xmin = -2
ymax =  3
ymin = -3
bin_size = 200

i=0 
hists = np.zeros((bin_size, bin_size))
for i in range(len(eq)):
    hist  = np.histogram2d( dat1[i], dat2[i], bins=bin_size, range=[ [xmin, xmax], [ymin, ymax] ])[0]
    hists = hists + hist * eq[i] / len(dat1[i])
energy = -0.6*np.log(hists) - np.min(np.hstack(-0.6*np.log(hists)))
energy = np.transpose(energy)

import matplotlib.pyplot as plt
import math
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size': '12', 'weight':'bold'})
params = {'mathtext.default': 'regular' }
plt.rcParams.update(params)

from matplotlib.font_manager import FontProperties
fontP = FontProperties()
fontP.set_size('12')

ax0 = plt.subplot2grid((2,2),(0,0))

#c=ax0.imshow(energy, extent=[xmin, xmax, ymin, ymax], origin='lower', aspect='auto', cmap='jet', vmin=0, vmax=6, interpolation='nearest')

#xs  = np.linspace(xmin, xmax, bin_size)
#ys  = np.linspace(xmin, ymax, bin_size)
c=ax0.contourf(energy, np.linspace(0, 12, 49), origin='lower', extent=[xmin, xmax, ymin, ymax], cmap='jet')

ax0.set_xlim(-2, 4)
ax0.set_ylim(-3, 3)
ax0.set_xticks((-2, -1, 0, 1, 2, 3, 4))
ax0.set_yticks((-3, -2, -1, 0, 1, 2, 3))
ax0.set_xlabel(r'tIC 1 (a.u.)', fontweight="bold")
ax0.set_ylabel(r'tIC 2 (a.u.)', fontweight="bold")
cbar = plt.colorbar(c,ticks=[0,2,4,6,8,10,12])
cbar.ax.set_ylabel('Free energy (kcal/mol)', fontweight="bold")

"""
states = [75, 193, 33]
#[ 89, 165, 147,   1]
data   = np.loadtxt("avg_dist.txt")
tic1   = [ data[i][1] for i in states ]
tic2   = [ data[i][3] for i in states ]
ax0.scatter(tic1, tic2, marker='*', color='magenta', alpha=0.5, s=30, linewidths=0.5)

texts  = ['1', '2', '3']

for i, txt in enumerate(texts):
    ax0.annotate(txt, (tic1[i], tic2[i]))
"""

plt.tight_layout()
plt.savefig("tIC1-tIC2-landscape.png", dpi=300, bbox_inches='tight')
