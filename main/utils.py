import os

from dateutil.parser import parse

import requests


def convert_to_timestamp(value: str) -> float:
    _datetime = parse(value)
    return _datetime.timestamp()


def make_required(key_name):
    """
    Raises error for given environment key is last one is not set.
    :param key_name: <class: str> environment key name
    :return: value for given environment key
    """
    value = os.environ.get(key_name)
    if not value:
        raise EnvironmentError(f'The key `{key_name}` is required.')
    return value


class Client:
    """
    Service class for making API calls and retrieving data from resources.
    """

    __slots__ = ('url', 'session', 'public_key', 'secret')

    def __init__(self, url=None, public_key=None, secret_key=None):
        self.url = url
        self.session = requests.session()
        self.session.auth = (public_key, secret_key)

    def _get_response(self, endpoint):
        response = self.session.get(endpoint)
        response.raise_for_status()
        return response.json()

    def get_transactions(self):
        """Returns transaction info."""
        endpoint = f'{self.url}/account/transactions/'
        return self._get_response(endpoint)

    def get_trades(self):
        """Returns trades info."""
        endpoint = f'{self.url}/history/trades'
        return self._get_response(endpoint)


class PrepareDataMixin:
    """
    Service mixin for data preparing in the following format:
    - timestamp: unix timestamp
    - assetName: `symbol` for trades and `currency` for account transactions
    - type: `side` field for trades and `type` for account transactions
    - quantity: `quantity` field for trades, `amount` field for transactions
    - price: `price` field for trades, `1` for account transactions
    - fee: fee
    """

    @staticmethod
    def _prepare_trade_data(client):
        trades = client.get_trades()
        data = [
            {
                'timestamp': convert_to_timestamp(trade['timestamp']),
                'assetName': trade['symbol'],
                'type': trade['side'],
                'quantity': trade['quantity'],
                'price': trade['price'],
                'fee': trade.get('fee'),
            } for trade in trades
        ]
        return data

    @staticmethod
    def _prepare_transactions_data(client):
        transactions = client.get_transactions()
        data = [
            {
                'timestamp': convert_to_timestamp(txn['createdAt']),
                'assetName': txn['currency'],
                'quantity': txn['amount'],
                'type': txn['type'],
                'price': 1,
                'fee': txn.get('fee'),
            } for txn in transactions
        ]
        return data
