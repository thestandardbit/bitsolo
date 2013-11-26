__author__ = 'jonathan'

import urllib2
import json
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.dates import date2num


url1 = 'http://www.quandl.com/api/v1/datasets/BITCOIN/BITSTAMPUSD.json?&sort_order=asc'

f = urllib2.urlopen(url1).read()
j = json.loads(f)

def get_elements(url, data):
    # find the list index of the input name

    f = urllib2.urlopen(url).read()

    jstr = json.loads(f)

    jstr_column_names = jstr.get('column_names')
    jstr_data = jstr.get('data')

    for index, item in enumerate(jstr_column_names):
        if item == data:
            #print str(index) + ' ' + item
            lst = []
            for e in jstr_data:
                lst.append(e[index])
            return lst

closes = get_elements(url1, 'Close')
dates = get_elements(url1, 'Date')

plt.close('all')
fig, ax = plt.subplots(1)
ax.plot(closes)
#plt.show()

for date in dates:
    print date

plt.plot(closes)
plt.show()