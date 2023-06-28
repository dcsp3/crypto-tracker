from coinbase.wallet.client import Client

class CoinbaseTracker:
    def __init__(self):
        api_file = open('tracker\\coinbase_api_keys.txt', 'r')
        keys = api_file.read().split()

        self.api_key = keys[0]
        self.api_secret = keys[1]

        self.client = Client(self.api_key, self.api_secret)
        self.accounts = self.client.get_accounts() 

        self.currencies = [x for x in self.accounts.data if float(x.balance.amount) > 0.00][::-1]

        self.tableData = self.getTableData()

    def getCurrencyAmount(self, currency):
        return currency.balance.amount
    
    def currencyToGBP(self, currency):
        price = self.client.get_spot_price(currency_pair=f"{currency}-GBP")
        return float(price.amount)

    def getCurrencyValue(self, currency):
        return float(currency.balance.amount) * self.currencyToGBP(currency.currency)
    
    def getCurrencyCostBasis(self, currency):
        account_id = [x.id for x in self.accounts.data if x.currency == currency.currency][0]

        transactions = self.client.get_transactions(account_id)
        total_invested = 0.0

        for transaction in transactions.data:
            if transaction.type == 'buy':
                native_amount = float(transaction.native_amount.amount)
                total_invested += native_amount
        
        return total_invested
    
    def getCurrencyPnL(self, currency):
        return self.getCurrencyValue(currency) - self.getCurrencyCostBasis(currency)

    def getCurrencyROIPercent(self, currency):
        pass

    def getCurrencyAllocationPercent(self, currency):
        pass
    
    def getCurrencyValuePairs(self): 
        currency_value_pairs = []
        
        for i in self.currencies:
            currency_value_pairs.append([i.currency, round(self.getCurrencyValue(i), 2)])

        return currency_value_pairs
    
    def getTableData(self):
        pass
    

    def getTotalPortfolioValue(self):
        total_value = 0.0

        for currency in self.currencies:
            total_value += self.getCurrencyValue(currency)

        return round(total_value, 2)
    
    def getTotalPnL(self):
        pass