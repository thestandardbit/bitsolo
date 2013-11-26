__author__ = 'jonathan'

import numpy
import pandas
import Quandl
import matplotlib.pyplot as plt

assets = ['BITCOIN/BITSTAMPUSD/CLOSE',
          'BITCOIN/MTGOXUSD/CLOSE']

data = Quandl.get(assets)
data.head()

#fig = plt.figure()
#ax = data.add_subplot(2,1,1)
#ax.set_yscale('log')

data.plot()
plt.show()