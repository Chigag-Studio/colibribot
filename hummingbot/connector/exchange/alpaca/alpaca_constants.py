# A single source of truth for constant variables related to the exchange

from hummingbot.core.api_throttler.data_types import RateLimit
#REQUIRED
EXCHANGE_NAME = "alpaca"
REST_URL = "https://broker-api.alpaca.markets/"
REST_URL_SANDBOX = "https://broker-api.sandbox.alpaca.markets/"
WSS_URL = "wss://stream.data.alpaca.markets/v2/sip"
WSS_URL_SANDBOX = "wss://stream.data.alpaca.markets/v2/iex"

#HBOT  Stuff
HBOT_ORDER_ID_PREFIX = "x-XEKWYICX"

#todo; add account id and remove order_id from suffix where located below

# REST API ENDPOINTS
CHECK_NETWORK_PATH_URL = "system/service"
GET_ASSET_PATH_URL = "/v1/assets"
GET_ASSET_SYMBOL_PATH_URL = "/v1/assets/:symbol"
GET_TRADES_STATUS_PATH_URL = "/v1/events/trades"
GET_ORDER_BOOK_PATH_URL = "/v1/trading/accounts/{account_id}/orders"
CREATE_ORDER_PATH_URL = "/v1/trading/accounts/{account_id}/orders"
DELETE_ORDER_PATH_URL = "/v1/trading/accounts/{account_id}/orders/{order_id}"
GET_ORDER_DETAIL_PATH_URL = "/v1/trading/accounts/{account_id}/orders/{order_id}"
PATCH_ORDER_PATH_URL = "/v1/trading/accounts/{account_id}/orders/{order_id}"
#MISC FUNCTIONS
GET_ACCOUNT_SUMMARY_PATH_URL = "/v1/accounts/{account_id}"
GET_OPEN_ORDERS_PATH_URL = "/v1/trading/accounts/{account_id}/orders"
DELETE_ALL_ORDERS_PATH_URL = "/v1/trading/accounts/{account_id}/orders/"
#POSITIONS
GET_ALL_POSITIONS_PATH_URL = "/v1/trading/accounts/{account_id}/positions"
DELETE_ALL_POSITIONS_PATH_URL = "/v1/trading/accounts/{account_id}/positions"
DELETE_SPECIFIC_POSITION_PATH_URL = "/v1/trading/accounts/{account_id}/positions/{symbol}"
#PORTFOLIO HISTORY
GET_PORTFOLIO_HISTORY_PATH_URL = "/v1/trading/accounts/{account_id}/account/portfolio/history"

# WS API ENDPOINTS
WS_CONNECT = "WSConnect"
WS_SUBSCRIBE = "WSSubscribe"

# BitMart has a per method API limit
RATE_LIMITS = [
    RateLimit(limit_id=CHECK_NETWORK_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_ASSET_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_ASSET_SYMBOL_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_TRADES_STATUS_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_ORDER_BOOK_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=CREATE_ORDER_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=DELETE_ORDER_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_ACCOUNT_SUMMARY_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_ORDER_DETAIL_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=PATCH_ORDER_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_OPEN_ORDERS_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=DELETE_ALL_ORDERS_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_ALL_POSITIONS_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=DELETE_ALL_POSITIONS_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=DELETE_SPECIFIC_POSITION_PATH_URL, limit=15, time_interval=1),
    RateLimit(limit_id=GET_PORTFOLIO_HISTORY_PATH_URL, limit=15, time_interval=1),

    RateLimit(limit_id=WS_CONNECT, limit=1, time_interval=1),
    RateLimit(limit_id=WS_SUBSCRIBE, limit=60, time_interval=600),
]

ORDER_STATUS = {
    1: "new",               # The order has been received by Alpaca
    2: "partially_filled",  # Partially filled
    3: "filled",            # Completed
    4: "done_for_day",      # The order is done executing for the day,
    5: "canceled",          # The order has been canceled, and no further updates will occur for the order.
    6: "expired",           # The order has expired, and no further updates will occur for the order.
    7: "replaced",          # The order was replaced by another order, or was updated due to a market event.
    8: "pending_cancel",    # The order is waiting to be canceled.
    9: "pending_replace",   # The order is waiting to be replaced by another order.
}
