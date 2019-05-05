"""MC2-P1: Market simulator."""

import pandas as pd
import numpy as np
import datetime as dt
import os
from util import get_data, plot_data


def compute_portvals(orders_file="./orders/orders.csv", start_val=1000000):
    # this is the function the autograder will call to test your code
    # TODO: Your code here

    # In the template, instead of computing the value of the portfolio, we just
    # read in the value of IBM over 6 months
    start_date = dt.datetime(2008, 1, 1)
    end_date = dt.datetime(2008, 6, 1)
    portvals = get_data(['IBM'], pd.date_range(start_date, end_date))
    portvals = portvals[['IBM']]  # remove SPY

    def assess_portfolio(sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 1, 1), \
                         syms=['GOOG', 'AAPL', 'GLD', 'XOM', 'TRV'], \
                         allocs=[0.1, 0.2, 0.3, 0.4], \
                         sv=1000000, \
                         rfr=0.0, sf=252.0, \
                         gen_plot=False):
        dates = pd.date_range(sd, ed)  # Generating date range data frame
        dateSPY = pd.date_range(sd, ed)  # Doing the same for SPY
        dfAdj = pd.DataFrame(index=dates)  # Creating a Data frame with dates as index
        dfAdjSPY = pd.DataFrame(index=dates)  # Same for SPY

        for x in syms:  # For all symbols in syms
            df2 = pd.read_csv('data2/' + x + '.csv', index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'],
                              na_values=[
                                  'NaN'])  # Reading files from the data/xxx.csv. Also replacing missing values with NANs
            df2 = df2.rename(columns={'Adj Close': x})  # Renaming the Adj Close column to the symbol
            dfAdj = dfAdj.join(df2, how="inner")  # Inner join the data frames
            dfAdj = dfAdj.dropna()
        dfEquity = (dfAdj / dfAdj.ix[0, :])  # Normalizing the values by dividing with first row / all symbol values
        dfEquity = (dfEquity[:].mul(allocs))  # Multiplying each row with allocations
        dfEquity['Total Value'] = dfEquity.sum(
            axis=1)  # Row wise sum (for each day) create new column Total Value within the same frame

        dfSPY = pd.read_csv('data2/SPY.csv', index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'],
                            na_values=['NaN'])  # Doing the same process for SPY
        dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})
        dfSPY = dfSPY.join(dfAdjSPY, how="inner")









    return portvals


def test_code():
    # this is a helper function you can use to test your code
    # note that during autograding his function will not be called.
    # Define input parameters









    of = "./orders/orders2.csv"
    sv = 1000000

    # Process orders
    portvals = compute_portvals(orders_file=of, start_val=sv)
    if isinstance(portvals, pd.DataFrame):
        portvals = portvals[portvals.columns[0]]  # just get the first column
    else:
        "warning, code did not return a DataFrame"

    # Get portfolio stats
    # Here we just fake the data. you should use your code from previous assignments.
    start_date = dt.datetime(2008, 1, 1)
    end_date = dt.datetime(2008, 6, 1)
    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = [0.2, 0.01, 0.02, 1.5]
    cum_ret_SPY, avg_daily_ret_SPY, std_daily_ret_SPY, sharpe_ratio_SPY = [0.2, 0.01, 0.02, 1.5]
'''
   "" "
    # Compare portfolio against $SPX
    print
    ("Date Range: {} to {}".format(start_date, end_date))
    print
    print
    "Sharpe Ratio of Fund: {}".format(sharpe_ratio)
    print
    "Sharpe Ratio of SPY : {}".format(sharpe_ratio_SPY)
    print
    print
    "Cumulative Return of Fund: {}".format(cum_ret)
    print
    "Cumulative Return of SPY : {}".format(cum_ret_SPY)
    print
    print
    "Standard Deviation of Fund: {}".format(std_daily_ret)
    print
    "Standard Deviation of SPY : {}".format(std_daily_ret_SPY)
    print
    print
    "Average Daily Return of Fund: {}".format(avg_daily_ret)
    print
    "Average Daily Return of SPY : {}".format(avg_daily_ret_SPY)
    print
    print
    "Final Portfolio Value: {}".format(portvals[-1])...
"" " '''

if __name__ == "__main__":
    test_code()