def get_vat(price, vat_rate):
	vat = price / 100 * vat_rate
	prive_not_vat = price - vat
	print(prive_not_vat)

price1 = 500
vat_rate1 = 10
get_vat(price1, vat_rate1)

