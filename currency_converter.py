# currency_converter.py
# Aidan Nachi
# 2023.05.03
#
# This file defines functions that make get requests from the FreecurrencyAPI
# in order to convert a user inputted base currency to numerous other currencies.
# The program displays foreign exchange data and allows the user to select which
# currency they want to convert from and the currency for the data they want to
# recieve.


import requests

# Constant Variables
API_KEY = "fca_live_R14VTAo9g4FavBE3fZKeTJa8SwFSkFilOV574cPL"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCIES = ['USD', 'CAD', 'EUR', 'AUD', 'CNY', 'JPY', 'BGN', 'CZK', 'GBP', 'INR'
              , 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK', 'NOK', 'HRK', 'RUB', 'TRY',
              'BRL', 'HKD', 'IDR', 'ILS', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 
              'THB', 'ZAR']


def get_conversion_currencies(base):
    """ Get currency data for the currencies. """

    # Seperate currencies with a comma.
    currencies = ",".join(CURRENCIES)

    # Establish a url with the base currency and the currencies we want
    # data for.
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    # Attempt to get currency data.
    try:
        response = requests.get(url)
        data = response.json()
        return data['data']

    # Print error if attemp fails and avoid crashing the program. 
    except:
        print("Invalid Currency")
        return None
    

def get_conversion_currency(base, conversion_currency):
    """ Convert base currencies to chosen currency. """


    # Establish a url where we can take the base currency and the
    # currency we want data for.
    url = f"{BASE_URL}&base_currency={base}&currencies={conversion_currency}"

    # Attempt to get currency data.
    try:
        response = requests.get(url)
        data = response.json()
        return data['data']

    # Print error if attemp fails and avoid crashing the program. 
    except:
        print("Invalid Currency")
        return None

def do_currency_conversion():
    """ Convert and print currencies from a base currency. """

    print("\nCURRENCY CONVERTER\n")
    print("The Currency Converter converts a user inputted base currency and displays"+
          " Foreign \nExchange data for the conversion to other foreign currencies.\n")

    # Give users the option to convert currencies.
    while True:

        # Allow users to input valid currencies for conversion
        user_base_currency_input = input("\nEnter the base currency (q for quit): ").upper()
        print('')

        if user_base_currency_input == 'Q':
            break

        choose_to_transfer_option = input("What currency would you like to transfer to? "+
                                          "('All' for all currencies): ").upper()
        print('')
        
        # Print out all currencies converted from the base currency.
        if choose_to_transfer_option == 'ALL':

            # Set our data to be all of the currencies.
            data = get_conversion_currencies(user_base_currency_input)
        
            if not data:
                continue

            # Print currency conversions for currencies that are not
            # the base currency.
            del data[user_base_currency_input]

            for ticker, value in data.items():
                print(f"{ticker}: {value}")
            print('')

        else:

            # Set our data to be the currency the user selected.
            data = get_conversion_currency(user_base_currency_input, 
                                           choose_to_transfer_option)

            if not data:
                continue

            for ticker, value in data.items():
                print(f"{ticker}: {value}")
            print('')

def main():
    """ Demonstrate functionality of currency conversion. """

    do_currency_conversion()


if __name__ == "__main__":
    main()