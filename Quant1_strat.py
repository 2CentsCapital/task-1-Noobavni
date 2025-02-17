import numpy as np
import pandas as pd
from backtesting import Backtest,Strategy
from backtesting.test import SMA
df =pd.read_csv("CleanedData")
def SMA(values,length):
    return pd.Series(values).rolling(length).mean()

class SMACross(Strategy):
    long=50
    short=10
    def init(self):
        self.short_SMA=self.I(SMA,self.data.Close,self.short)
        self.long_SMA=self.I(SMA,self.data.Close,self.long)
    def next(self):
            if self.short_SMA[-1]>self.long_SMA[-1]:
                self.position.close()
                self.buy(sl=self.data.Close[-1]-3)
            elif self.long_SMA[-1]>self.short_SMA[-1]:
                self.position.close()
                self.sell(sl=self.data.Close[-1]+2)
                
            
bt=Backtest(df,SMACross,cash =10000)
stats=bt.run()
print(stats)
bt.plot()