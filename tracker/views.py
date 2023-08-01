from django.shortcuts import render

from .coinbase_tracker import CoinbaseTracker

# Create your views here.

def index(request):
    tracker = CoinbaseTracker()
    return render(request, "tracker/index.html", {
        "value": tracker.getTotalPortfolioValue(),
        "currency_value_pairs": tracker.getCurrencyValuePairs(),
        "currencies": [i.currency for i in tracker.currencies][::-1],
        "allocations": [tracker.getCurrencyAllocationPercent(i) for i in tracker.currencies][::-1],
        "table_data": tracker.getTableData()
    })

