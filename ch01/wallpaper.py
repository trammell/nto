#!/usr/bin/python2.5

import sys
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams['font.size'] = 6

# Draw chart
fig = plt.figure()
plt.title(' '.join(sys.argv))
#plt.setp(plt.gca(), 'yticklabels', [])
#plt.setp(plt.gca(), 'xticklabels', [])
#ax = fig.add_subplot(111, axisbg=options.bgcolor)
#ax.scatter(xs, ys, s=sizes, c=colors, cmap=colormap, linewidths=0, 
#    alpha=options.alpha)
#
## Evaluate an expression at each n (and draw these points if necessary)
#if hasattr(options, 'expr'):
#    special_xs = []
#    special_ys = []
#    for i in range(n):
#            y = eval(options.expr, {'n': i})
#            if y < n:
#                special_xs.append(xs[y])
#                special_ys.append(ys[y])
#
#    ax.scatter(special_xs, special_ys, s=12.0, c='green', linewidths=0)
#
#ax.set_xlim(min(xs), max(xs))
#ax.set_ylim(min(ys), max(ys))
plt.savefig('wallpaper.png', dpi=100)
#
# Clean up and goodbye
plt.close(fig)
sys.exit()
