from zipline import TradingAlgorithm
from zipline.transforms import MovingAverage as zma

class MovingAverage(TradingAlgorithm):
    def initialize(self, short_window=50, long_window=200):
        self.add_transform(zma, 'short_mavg', ['price'], window_length=short_window)
        self.add_transform(zma, 'long_mavg', ['price'], window_length=long_window)

    def handle_data(self, data):
        short_mavg = data['ATVI'].short_mavg['price']
        long_mavg = data['ATVI'].long_mavg['price']

        buy = False
        sell = False

        if short_mavg > long_mavg:
            buy = True
        elif long_mavg > short_mavg:
            sell = True

        self.record(short_mavg=short_mavg, long_mavg=long_mavg, buy=buy, sell=sell)