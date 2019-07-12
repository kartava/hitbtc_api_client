from flask_restful import Resource
from werkzeug.utils import redirect

from . import app, cache, utils


class Index(Resource):

    def get(self):
        return redirect('/txs')


class Transactions(utils.PrepareDataMixin, Resource):

    @cache.cached()
    def get(self):
        client = utils.Client(
            app.config['API'],
            app.config['PUBLIC_KEY'],
            app.config['SECRET_KEY']
        )
        trades = self._prepare_trade_data(client)
        transactions = self._prepare_transactions_data(client)

        return trades + transactions
