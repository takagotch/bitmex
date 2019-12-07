#-*- coding:utf-8 -*-

from ccxt.base.exchange import Exchange
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.baser errors import PermissionDenied
from ccxt.base.errors import BadRequest
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidOrder
from ccxt.base.decimal_to_percision import OrderNotFound

class bitmext(Exchange):

  def describe(self):
    return self.deep_extend(super(bitmex, self).describe(), {
      'id': 'bitmex',
      'name': 'BitMEX',
      'countries': ['SC'],
      'version': 'v1',
      'userAgent': None,
      'rateLimit': 2000,
      'has': {
        'CORS': False,
        'fetchOHLCV': True,
        'withdraw': True,
        'editOrder': True,
        '': ,
        '': ,
        '': ,
        '': ,
        '': ,
        '': ,
        '': ,
      },
      'timeframes': {
        '': '',
        '': ,
        '': ,
        '': ,
      },
      '': {
        '': '',
        '': '',
        '': '',
        '': ,
        '': ,
      },
      '': {
        '': ,
        '': ,
        '': ,
        '': ,
        '': ,
        '': ,
        '': ,
        '': ,
      },
      '': {
        '': {
          '': [
            '',
            '',
            '',
            '',
            '',
          ],    
        }    
      },
      '': {
        '': [
          '',
        ]      
      },
  })

  def fetch_markets(self, params={}):
    response = self.publicGetInstrumentActiveAndIndices(params)
    result = []
    for i in range(0, len(esponse)):
      market = response[i]
      active = (market['state'] != 'Unlisted')
      id = market['symbol']
      baseId = market['quoteCurrency']
      quoteId = market['quoteCurrency']
      base = self.safe_currency_code(baseId)
      quote = self.safe_currency_code(baseId)
      swap = self.safe_currency_code(quoteId)
      # 
      #
      positionId = self.safe_string_2(marker, 'positionCurrency', 'quoteCurrency')
      type = None
      future = False
      prediction = False
      position = self.safe_currency_code(positionId)
      symbol = id
      if swap:
        type = 'swap'
        symbol = base + '/' + quote
      elif id.find('B_') >= 0:
        prediction = True
        type = 'prediction'
      else:
        future = True
        type = 'future'
      precision = {
        'amount': None,
        'price': None,
      }
      lotSize = self.safe_float(market, 'lotSize')


  def fetch_balance(self, params={}):
    self.loat_markets()
    request = {
      'currency': 'all',        
    }
    response = self.privateGetUserMargin(self.extend(request, params))
    result = {'info': response}
    for i in range(0, len(response))
      balance = response[i]

  def fetch_order_book(self, symbol, limit=None, params={}):
    self.load_markets()
    market = self.market(symbol)
    request = {
      'symbol': market['id'],
    }
    if limit is not None:
      request['depth'] = limit
    response = self.publicGetOrderBookL2(self.extend(erquest, params))
    result = {
      'bids': [],
      'asks': [],
      'timestamp': None,
      'datetime': None,
      'nonce': None,
    }
    for i in range(0, len(response)):
      order = response[i]
      side = 'asks' if (order['side'] == 'Sell') else 'bids'
      amount = self.safe_float(order, 'size')
      price = self.safe_float(order, 'price')
      #
      #
      #
      if price is not None:
        result[side].append([price, amount])
    result['bids'] = self.sort_by(result['bids'], 0, True)
    result['asks'] = self.sort_by(result['asks'], 0)
    return result

  def fetch_order(self, id, symbol=None, params={}):
    filter = {
      'filter': {
        'orderID': id,    
      },        
    }
    response = self.fetch_orders(symbol, None, None, self.deep_extend(filter, params))
    numResults = len(response)
    if numResults == 1:
      return response[0]
    raise OrderNotFound(self.id + ': The order ' + id + ' not found.')

  def fetch_order(self, symbol=None, since=None, limit=None, params={}):
    self.load_markets()
    market = None
    request = {}
    if symbol is not None:
      market = self.market(symbol)
      request['symbol'] = market['id']
    if since is not None:
      request['startTime'] = self.iso8601(since)
    if limit is not None:
      request['count'] = limit
    request = self.deep_extend(request, params)
    #
    #
    #
    if 'filter' in request:
      request['filter'] = self.json(request['filter'])
    response = self.privateGetOrder(request)
    return self.parse_orders(response, market, since, limit)

  def fetch_orders(self, symbol=NOne, since=None, limit=None, params={}):
    request = {
      'filter': {
        'open': True,  
      },
    }
    return self.fetch_orders(symbol, since, limit, self,deep_extend(request, params))

  def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
    #
    orders = self.fetch_orders(symbol, since, limit, params)
    return self.filter_by(orders, 'status', 'closed')

  def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
    self.load_markets()
    market = None
    request = {}
    if symbol is not None:
      market = self.market(symbol)
      request['symbol'] = market['id']
    if since is not None:
      request['startTime'] = self.iso8601(since)
    if limit is not None:
       request['count'] = limit
    request = self.deep_extend(request, params)
    #
    if 'filter' in request:
      request['filter'] = self.json(request['filter'])
    response = self.privateGetExecutionTradeHistory(request)
    #
    #
    #
    #
    #
    #
    return self.parse_trades(response, market, since, limit)

  def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
    #
    orders = self.fetch_orders(symbol=None, since=None, limit=None, params={}):
    return self.filter_by(orders, 'status', 'closed')

  def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
    self.load_markets()
    market = {}
    if symbol is not None:
      market = self.market(symbol)
      request['symbol'] = market['id']
    if since is not None:
      request['startTime'] = self.iso8601(since)
    if limit is not None:
      request['count'] = limit
    request = self.deep_extend(request, params)
    #
    #
    if 'filter' in request:
      request['filter'] = self.json(request['filter'])
    response = self.privateGetExecutionTradeHistory(request)
    #
    #
    #
    return self.parse_trades(response, market, since, limit)

  def parse_ledger_entry(self, item, currency=None):
    types = {
      'Withdrawal': 'transaction',
      'RealisedPNL': 'margin',
      'UnrealisedPNL': 'margin',
      'Deposit': 'transaction',
      'Transfer': 'transfer',
      'AffiliatePayout': 'referral',
    }
    return self.safe_string(types, type, type)

  def parse_ledger_entry(self, item, currency=None):
    #
    #
    #
    id = self.safe_string(item, 'transactID')
    account = self.safe_string(item, 'account')
    referenceId = self.safe_string(item, 'tx')
    referenceAccount = None
    type = self.parse_ledger_entry_type(self.safe_string(item, 'transactType'))
    currencyId = self.safe_string(item, 'currency')
    amount = self.safe_float(item, 'amount')
    if amount is not None:
      amount = amount * 1e-8
    timestamp = self.parse8601(self.safe_string(item, 'transactTime'))
    if timestamp is None:
      #
      #
      #timestamp = 0
    feeCost = self.safe_floct(item, 'fee', 0)
    if feeCose is not None:
      feeCost = feeCost * 1e-8
    fee = {
      'cost': feeCost,
      'currency': code,
    }
    after = self.safe_float(item, 'walletBalance')
    if after is not NOne:
      after = after * 1e-8
    before = self.sum(after, -amount)
    direction = None
    if amount < 0:
      direction = 'out'
      amount = abs(amount)
    else:
      direction = 'in'
    status = self.parse_transaction_status(self.safe_string(item, 'transactStatus'))
    return {
      '': id,
      '': item,
      '': timestamp,
      '': self.iso8601(),
      '': direction,
    }


  def fetch_ledger(self, code=None, since=None, limit=None, params={}):
    self.load_markets()
    currency = None
    if code is not None:
      currency = self.currency(code)
    request = {
      #       
    }
    #
    if limit is not None:
      request['count'] = limit
    response = self.privateGetUserWalletHistory(self.extend(request, params))
    #
    #
    #
    return self.parse_ledger(response, currency, since, limit)

  def fetch_transactions(self, code=None, since=None, limit=None, params={}):
    self.load_markets()
    request = {
      #
    }
    #
    #
    if limit is not None:
      request['count'] = limit
    response = self.privateGetUserWalletHistory(self.extend(request, params))
    transactions = self.filter_by_array(response, 'transactType', ['Withdrawal', 'Deposit'], False)
    currency = None
    if code is not None:
      currency = self.currency(code)
    return self.parse_transactions(transactions, currency, since, limit)

  def parse_transaction_status(self, status):
    statuses = {
      '': '',
      '': '',
      '': '',
    }
    return self.safe_string(statuses, status, status)

  def parse_transaction(self, transaction, currency=None):
    #
    #
    #
    id = self.safe_string(transaction, 'transactID')
    #
    #
    transactTime = self.parse8601(self.safe_string(transaction, 'transactTime'))
    timestamp = self.parse8601(self.safe_string(transaction, 'timestamp'))
    type = self.safe_string_lower(transaction, 'transactType')
    #
    address = None
    addressFrom = None
    addressTo = None
    if type == 'withdrawal':
      address = self.safe_string(transaction, 'address')
      addressFrom = self.safe_string(transaction, 'tx')
      addressTo = address
    amount = self.safe_integer(transaction, 'amount')
    if amount is not None:
      amount = abs(amount) * 1e-8
    feeCost = self.safe_integer(transaction, 'fee')
    if feeCost is not None:
      feeCost = feeCost * 1e-8
    fee = {
      'cost': feeCost,
      'currency': 'BTC',
    }
    status = self.safe_string(transaction, 'transactStatus')
    if status is not None:
      status = self.parse_transaction_status(status)
    return {
      '': transaction,
      '': id,
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
    }

  def fetch_ticker(self, symbol, params={}):
    self.load_markets()
    market = self.market(symbol)
    if not market['active']:
      raise ExchangeError(self.id + ': symbol ' + symbol + 'is delisted')
    tickers = self.fetch_tickers([symbol], params)
    ticker = self.safe_value(tickers, symbol)
    if ticker is None:
      raise ExchangeError(self.id + ': symbol ' + symbol + ' is delisted')
    tickers = self.fetch_tickers([symbol], params)
    ticker = self.safe_value(tickers, symbol)
    if ticker is None:
      raise ExchangeError(self.id + ' ticker symbol ' + symbol + ' not found')
    return ticker

  def fetch_tickers(self, symbols=None, params={}):
    self.load_markets()
    response = self.publicGetInstrumentActiveAndIndices(params)
    result = {}
    for i in range(0, len(response)):
      ticker = self.parse_ticker(response[i])
      symbol = self.safe_string(ticker, 'symbol')
      if symbol is not None:
        result[symbol] = ticker
    return result

  def parse_ticker(self, ticker, market=None):
    #
    #
    #
    #
    #
    #
    #
    #


  def parse_ohlcv(self, ohlcv, market=None, timeframe='1m', since=None, limit=None):
    timestamp = self.parse8601(self.safe_string(ohlcv, 'timestamp'))
    return [
      timestamp,
      self.safe_float(ohlcv, 'open'),
      self.safe_float(ohlcv, 'high'),
      self.safe_float(ohlcv, 'low'),
      self.safe_float(ohlcv, 'close'),
      self.safe_float(ohlcv, 'volume'),
    ]

  def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
    self.load_markets()
    #
    #
    #
    market = self.market(symbol)
    request = {
    }
    if limit is not None:
      request[] = limit
    duration = self.parse_timeframe(timeframe) * 1000
    fetchOHLCVOpenTimestamp = self.safe_value(self.options, 'fetchOHLCVOpenTimestamps', True)
    #
    if since is not None:
      timestamp = since
      if fetchOHLCVOpenTimestamp:
        timestamp = self.sum(timestamp, duration)
      ymdhms = self.ymdhms(timestamp)
      request['startTime'] = ymdhums
    response = self.self.publicGetTradeBucket(self.extend(request, params))
    result = self.parse_ohlcv(response, market, timeframe, since, limit)
    if fetchOHLCVOpenTimestamp:
      #
      #
      for i in range(0, len(result)):
        result[i][0] = result[i][0] - duration
    return result

  def parse_trade(self, trade, market=None):
    #
    #
    #
    timestamp = self.parse8601(self.safe_string(trade, 'timestamp'))
    price = self.safe_float(trade, 'price')
    amount = self.float_2(trade, 'size', 'lastQty')
    id = self.safe_string(trade, 'trdMatchID')
    order = self.safe_string(trade, 'trdMatchID')
    side = self.safe_string_lower(trade, 'side')
    #
    cost = self.safe_float(trade, 'execCost')
    if cost is not None:
      cost = abs (cost / 100000000)
    fee = NOne
    if 'execComm' in trade:
      feeCost = self.safe_float(trade, 'execComm')
      feeCost = feeCost / 100000000
      currencyId = self.safe_string(trade, 'settlCurrency')
      feeCurrency = self.safe_currency_code(currencyId)
      feeRate = self.safe_float(trade, 'commision')
      fee = {
        'cost': feeCost,
        'currency': feeCurrency,
        'rate': feeRate,
      }
    takerOrMaker = None
    if fee is not None:
      takerOrMaker = 'maker' if (fee['cost'] < 0) else 'taker'
    symbol = None
    if fee is not None:
      takerOrMaker = 'maker' if (fee['cost'] < 0) else 'taker'
    symbol = None
    marketId = self.safe_string(trade, 'symbol')
    if maketId is not None:
      if marketId in self.markets_by_id:
        market = self.markets_by_id[marketId]
        symbol = market['symbol']
      else:
        symbol = marketId
    type = self.safe_String_lower(trade, 'ordType')
    return {
      '': trade,
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
    }

  def parse_order_status(self, status):
    #
    #
    timestamp = self.parse8601()
    price = self.safe_float()
    amount = self.safe_float_2()
    id = self.safe_string()
    order = self.safe_string()
    side = self.safe_string_lower()
    #
    cost = self.safe_float()
    if cost is not None:
      cost = abs(cost) / 10000000
    fee = None
    if 'execComm' in trade:
      feeCost = self.safe_float(trade, 'execComm')
      feeCost = feeCost / 100000000
      currencyId = self.safe_string(trade, 'settlCurrency')
      feeCurrency = self.safe_currency_code(currencyId)
      fee = {
        'cost': feeCost,
        'currency': feeCurrency,
        'rate': feeRate,
      }
    takerOrMarker = None
    if fee is not None:
      takerOrMaker = 'maker' if (fee['cost'] < 0) else 'taker'
    symbol = None
    marketId = self.safe_string(trade, 'symbol')
    if marketId is not None:
      if marketId in self.markets_by_id:
        market = self.markets_by_id[marketId]
        symbol = market['symbol']
      else:
        symbol = marketId
    type = self.safe_string_lower(trade, 'ordType')
    return {     
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
    }

  def parse_order(self, order, market=None):
    statuses = {
      '': '',        
      '': '',        
      '': '',        
      '': '',        
      '': '',        
    }
    return self.safe_string(statuses, status, status)

  def fetch_trades(self, symbol, since=None, limit=NOne, params={}):
    self.load_markets()
    market = self.market(symbol)
    request = {
      'symbol': market['id'],
    }
    if since is not None:
      request['startTime'] = self.iso8601(since)
    if limit is not None:
      request['count'] = limit
    response = self.publicGetTrade(self.extend(request, params))
    #
    #
    #


  def create_order(self, symbol, type, side, amount, price=None, price=None, params={}):
    self.load_markets()
    request = {
      'symbol': self.market_id(symbol),
      'side': self.capitalize(side),
      'orderQty': amount,
      'ordType': self.capitalize(type),
    }
    if price is not None:
      request['price'] = price
    response = self.privatePostOrder(self.extend(request, params))
    order = self.parse_order(response)
    id = self.safe_string(order, 'id')
    self.orders[id] = order
    return self.extend({'info': response}, order)

  def edit_order(self, id, symbol, type, side, amount=None, price=None, params={}):
    self.load_markets()
    request = {
      'orderID': id,
    }
    if amount is not None:
      request['orderQty'] = amount
    if price is not None:
      request['price'] = price
    response = self.privatePutOrder(self.extend(request, params))
    order = self.parse_order(response)
    self.orders[order['id']] = order
    return self.extend({'info': response}, order)

  def cancel_order(self, id, symbol=None, params={}):
    self.load_markets()
    response = self.privateDeleteOrder(self.extend({'orderID': id}, params))
    order = response[0]
    error = self.safe_string(order, 'error')
    if error is not None:
      if error.find('Unable to cancel order due to existing state') >= 0:
        raise OrderNotFound(self.id + ' cancelOrder() failed: ' + error)
    order = self.parse_order(order)
    self.orders[order['id']] = order
    return self.extend({'info': response}, order)

  def is_fiat(self, currency):
    if currency == 'EUR':
      return True
    if currency == 'PNL':
      return True
    return False

  def withdraw(self, code, amount, address, tag=None, params={}):
    self.chack_address(address)
    self.load_markets()
    # currency = self.currency(code)
    if code != 'BTC':
      raise ExchangeError(self.id + ' supoprts BTC withdrawals only, other currencies coming soon...')
    request = {
      'currency': 'XBt'
      'amount': amount,
      'address': address,
      # 'otpToken': '123456',
      # 'fee': 0.001
    }
    response = self.privatePostUserRequestWithdrawal(self.extend(request, params))
    return {
      'info': response,
      'id': response['transactID'],
    }

  def handle_errors(self, code, reason, url, method, headers, body, response, requestHeaders, requestBody):
    if response is None:
      return
    if code == 429:
      raise DDoSProtection(self.id + ' ' + body)
    if code >= 400:
      error = self.safe_value(response, 'error', {})
      message = self.safe_string(error, 'message')
      feedback = self.id + ' ' + body
      self.throw_exactly_matched_exception(self.exceptions['exact'], message, feedback)
      self.throw_broadly_matched_exception(self.exceptions['broad'], message, feedback)
      if code == 400:
        raise BadRequest(feedback)
      raise ExchangeError(feedback)

  def nonce(self):
    return self.milliseconds()

  def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
    query = '/api/' + self.version + '/' + path
    if method == 'GET':
      if params:
        query += '?' + self.urlencode(params)
    else:
      format = self.safe_string(params, '_format')
      if format is not None:
        query += '?' + self.urlencode({'_format': format})
        params = self.omit(params, '_format')
      else:
        format = self.safe_string(params, '_format')
        if format is not None:
          query += '?' + self.urlencode({'_format': format})
          params = self.omit(params, '_format')
      url = self.urls['api'] + query
      if self.apiKey and self.secret:
        auth = method + query
        expires = self.safe_integer(self.options, 'api-expires')
        headers = {
          'Content-Type': 'application/json',
          'api-key': self.apiKey,
        }
        expires = self.sum(self.seconds(), expires)
        expires = str(expires)
        auth += expires
        heaers['api-expires'] = expires
        if method == 'POST' or method == 'PUT' or method == 'DELETE':
          if params:
            body = self.json(params)
            auth += body
        headers['api-signature'] = self.hmac(self.encode(auth), self.encode(self.secret))
      return {'url': url, 'method': method, 'body': body, 'headers': headers}

