#!/usr/bin/env python3
""" Choquet integral example in NonAdditiveProbability

Created: Wed Jul 30, 2025, 12:16 PM EST
Author: Tobias Thrien
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, FixedLocator, FixedFormatter

a = 0
b = 1
margin = 0.05 * (b - a)
s_min, s_max = a - margin, b + margin


def fcap(s):
    s = np.array(s)
    return np.where(s > b, 0,
            np.where(s <= 1/2*(a+b), 1,
                1/2*(b-a)/(s-a)))

S = np.linspace(s_min, s_max, endpoint=True, num=300)
F = fcap(S)

fig, ax = plt.subplots()

# TODO mark discontinuity by splitting array above b
ax.plot(S, F, linewidth=3)

ax.set_xlabel("$s$")
ax.xaxis.set_minor_formatter(NullFormatter())
ax.xaxis.set_major_locator(FixedLocator([a, 1/2*(a+b), b]))
ax.xaxis.set_major_formatter(FixedFormatter(
    ["$a$", r"${}^1/_2(a+b)$", "$b$"]))
ax.set_xlim(s_min, s_max)

ax.set_ylabel("$\mathrm{fcap}_{\mathsf{o}}(A(s))$")
ax.set_ylim(bottom=0)
y_min, y_max = ax.get_ylim()

ax.spines[["top", "right"]].set_visible(False)
ax.plot(s_max, y_min, ">k", clip_on=False)
ax.plot(s_min, y_max, "^k", clip_on=False)
# This doesn't work for some reason
#ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
# The pointer on the y axis appears above a instead of s_min
#ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

plt.tight_layout()
fig.savefig("ChoquetPlot.png")
plt.close(fig)
