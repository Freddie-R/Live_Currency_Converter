import requests


def get_data():
    #define the API endpoint URL
    url = "API url"

    #Make a GET request to the API endpoint
    response = requests.get(url) 

    #Check if the request was successful (status code 200)
    if response.status_code == 200:
        #Extract the JSON data
        data = response.json()
        #Print the result of the data
        return data
    else:
        print("Failed to retrive data")
        exit()


def past_data():
    #A set of data from 2024/04/10 used so not to use to API
    data = {'meta': {'last_updated_at': '2024-04-10T23:59:59Z'}, 'data': {'ADA': {'code': 'ADA', 'value': 1.694876951}, 'AED': {'code': 'AED', 'value': 3.6710906579}, 'AFN': {'code': 'AFN', 'value': 71.1974781664}, 'ALL': {'code': 'ALL', 'value': 94.9386465288}, 'AMD': {'code': 'AMD', 'value': 395.1396666584}, 'ANG': {'code': 'ANG', 'value': 1.7876402779}, 'AOA': {'code': 'AOA', 'value': 834.8953415895}, 'ARB': {'code': 'ARB', 'value': 0.6775453923}, 'ARS': {'code': 'ARS', 'value': 865.0195531297}, 'AUD': {'code': 'AUD', 'value': 1.5366802974}, 'AVAX': {'code': 'AVAX', 'value': 0.0210136446}, 'AWG': {'code': 'AWG', 'value': 1.79}, 'AZN': {'code': 'AZN', 'value': 1.7}, 'BAM': {'code': 'BAM', 'value': 1.8197803231}, 'BBD': {'code': 'BBD', 'value': 2}, 'BDT': {'code': 'BDT', 'value': 110.1602424963}, 'BGN': {'code': 'BGN', 'value': 1.8032202437}, 'BHD': {'code': 'BHD', 'value': 0.376}, 'BIF': {'code': 'BIF', 'value': 2870.8340486967}, 'BMD': {'code': 'BMD', 'value': 1}, 'BNB': {'code': 'BNB', 'value': 0.0016309974}, 'BND': {'code': 'BND', 'value': 1.3528802219}, 'BOB': {'code': 'BOB', 'value': 6.9097512324}, 'BRL': {'code': 'BRL', 'value': 5.0793308831}, 'BSD': {'code': 'BSD', 'value': 1}, 'BTC': {'code': 'BTC', 'value': 1.4117e-05}, 'BTN': {'code': 'BTN', 'value': 83.2398907572}, 'BWP': {'code': 'BWP', 'value': 13.554132117}, 'BYN': {'code': 'BYN', 'value': 3.2701690584}, 'BYR': {'code': 'BYR', 'value': 32701.687974434}, 'BZD': {'code': 'BZD', 'value': 2}, 'CAD': {'code': 'CAD', 'value': 1.3686702731}, 'CDF': {'code': 'CDF', 'value': 2786.9857226485}, 'CHF': {'code': 'CHF', 'value': 0.9128301086}, 'CLF': {'code': 'CLF', 'value': 0.025280003}, 'CLP': {'code': 'CLP', 'value': 954.068118821}, 'CNY': {'code': 'CNY', 'value': 7.2266614011}, 'COP': {'code': 'COP', 'value': 3802.059724537}, 'CRC': {'code': 'CRC', 'value': 505.2328586505}, 'CUC': {'code': 'CUC', 'value': 1}, 'CUP': {'code': 'CUP', 'value': 24}, 'CVE': {'code': 'CVE', 'value': 102.6383793406}, 'CZK': {'code': 'CZK', 'value': 23.670894594}, 'DAI': {'code': 'DAI', 'value': 0.993355149}, 'DJF': {'code': 'DJF', 'value': 177.721}, 'DKK': {'code': 'DKK', 'value': 6.9426211139}, 'DOP': {'code': 'DOP', 'value': 59.1056996992}, 'DOT': {'code': 'DOT', 'value': 0.1180918912}, 'DZD': {'code': 'DZD', 'value': 134.9965440388}, 'EGP': {'code': 'EGP', 'value': 47.5927864152}, 'ERN': {'code': 'ERN', 'value': 15}, 'ETB': {'code': 'ETB', 'value': 57.5483611541}, 'ETH': {'code': 'ETH', 'value': 0.0002812642}, 'EUR': {'code': 'EUR', 'value': 0.9306801689}, 'FJD': {'code': 'FJD', 'value': 2.2591903232}, 'FKP': {'code': 'FKP', 'value': 0.7976691765}, 'GBP': {'code': 'GBP', 'value': 0.7975701539}, 'GEL': {'code': 'GEL', 'value': 2.6853903618}, 'GGP': {'code': 'GGP', 'value': 0.797668643}, 'GHS': {'code': 'GHS', 'value': 13.4116019268}, 'GIP': {'code': 'GIP', 'value': 0.7976687977}, 'GMD': {'code': 'GMD', 'value': 59.0792199915}, 'GNF': {'code': 'GNF', 'value': 8543.0816317109}, 'GTQ': {'code': 'GTQ', 'value': 7.7817110362}, 'GYD': {'code': 'GYD', 'value': 208.9320112307}, 'HKD': {'code': 'HKD', 'value': 7.8319714025}, 'HNL': {'code': 'HNL', 'value': 24.6931434391}, 'HRK': {'code': 'HRK', 'value': 6.7518108419}, 'HTG': {'code': 'HTG', 'value': 134.5778329264}, 'HUF': {'code': 'HUF', 'value': 363.9475545474}, 'IDR': {'code': 'IDR', 'value': 15835.575020602}, 'ILS': {'code': 'ILS', 'value': 3.7476806063}, 'IMP': {'code': 'IMP', 'value': 0.7976691099}, 'INR': {'code': 'INR', 'value': 83.3595309707}, 'IQD': {'code': 'IQD', 'value': 1309.2177144893}, 'IRR': {'code': 'IRR', 'value': 42033.808434889}, 'ISK': {'code': 'ISK', 'value': 138.4747522086}, 'JEP': {'code': 'JEP', 'value': 0.7976687771}, 'JMD': {'code': 'JMD', 'value': 154.738777351}, 'JOD': {'code': 'JOD', 'value': 0.71}, 'JPY': {'code': 'JPY', 'value': 152.9083644866}, 'KES': {'code': 'KES', 'value': 129.9729283126}, 'KGS': {'code': 'KGS', 'value': 90.1627976033}, 'KHR': {'code': 'KHR', 'value': 4037.1754762214}, 'KMF': {'code': 'KMF', 'value': 453.0790653862}, 'KPW': {'code': 'KPW', 'value': 899.9791273153}, 'KRW': {'code': 'KRW', 'value': 1361.2272279812}, 'KWD': {'code': 'KWD', 'value': 0.3085700456}, 'KYD': {'code': 'KYD', 'value': 0.83333}, 'KZT': {'code': 'KZT', 'value': 446.9880334594}, 'LAK': {'code': 'LAK', 'value': 21190.693400186}, 'LBP': {'code': 'LBP', 'value': 89630.020260597}, 'LKR': {'code': 'LKR', 'value': 302.0019313862}, 'LRD': {'code': 'LRD', 'value': 193.8675241318}, 'LSL': {'code': 'LSL', 'value': 18.4784023477}, 'LTC': {'code': 'LTC', 'value': 0.0102951646}, 'LTL': {'code': 'LTL', 'value': 3.214464859}, 'LVL': {'code': 'LVL', 'value': 0.6542876714}, 'LYD': {'code': 'LYD', 'value': 4.8343106989}, 'MAD': {'code': 'MAD', 'value': 10.0169114378}, 'MATIC': {'code': 'MATIC', 'value': 1.1201097478}, 'MDL': {'code': 'MDL', 'value': 17.5249820659}, 'MGA': {'code': 'MGA', 'value': 4360.3741283553}, 'MKD': {'code': 'MKD', 'value': 56.7826185031}, 'MMK': {'code': 'MMK', 'value': 2096.4982090362}, 'MNT': {'code': 'MNT', 'value': 3394.6012894941}, 'MOP': {'code': 'MOP', 'value': 8.1473316165}, 'MRO': {'code': 'MRO', 'value': 356.999828}, 'MRU': {'code': 'MRU', 'value': 39.6730505988}, 'MUR': {'code': 'MUR', 'value': 46.1514985688}, 'MVR': {'code': 'MVR', 'value': 15.4312121848}, 'MWK': {'code': 'MWK', 'value': 1734.9521790622}, 'MXN': {'code': 'MXN', 'value': 16.455203192}, 'MYR': {'code': 'MYR', 'value': 4.7508508152}, 'MZN': {'code': 'MZN', 'value': 63.7675694868}, 'NAD': {'code': 'NAD', 'value': 18.7412020495}, 'NGN': {'code': 'NGN', 'value': 1247.6214621157}, 'NIO': {'code': 'NIO', 'value': 36.7954565234}, 'NOK': {'code': 'NOK', 'value': 10.8331413279}, 'NPR': {'code': 'NPR', 'value': 134.8362360426}, 'NZD': {'code': 'NZD', 'value': 1.6736702883}, 'OMR': {'code': 'OMR', 'value': 0.384380069}, 'OP': {'code': 'OP', 'value': 0.3273716172}, 'PAB': {'code': 'PAB', 'value': 0.998840157}, 'PEN': {'code': 'PEN', 'value': 3.7123906109}, 'PGK': {'code': 'PGK', 'value': 3.8293807501}, 'PHP': {'code': 'PHP', 'value': 56.4824073604}, 'PKR': {'code': 'PKR', 'value': 278.0477407505}, 'PLN': {'code': 'PLN', 'value': 3.9690205822}, 'PYG': {'code': 'PYG', 'value': 7408.5638403976}, 'QAR': {'code': 'QAR', 'value': 3.6424204123}, 'RON': {'code': 'RON', 'value': 4.6255905945}, 'RSD': {'code': 'RSD', 'value': 108.5690922606}, 'RUB': {'code': 'RUB', 'value': 93.2868721226}, 'RWF': {'code': 'RWF', 'value': 1288.4091170893}, 'SAR': {'code': 'SAR', 'value': 3.7449305277}, 'SBD': {'code': 'SBD', 'value': 8.3468707162}, 'SCR': {'code': 'SCR', 'value': 14.6050028549}, 'SDG': {'code': 'SDG', 'value': 601.5}, 'SEK': {'code': 'SEK', 'value': 10.7214020116}, 'SGD': {'code': 'SGD', 'value': 1.3538101587}, 'SHP': {'code': 'SHP', 'value': 0.7975700989}, 'SLL': {'code': 'SLL', 'value': 22568.733098319}, 'SOL': {'code': 'SOL', 'value': 0.0057335668}, 'SOS': {'code': 'SOS', 'value': 571.4447541346}, 'SRD': {'code': 'SRD', 'value': 35.1557367286}, 'STD': {'code': 'STD', 'value': 22983.245762819}, 'STN': {'code': 'STN', 'value': 22.9832534249}, 'SVC': {'code': 'SVC', 'value': 8.75}, 'SYP': {'code': 'SYP', 'value': 13001.874867772}, 'SZL': {'code': 'SZL', 'value': 18.7774933037}, 'THB': {'code': 'THB', 'value': 36.7080344304}, 'TJS': {'code': 'TJS', 'value': 11.0458515576}, 'TMT': {'code': 'TMT', 'value': 3.5}, 'TND': {'code': 'TND', 'value': 3.1105305534}, 'TOP': {'code': 'TOP', 'value': 2.3573303112}, 'TRY': {'code': 'TRY', 'value': 32.2682964213}, 'TTD': {'code': 'TTD', 'value': 6.7820809208}, 'TWD': {'code': 'TWD', 'value': 32.2454052235}, 'TZS': {'code': 'TZS', 'value': 2574.6328932096}, 'UAH': {'code': 'UAH', 'value': 39.1499548861}, 'UGX': {'code': 'UGX', 'value': 3797.3700149448}, 'USD': {'code': 'USD', 'value': 1}, 'USDC': {'code': 'USDC', 'value': 0.9927417364}, 'USDT': {'code': 'USDT', 'value': 0.9933536607}, 'UYU': {'code': 'UYU', 'value': 38.5590354099}, 'UZS': {'code': 'UZS', 'value': 12813.825859739}, 'VEF': {'code': 'VEF', 'value': 3613986.82788}, 'VES': {'code': 'VES', 'value': 36.139866141}, 'VND': {'code': 'VND', 'value': 24952.427544284}, 'VUV': {'code': 'VUV', 'value': 119.8090577819}, 'WST': {'code': 'WST', 'value': 2.7644292655}, 'XAF': {'code': 'XAF', 'value': 610.4857429962}, 'XAG': {'code': 'XAG', 'value': 0.0358283911}, 'XAU': {'code': 'XAU', 'value': 0.0004282603}, 'XCD': {'code': 'XCD', 'value': 2.7}, 'XDR': {'code': 'XDR', 'value': 0.7628801335}, 'XOF': {'code': 'XOF', 'value': 610.4857179701}, 'XPD': {'code': 'XPD', 'value': 0.0009552162}, 'XPF': {'code': 'XPF', 'value': 110.9833397837}, 'XPT': {'code': 'XPT', 'value': 0.0010382498}, 'XRP': {'code': 'XRP', 'value': 1.6086826883}, 'YER': {'code': 'YER', 'value': 249.9797023338}, 'ZAR': {'code': 'ZAR', 'value': 18.7857037173}, 'ZMK': {'code': 'ZMK', 'value': 9001.2}, 'ZMW': {'code': 'ZMW', 'value': 24.7752137559}, 'ZWL': {'code': 'ZWL', 'value': 361.9}}}
    return data

