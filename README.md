[HitBTC](https://hitbtc.com) Api Client
====================

A small Flask application that provides historical trades data with account transactions data from the HitBTC [API](https://api.hitbtc.com/api/2/explore/).

## Getting Started

### Requirements
- [Git](https://git-scm.com) >= 2.17.2
- [Docker](https://www.docker.com) >= 18.09.2
- [Docker Compose](https://docs.docker.com/compose/) >= 1.23.2


```
$ git clone git@github.com:kartava/hitbtc_api_client.git
$ cd hitbtc_api_client
$ docker-compose build
```

Wait a few minutes for the magic to happen.

### Required settings

backend: `hitbtc_api_client/.env.variables`
```
PUBLIC_KEY="<KEY>"
SECRET_KEY="<SECRET>"
```

### Run development server

```
$ docker-compose up
```

You're able to get access to the data by going to this URLs:

endpoint: http://0.0.0.0:5000/txs/
