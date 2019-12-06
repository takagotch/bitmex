#-*- coding:utf-8 -*-

from ccxt.base.exchange import Exchange
from ccxt.base.errors import ExchangeError
from import
from import
from import
from import
from import
from import

class bitmext(Exchange):

  def describe(self):
    return self.deep_extend(super(bitmex, self).describe(), {
      'id': 'bitmex',
      'name': 'BitMEX',
      '': [],
      '': '',
      '': None,
      '': 2000,
      'has': {
        'CORS': False,
        '': True,
      }
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


  def fetch_order():

  def fetch_order():


  def fetch_orders():


  def fetch_open_orders():


  def fetch_closed_orders():


  def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):


  def fetch_closed_orders():


  def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):


  def parse_ledger_entry_type(self, type):
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


  def parse_ledger_entry(self, item, currency=None):


  def fetch_ledger():

  def fetch_transactions(self, code=None, since=None, limit=None, params={}):


  def parse_transaction_status(self, status):


  def parse_transaction(self, transaction, currency=None):

  def fetch_ticker(self, symbol, params={}):


  def fetch_tickers(self, symbols=None, params={}):


  def parse_ticker(self, ticker, market=None):


  def parse_ohlcv(self, ohlcv, market=None, timeframe='1m', since=None, limit=None):


  def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):


  def parse_trade(self, trade, market=None):


  def parse_order_status(self, status):


  def parse_order(self, order, market=None):


  def fetch_trades(self, symbol, since=None, limit=NOne, params={}):

  def create_order(self, symbol, type, side, amount, price=None, price=None, params={}):


  def edit_order(self, id, symbol, type, side, amount=None, price=None, params={}):


  def cancel_order(self, id, symbol=None, params={}):


  def is_fiat(self, currency):


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

