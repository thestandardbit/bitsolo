import requests
import json
import matplotlib.pyplot as plt

QUANDL_BASE_URL = 'http://www.quandl.com/api/v1/datasets/BITCOIN'

response_1 = requests.get(QUANDL_BASE_URL + '/BITSTAMPUSD.json?&sort_order=asc')
response_2 = requests.get(QUANDL_BASE_URL + '/MTGOXUSD.json?&sort_order=asc')

try:
    bitstamp_usd_response = json.loads(response_1.text)
    mtgox_usd_response = json.loads(response_2.text)
except ValueError:
    print "AH!"

bitstamp_usd_data = bitstamp_usd_response.get('data')
mtgox_usd_data = mtgox_usd_response.get('data')

dates_dictionary = {}

for data_item in bitstamp_usd_data:
        date_value = data_item[0]
        # for safety
        if date_value not in dates_dictionary:
            dates_dictionary[date_value] = {} # creating the object
        dates_dictionary[date_value]['mtgox'] = data_item
for data_item in mtgox_usd_data:
        date_value = data_item[0]
        if date_value not in dates_dictionary:
            dates_dictionary[date_value] = {}
        dates_dictionary[date_value]['bitstamp'] = data_item

print dates_dictionary


""" find intersection """

filtered_zipped_data = []

for key in dates_dictionary:
    zipped_date_item = dates_dictionary[key]
    if len(zipped_date_item) == 2:
        bitstamp_data = zipped_date_item['bitstamp']
        mtgox_data = zipped_date_item['mtgox']
        filtered_zipped_data.append( (mtgox_data, bitstamp_data) )

print len(filtered_zipped_data)
print filtered_zipped_data[0]

dates = []
dated_spread_nominal = []
dated_spread_percentage = []

import datetime

for zipped_data in filtered_zipped_data:
    bitstamp_close = zipped_data[0][4]
    mtgox_close = zipped_data[1][4]
    date_string = zipped_data[0][0]
    year, month, day = date_string.split('-')
    date_object = datetime.date(int(year), int(month), int(day))
    dates.append(date_object)

    spread_nominal = mtgox_close - bitstamp_close
    spread_percentage = (mtgox_close / bitstamp_close) - 1

    dated_spread_nominal.append(spread_nominal)
    dated_spread_percentage.append(spread_percentage)

plt.plot(dates, dated_spread_nominal)
plt.show()