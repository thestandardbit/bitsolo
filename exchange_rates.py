import mexbtcapi
from mexbtcapi.concepts.currencies import USD
from mexbtcapi.concepts.currency import Amount

dollars = "100" * USD

for api in mexbtcapi.apis:
	try:
		exchange_rate = api.market(USD).getTicker().sell
	except:
		print "%s: %s" % (api.name, "(request failed)")
	else:
		print "%s: %s" % (api.name, exchange_rate)

