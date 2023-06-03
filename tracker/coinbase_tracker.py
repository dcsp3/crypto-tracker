from coinbase.wallet.client import Client

class CoinbaseTracker:
    def __init__(self):
        api_file = open('tracker\\api_keys.txt', 'r')
        keys = api_file.read().split()

        self.api_key = keys[0]
        self.api_secret = keys[1]

        self.client = Client(self.api_key, self.api_secret)
        self.accounts = self.client.get_accounts() 

        self.assets = [x for x in self.accounts.data if float(x.balance.amount) > 0.00]

    def currencyToGBP(self, currency):
        price = self.client.get_spot_price(currency_pair=f"{currency}-GBP")
        return float(price.amount)

    def getWalletValue(self, asset):
        return float(asset.balance.amount) * self.currencyToGBP(asset.currency)

    def getTotalPortfolioValue(self):
        total_value = 0.0

        for asset in self.assets:
            total_value += self.getWalletValue(asset)

        return round(total_value, 2)