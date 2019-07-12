from .utils import make_required


class Config:
    API = 'https://api.hitbtc.com/api/2'
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT: 60
    PUBLIC_KEY = make_required('PUBLIC_KEY')
    SECRET_KEY = make_required('SECRET_KEY')
