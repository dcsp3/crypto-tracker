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
        currency_pnl = self.getCurrencyPnL(currency)
        currency_cost_basis = self.getCurrencyCostBasis(currency)

        return round((currency_pnl/currency_cost_basis) * 100, 2)

    def getCurrencyAllocationPercent(self, currency):
        currency_value = self.getCurrencyValue(currency)
        total_value = self.getTotalPortfolioValue()

        return round((currency_value/total_value) * 100, 2)
    
    def getCurrencyValuePairs(self): 
        currency_value_pairs = []
        
        for i in self.currencies:
            currency_value_pairs.append([i.currency, round(self.getCurrencyValue(i), 2)])

        return currency_value_pairs
    
    def getTableData(self):
        table_data = []

        for currency in self.currencies:
            data = {}
            data["currency"] = currency.currency
            data["amount"] = self.getCurrencyAmount(currency)
            data["cost_basis"] = self.getCurrencyCostBasis(currency)
            data["current_value"] = round(self.getCurrencyValue(currency), 2)
            data["pnl"] = round(self.getCurrencyPnL(currency), 2)
            data["roi"] = str(self.getCurrencyROIPercent(currency)) + "%"
            data["allocation"] = str(self.getCurrencyAllocationPercent(currency)) + "%"

            table_data.append(data)
        
        return table_data
    
    def getTotalPortfolioValue(self):
        total_value = 0.0

        for currency in self.currencies:
            total_value += self.getCurrencyValue(currency)

        return round(total_value, 2)
    
    def getTotalPnL(self):
        total = 0

        for currency in self.currencies:
            total += self.getCurrencyPnL(currency)

        return round(total, 2)

    def getTotalROI(self):
        total = 0

        for currency in self.currencies:
            total += self.getCurrencyPnL(currency)

        return round(total / len(self.currencies), 2)