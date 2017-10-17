''''''
import quandl
import pandas as pd

#my API key iU9ZbpyyhDs4dSLiRdDr

def getStockFromQuandl(symbol, name, start, end):
    """
    Downloads Stock from Quandl.
    Computes daily Returns based on Adj Close.
    Returns pandas dataframe.
    """
    #import quandl
    df =  quandl.get(symbol, trim_start = start, trim_end = end, authtoken="b2-BGG-ptXRn6-WCBMy5") #elena's quandl key
 
    df.columns.values[-1] = 'AdjClose'
    df.columns = df.columns + '_' + name
    df['Return_%s' %name] = df['AdjClose_%s' %name].pct_change()
    
    return df



def main():
    quandl.ApiConfig.api_key = 'b2-BGG-ptXRn6-WCBMy5'
    quandl.ApiConfig.api_version = '2015-04-09'
    #data = quandl.get('NSE/OIL')
    #data1 = quandl.get_table('ZACKS/FC', ticker='AAPL')
    #data.head()
    data = quandl.get_table('ZACKS/FC', ticker='AAPL')
    #data = quandl.get("EOD/GOOGL")

    data.columns.values[-1] = 'AdjClose'
    data.columns = data.columns + '_' + 'someName'
    data['Return_%s' %'someName'] = data['AdjClose_%s' %'someName'].pct_change()

    #data.groupby('A', as_index=False).head(1)
    print("testing quandl")
    print(data)
    print("\n\n\n\n\n\n\n*************************************")
    #print(data1)


if __name__ == "__main__":
    main()