from json_module import reader, writer

countries = reader('countries.json')
currencies = reader('currencies.json')

for country in list(countries):
    if country['currency'] in currencies:
        country['currency'] = currencies[country['currency']]
    else:
        if "dollar" in str(country['currency_name']).lower():
            country['currency'] = {
                "symbol": f"{str(country['currency']).replace('D', '')}{str(country['currency_symbol'])}",
                "name": country['currency_name'],
                "symbol_native": country['currency_symbol'],
                "decimal_digits": 2,
                "rounding": 0,
                "code": country['currency'],
                "name_plural": f"{country['currency_name']}s"
            }
        else:
            country['currency'] = {
                "symbol": country['currency_symbol'],
                "name": country['currency_name'],
                "symbol_native": country['currency_symbol'],
                "decimal_digits": 2,
                "rounding": 0,
                "code": country['currency'],
                "name_plural": ""
            }

    country.pop("currency_name")
    country.pop("currency_symbol")

writer('countries-v2.json', countries)