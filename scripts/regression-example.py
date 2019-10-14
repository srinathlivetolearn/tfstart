import pandas as pd
import quandl as quandl

datafeed = quandl.get("WIKI/GOOGL", authtoken="yreUXt2fRyPK_zESHVNf")

datafeed = datafeed[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
