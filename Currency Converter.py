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


def run(self):
        """Run the currency converter tool."""
        rates = self.fetch_exchange_rates()
        if rates is None:
            print("Could not fetch exchange rates. Exiting the converter.")
            return

        print("Available currencies:", ', '.join(rates.keys()))  # Display available currencies

        while True:
            try:
                amount = float(input("Enter the amount to convert: "))
                from_currency = input("Enter the currency to convert from (e.g., USD, EUR): ").upper()
                to_currency = input("Enter the currency to convert to (e.g., USD, EUR): ").upper()

                if from_currency not in rates or to_currency not in rates:
                    print("Invalid currency. Please try again.")
                    continue

                # Perform currency conversion
                converted_amount = self.convert_currency(amount, from_currency, to_currency, rates)
                print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
            except ValueError:
                print("Invalid input. Please enter a valid number for the amount.")
            except Exception as e:
                print(f"An error occurred: {e}")