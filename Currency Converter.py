import requests

class CurrencyConverter:
    def __init__(self):
        """Initialize the Currency Converter."""
        self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"  # Base currency is USD

    def fetch_exchange_rates(self):
        """
        Fetch the latest exchange rates from the API.

        Returns:
            dict: A dictionary containing exchange rates.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()['rates']  # Return the rates from the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rates: {e}")
            return None
def convert_currency(self, amount, from_currency, to_currency, rates):
        """
        Convert amount from one currency to another using the provided exchange rates.


        Args:
            amount (float): The amount of money to convert.
            from_currency (str): The currency to convert from.
            to_currency (str): The currency to convert to.
            rates (dict): The dictionary of exchange rates.


        Returns:
            float: The converted amount.
        """
        if from_currency == "USD":
            # Convert from USD to the target currency
            return amount * rates.get(to_currency, 0)
        elif to_currency == "USD":
            # Convert from the source currency to USD
            return amount / rates.get(from_currency, 0)
        else:
            # Convert from source currency to target currency
            return (amount / rates.get(from_currency, 0)) * rates.get(to_currency, 0)


