# A single source of truth for constant variables related to the exchange

from hummingbot.core.api_throttler.data_types import RateLimit

EXCHANGE_NAME = "alpaca"
REST_URL = "https://paper-api.alpaca.markets"
REST_URL_HK = "https://data.alpaca.markets/v2"
WSS_URL = "wss://stream.data.alpaca.markets/v2/iex"
WSS_URL_HK = "wss://stream.data.alpaca.markets/v2/iex"

# REST API ENDPOINTS
CHECK_NETWORK_PATH_URL = "system/service"
GET_ASSET_PATH_URL = "/v2/assets"
GET_ASSET_SYMBOL_PATH_URL = "/v2/assets"
GET_TRADES_STATUS_PATH_URL = "/v2/events/trades"
GET_ORDER_BOOK_PATH_URL = "/v2/orders"
CREATE_ORDER_PATH_URL = "/v2/orders"
DELETE_ORDER_PATH_URL = "/v2/orders"
GET_ORDER_DETAIL_PATH_URL = "/v2/orders"
PATCH_ORDER_PATH_URL = "/v2/orders"
#MISC FUNCTIONS
GET_ACCOUNT_SUMMARY_PATH_URL = "/v2/account"
GET_OPEN_ORDERS_PATH_URL = "/v2/orders"
DELETE_ALL_ORDERS_PATH_URL = "/v2/orders"
#POSITIONS
GET_ALL_POSITIONS_PATH_URL = "/v2/positions"
DELETE_ALL_POSITIONS_PATH_URL = "/v2/positions"
DELETE_SPECIFIC_POSITION_PATH_URL = "/v2/positions"
#PORTFOLIO HISTORY
GET_PORTFOLIO_HISTORY_PATH_URL = "/v2/account/portfolio/history"

# WS API ENDPOINTS
WS_CONNECT = "WSConnect"
WS_SUBSCRIBE = "WSSubscribe"

# Alpaca has a per method API limit
RATE_LIMITS = [
    RateLimit(limit_id=CHECK_NETWORK_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_ASSET_SYMBOL_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_TRADES_STATUS_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_ALL_POSITIONS_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_ORDER_BOOK_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=CREATE_ORDER_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=DELETE_ORDER_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=DELETE_ALL_ORDERS_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_ACCOUNT_SUMMARY_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_ORDER_DETAIL_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=PATCH_ORDER_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_OPEN_ORDERS_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_PORTFOLIO_HISTORY_PATH_URL, limit=15, time_interval=1),
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
