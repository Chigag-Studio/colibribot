# A single source of truth for constant variables related to the exchange

from hummingbot.core.api_throttler.data_types import RateLimit

EXCHANGE_NAME = "alpaca"
REST_URL = "https://paper-api.alpaca.markets"
REST_URL_HK = "https://data.alpaca.markets/v2"
WSS_URL = "wss://stream.data.alpaca.markets/v2/iex"
WSS_URL_HK = "wss://stream.data.alpaca.markets/v2/iex"

# REST API ENDPOINTS
CHECK_NETWORK_PATH_URL = "v2/clock"
GET_TRADING_PAIRS_PATH_URL = "v2/assets"
GET_LAST_TRADING_PRICES_PATH_URL = "spot/v1/ticker"
GET_ORDER_BOOK_PATH_URL = "spot/v1/symbols/book"
CREATE_ORDER_PATH_URL = "v2/orders"
CANCEL_ORDER_PATH_URL = "v2/orders"
GET_ACCOUNT_SUMMARY_PATH_URL = "v2/account"
GET_ORDER_DETAIL_PATH_URL = "v2/orders"
GET_TRADE_DETAIL_PATH_URL = "spot/v1/trades"
GET_OPEN_ORDERS_PATH_URL = "v2/positions"


# WS API ENDPOINTS
WS_CONNECT = "WSConnect"
WS_SUBSCRIBE = "WSSubscribe"

# Alpaca has a per method API limit
RATE_LIMITS = [
    RateLimit(limit_id=CHECK_NETWORK_PATH_URL, limit=10, time_interval=1),
    RateLimit(limit_id=GET_TRADING_PAIRS_PATH_URL, limit=5, time_interval=1),
    RateLimit(limit_id=GET_TRADING_RULES_PATH_URL, limit=5, time_interval=1),
    RateLimit(limit_id=GET_LAST_TRADING_PRICES_PATH_URL, limit=5, time_interval=1),
    RateLimit(limit_id=GET_ORDER_BOOK_PATH_URL, limit=5, time_interval=1),
    RateLimit(limit_id=CREATE_ORDER_PATH_URL, limit=50, time_interval=1),
    RateLimit(limit_id=CANCEL_ORDER_PATH_URL, limit=50, time_interval=1),
    RateLimit(limit_id=GET_ACCOUNT_SUMMARY_PATH_URL, limit=10, time_interval=1),
    RateLimit(limit_id=GET_ORDER_DETAIL_PATH_URL, limit=50, time_interval=1),
    RateLimit(limit_id=GET_TRADE_DETAIL_PATH_URL, limit=10, time_interval=1),
    RateLimit(limit_id=GET_OPEN_ORDERS_PATH_URL, limit=10, time_interval=1),
    RateLimit(limit_id=WS_CONNECT, limit=1, time_interval=1),
    RateLimit(limit_id=WS_SUBSCRIBE, limit=60, time_interval=600),
]

ORDER_STATUS = {
    1: "FAILED",        # Order failure
    2: "OPEN",          # Placing order
    3: "REJECTED",      # Order failure, Freeze failure
    4: "ACTIVE",        # Order success, Pending for fulfilment
    5: "ACTIVE",        # Partially filled
    6: "FILLED",        # Fully filled
    7: "ACTIVE",        # Canceling
    8: "CANCELED",      # Canceled
    9: "ACTIVE",        # Outstanding (4 and 5)
    10: "COMPLETED"     # 6 and 8
}
