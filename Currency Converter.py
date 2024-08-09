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