def intake_of_two_currencies(currency_codes):
    #This function propts the user to input two currency codes for converstion and returns the two currencies
    original = input("Please enter a currency code you are converting from (E.G. GBP, USD): ").upper()
    while True:
        if original in currency_codes:
            break
        else:
            original = input("That doesn't seem to be a recognizable currency code, please try again: ").upper()

    final = input("Please enter a currency code you are converting to (E.G. GBP, USD): ").upper()
    while True:
            if final in currency_codes:
                break
            else:
                final = input("That doesn't seem to be a recognizable currency code, please try again: ").upper()

    result = [original,final]
    return result

def get_value(currency,data):
    #This function retrives the value of a currency imputed and then outputs the value
    value = data['data'].get(currency, {}).get('value')
    return value

def get_val_original():
    #prompts the user to input the amount of currency to convert
    value = input("Please enter the amount of currency you wish to convert: ")
    value = ''.join(char for char in value if char.isdigit() or char == ".")
    while check_value(value) == False:
        value = input("That did not work for some reason, please try again: ")
    return value

def check_value(value):
    #Checks if the value inputed is a valid number up to 2 decimal points
    parts = value.split(".")
    if len(parts)==2 and len(parts[1]) <= 2:
        return True
    elif len(parts) == 1:
        return True
    else:
        return False

def main():
    #Get all the data from the API
    data = get_data()
    #Creates a list of all currency codes
    currency_codes = list(data['data'].keys())
    
    #get the two currencies the person wants to convert
    currencys_retrived = intake_of_two_currencies(currency_codes)

    #Get the currency codes
    currency_1_code = currencys_retrived[0]
    currency_2_code = currencys_retrived[1]

    #Get the values of the currencies
    currency_1_value = float(get_value(currency_1_code,data))
    currency_2_value = float(get_value(currency_2_code,data))

    #Get the orginal amount wanted to convert
    value_original = round(float(get_val_original()),2)

    #Calculate a final value
    final_value = round((value_original/currency_1_value)*currency_2_value,2)

    #Return the final value
    print(value_original, currency_1_code, "is equivilent to", final_value, currency_2_code)


if __name__ == "__main__":
    main()