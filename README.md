Crypto Tracker is a web app that tracks my crypto portfolio using the Coinbase API. 

![image](https://github.com/dcsp3/crypto-tracker/assets/88645471/d96b63de-ac55-4b21-a2a3-ea0edc166231)

Future plans of this application are:
- Including other investments I make as I continue to diversify my portfolio thus making an all-in-one investment tracker.
- Switching to another web framework since using Django doesn't make any sense as we're not working with databases.


# Features

- Portfolio Value- The first section of the application includes the total portfolio value and a breakdown of all currencies and their respective values.
- Portfolio Allocation- This section features a doughnut chart (using [chart.js](https://www.chartjs.org/)) to display the allocation of different currencies in % value.
- Profit Margin- Features a horizontal bar chart (again, using [chart.js](https://www.chartjs.org/)) to display profit (or loss) margins for each individual currency. It also has a section to display the total return on investment (ROI%) and Total Profit/Loss in £.
- Table- The last section of the page contains a table that tracks various metrics of each individual currency.

# Installation
Clone the repository by `git clone https://github.com/dcsp3/crypto-tracker.git`

# Technologies Used
1. [Django](https://www.djangoproject.com/): Web framework
2. [Chart.js](https://www.chartjs.org/): Data visualisation
3. [Coinbase API](https://developers.google.com/books/):  Retrieving portfolio information
