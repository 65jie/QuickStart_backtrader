#! python3
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])

import backtrader as bt
from backtrader import cerebro

from TestStrategy import TestStrategy

if __name__ == '__main__':
        cerebro = bt.Cerebro()

        strats = cerebro.optstrategy(TestStrategy, maperiod = range(10, 31))
        # cerebro.addstrategy(TestStrategy)

        modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
        datapath = os.path.join(modpath, 'datas\\orcl-1995-2014.txt')

        data = bt.feeds.YahooFinanceCSVData(
                dataname = datapath,
                fromdate = datetime.datetime(2000, 1, 1),
                todate = datetime.datetime(2000, 12, 31),
                reverse = False
        )

        cerebro.adddata(data)

        cerebro.broker.setcash(100000.0)

        cerebro.addsizer(bt.sizers.FixedSize, stake = 10)

        cerebro.broker.setcommission(commission = 0.0)

        # print('Start Portofolio Value: %.2f ' % cerebro.broker.getvalue())

        cerebro.run(maxcpus = 1)

        # print('Final Portofolio Value: %.2f' % cerebro.broker.getvalue())

        # cerebro.plot()
