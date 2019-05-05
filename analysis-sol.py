
# Imporint all required libraries
import  argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt


# This is written as per the requirement format for API
def assess_portfolio(sd = dt.datetime(2008,1,1), ed = dt.datetime(2009,1,1), \
    syms = ['GOOG','AAPL','GLD','XOM','TRV'], \
    allocs=[0.1,0.2,0.3,0.4], \
    sv=1000000,\
    rfr=0.0, sf=252.0, \
    gen_plot=False):


    dates = pd.date_range(sd, ed)              # Generating date range data frame
    dateSPY = pd.date_range(sd, ed)            # Doing the same for SPY
    dfAdj = pd.DataFrame(index=dates)          # Creating a Data frame with dates as index
    dfAdjSPY = pd.DataFrame(index=dates)       # Same for SPY

    for x in syms:                             # For all symbols in syms
        df2 = pd.read_csv('data2/' + x + '.csv', index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'],na_values=['NaN'])    # Reading files from the data/xxx.csv. Also replacing missing values with NANs
        df2 = df2.rename(columns={'Adj Close': x})     # Renaming the Adj Close column to the symbol
        dfAdj = dfAdj.join(df2, how="inner")           # Inner join the data frames
        dfAdj = dfAdj.dropna()
    dfEquity = (dfAdj / dfAdj.ix[0, :])                # Normalizing the values by dividing with first row / all symbol values
    dfEquity = (dfEquity[:].mul(allocs))               # Multiplying each row with allocations
    dfEquity['Total Value'] = dfEquity.sum(axis=1)     # Row wise sum (for each day) create new column Total Value within the same frame

    dfSPY = pd.read_csv('data2/SPY.csv', index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['NaN']) # Doing the same process for SPY
    dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})
    dfSPY = dfSPY.join(dfAdjSPY, how="inner")
    dfSPY = dfSPY.dropna()
    dfSPYEquity = (dfSPY / dfSPY.ix[0, :])
    dfEquity['Daily Return'] = dfEquity['Total Value'].pct_change(1)                    # Daily Return is computed by percentage change Default is 1 , compares with one row above
    sr= dfEquity['Daily Return'].mean()*(sf**0.5) / dfEquity['Daily Return'].std()      # Computing sharpe ratio
    dr = (dfEquity['Total Value'] / dfEquity['Total Value'].shift(1)) - 1               # Daily returns as per slide
    cr = (dfEquity['Total Value'][-1:].item() / dfEquity['Total Value'][0].item()) - 1  # Total Value as per slide
    adr = dr.mean() # Mean for daily return - Avg. daily return
    sddr = dr.std() # Standard deviation    - Volatility
    ev=cr*sv+sv

    # This is for generating plot (Portfolio comparison SPY) Price across dates
    if gen_plot:
        ax = dfEquity.plot(y='Total Value', label='Portfolio', title="Stock Prizes", fontsize=20)
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        dfSPYEquity.plot(ax=ax)
        ax.plot
        ay = plt.show()
        pass



    return cr, adr, sddr, sr, ev





# This is the main code to take Argument Parsers
def run_code():
   #parser = argparse.ArgumentParser( prog='analysis', add_help=True, description='Short Sample' )

# Default Values
    start_date = '2010-01-01'
    end_date = '2010-12-31'
    alloc = [0.2,0.3,0.4,0.1]
    symbols=['GOOG']
    plotStat=True
    start_val = 1000000

# Parsing Arguments
#    parser.add_argument('-p', action="store_false", dest="plotStat", default=plot)
#    parser.add_argument('-s', action="store", dest="start_date",default=start)
#    parser.add_argument('-e', action="store", dest="end_date",default=end)
#    parser.add_argument('-a', nargs='*',action="store", dest="allocations",default=alloc)
#    parser.add_argument('-x', nargs='*',action="store", dest="symbols",default=syms)
#    args = parser.parse_args()
#    alloc=list(map(float,args.allocations))  # Converting string list to float list

# Function call
    cr, adr, sddr, sr, ev = assess_portfolio(sd=start_date, ed=end_date, \
                                         syms=symbols, \
                                         allocs=alloc, \
                                         sv=start_val, \
                                         gen_plot=plotStat)



# Priting the results
    print("Start Date : "+args.start_date)
    print("End Date   : "+args.end_date)
    print("Symbols    :",end=" ")
    print(args.symbols)
    print("Allocations:",end=" ")
    print(args.allocations)
    print("Sharpe Ratio                       : "+repr(sr))
    print("Volatility (stdev of daily returns): "+repr(sddr))
    print("Average Daily Return               : "+repr(adr))
    print("Cumulative Return                  : "+repr(cr))
#    print("End Value                          : "+"$"+repr(ev))



if __name__ == "__main__":
    run_code()

