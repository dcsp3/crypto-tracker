from django.shortcuts import render

from .coinbase_tracker import CoinbaseTracker

# Create your views here.

def index(request):
    tracker = CoinbaseTracker()
    return render(request, "tracker/index.html", {
        "value": tracker.getTotalPortfolioValue(),
        "totalpnl": tracker.getTotalPnL(),
        "totalroi": tracker.getTotalROI(),
        "currency_value_pairs": tracker.getCurrencyValuePairs(),
        "currencies": [i.currency for i in tracker.currencies][::-1],
        "allocations": [tracker.getCurrencyAllocationPercent(i) for i in tracker.currencies][::-1],
        "pnl_margins": [tracker.getCurrencyPnL(i) for i in tracker.currencies],
        "table_data": tracker.getTableData()
    })

