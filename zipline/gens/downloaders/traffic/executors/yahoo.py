from requests.exceptions import RequestException
from yahoo_historical import Fetcher
import math
from dateutil.parser import parse
from zipline.gens.downloaders.traffic.executors.executor import _RequestExecutor
from zipline.gens.downloaders.traffic.requests import EquityRequest
from time import sleep


class _Yahoo(_RequestExecutor):
	#todo: find a better implementation for this... like use the built-in to_dict of pandas
	def _execute(self, request):
		if isinstance(request,EquityRequest):
			start = request.start_date
			start_arr = self._create_date(start)
			end = request.end_date
			try:
				if request.frequency == '1D':
					if start == end:
						f = Fetcher(request.symbol, start_arr)

					else:
						f = Fetcher(request.symbol, start_arr, self._create_date(end))
				else:
					raise NotImplementedError
				historical = f.getHistorical()
				sleep(0.1)
				dividends = f.getDividends()
				sleep(0.1)
				splits = f.getSplits()
				h = historical.set_index(historical.Date)
				s = splits.set_index(splits.Date).drop(['Date'], axis=1)
				d = dividends.set_index(dividends.Date).drop(['Date'], axis=1)
				s.loc[:, 'Stock Splits'] = [eval(i) for i in s.loc[:, 'Stock Splits']]
				l = h.merge(d, left_index=True, right_index=True, how='outer').merge(s, left_index=True,
																					 right_index=True,
																					 how='outer')
				tr = l.drop(['Date'], axis=1).reset_index().transpose()
				key = tr.index.get_loc
				date = key('Date')
				open_ = key('Open')
				high = key('High')
				low = key('Low')
				close = key('Close')
				volume = key('Volume')
				dividend = key('Dividends')
				split = key('Stock Splits')
				documents = []
				for d in range(tr.shape[1]):
					t = tr[d]
					s = t[split]
					p = t[dividend]
					if math.isnan(s):
						s = 1.0
					if math.isnan(p):
						p = 0.0
					documents.append(
						{'Date': parse(t[date]),
						 'Open': t[open_],
						 'High': t[high],
						 'Low': t[low],
						 'Close': t[close],
						 'Volume': t[volume],
						 'Dividend': p,
						 'Split': s})
				documents = documents[::-1]
				if start == end:
					documents.pop()
				return {'symbol': request.symbol, 'series': documents}
			except RequestException as e:
				print('unable to download data for {0}'.format(request.symbol),e)
				return None
			except Exception as e:
				print('unable to download data for {0}'.format(request.symbol),e)
				return None

	def _create_date(self, datetime):
		if datetime:
			return [datetime.year, datetime.month, datetime.day]
		else:
			return None

	def _cool_down_time(self):
		return 2.1 #todo: maybe use a random time between 0.1 and 2.1 secs
