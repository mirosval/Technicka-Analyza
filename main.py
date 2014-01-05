from zipline.utils.factory import load_from_yahoo
from pandas import DataFrame
from moving_average import MovingAverage
import datetime
import logging
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

start = datetime.datetime.today() - datetime.timedelta(days=500)
end = datetime.datetime.today()

stocks = [row.strip() for row in open('indexes.csv') if row.strip() != ""]

data_cache_path = 'data_cache.csv'
if not os.path.exists(data_cache_path):
    logger.info("No Data Cache found, loading from Yahoo")
    data = load_from_yahoo(indexes={}, stocks=[stocks[0]], start=start, end=end, adjusted=False)
    data.to_csv(data_cache_path)
else:
    logger.info("Loading data from cache")
    data = DataFrame.from_csv(data_cache_path)

mavg = MovingAverage()
perf = mavg.run(data)

