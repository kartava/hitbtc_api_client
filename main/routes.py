from . import api, resources

api.add_resource(resources.Index, '/')
api.add_resource(resources.Transactions, '/txs')
