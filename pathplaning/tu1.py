# -----------------------------------------------------------------------------
# Copyright (c) 2015, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
data = [(1,0),(0,1)]
fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[1, 1].hist2d(data[0], data[1])
plt.show()
print(data)

