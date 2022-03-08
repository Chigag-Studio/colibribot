#!/usr/bin/env python
from typing import Any, Dict, Optional

from hummingbot.connector.exchange.alpaca.alpaca_order_book_message import AlpacaOrderBookMessage
from hummingbot.core.data_type.order_book import OrderBook
from hummingbot.core.data_type.order_book_message import OrderBookMessageType

#todo; lyghtccode below orderbook message has been completed and aligns with formatting of Alpaca API

class AlpacaOrderBook(OrderBook):

    @classmethod
    def snapshot_message_from_exchange(cls,
                                       msg: Dict[str, any],
                                       timestamp: float,
                                       metadata: Optional[Dict] = None):
        """
        Convert json snapshot data into standard OrderBookMessage format
        :param msg: json snapshot data from live web socket stream
        :param timestamp: timestamp attached to incoming data
        :return: AlpacaOrderBookMessage
        """

        if metadata:
            msg.update(metadata)

        return AlpacaOrderBookMessage(
            message_type=OrderBookMessageType.SNAPSHOT,
            content=msg,
            timestamp=timestamp
        )

    @classmethod
    def trade_message_from_exchange(cls,
                                    msg: Dict[str, Any],
                                    timestamp: Optional[float] = None,
                                    metadata: Optional[Dict] = None):
        """
        Convert a trade data into standard OrderBookMessage format
        :param record: a trade data from the database
        :return: AlpacaOrderBookMessage
        """

        if metadata:
            msg.update(metadata)

        msg.update({
            "exchange_order_id": str(msg.get("client_order_id")),
            "trade_type": msg.get("side"),
            "price": msg.get("filled_avg_price"),
            "amount": msg.get("qty"),
        })

        return AlpacaOrderBookMessage(
            message_type=OrderBookMessageType.TRADE,
            content=msg,
            timestamp=timestamp
        )
