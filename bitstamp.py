__author__ = 'jonathan'

import urllib2
import json

url1 = 'http://www.quandl.com/api/v1/datasets/BITCOIN/BITSTAMPUSD.json?&sort_order=desc'
url2 = 'http://www.quandl.com/api/v1/datasets/BITCOIN/MTGOXUSD.json?&sort_order=desc'

'http://www.quandl.com/api/v1/datasets/BITCOIN/BITSTAMPUSD.json?&trim_start=2011-09-13&trim_end=2013-11-21&sort_order=desc'



def get_elements(url, data):
    # find the list index of the input name

    f = urllib2.urlopen(url).read()

    jstr = json.loads(f)

    jstr_column_names = jstr.get('column_names')
    jstr_data = jstr.get('data')

    for c in jstr_column_names:
        print c

    for e in jstr_data:
        print e

    for index, item in enumerate(jstr_column_names):
        if item == data:
            #print str(index) + ' ' + item
            lst = []
            for e in jstr_data:
                lst.append(e[index])
            return lst

def intersect(a, b):
    return list(set(a) & set(b))

dates = sorted(intersect(get_elements(url1, 'Date'), get_elements(url2, 'Date')))

start_date = dates[0]
end_date = dates[len(dates)-1]
print '%s to %s' % (start_date, end_date)

bitstamp = 'http://www.quandl.com/api/v1/datasets/BITCOIN/BITSTAMPUSD.json?&trim_start=%s&trim_end=%s&sort_order=desc' % (start_date, end_date)
gox = 'http://www.quandl.com/api/v1/datasets/BITCOIN/MTGOXUSD.json?&trim_start=%s&trim_end=%s&sort_order=desc' %  (start_date, end_date)

b_close = get_elements(bitstamp, 'Close')
g_close = get_elements(gox, 'Close')

print b_close
print g_close

spread = []
for i, close in enumerate(b_close):
    s = close - g_close[i]

print spread

#query returns a json object of historical data
def query(url):
    pass
