from .validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)


def place_order(client, logger, symbol, side, order_type, quantity, price=None):
    try:
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(float(quantity))
        price = validate_price(price, order_type)

        logger.info(f"Request -> {symbol} {side} {order_type} qty={quantity} price={price}")

        if order_type == "MARKET":
            response = client.place_market_order(symbol, side, quantity)
        else:
            response = client.place_limit_order(symbol, side, quantity, price)

        logger.info(f"Response -> {response}")

        print("\nOrder Success")
        print(f"OrderId: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")

    except Exception as e:
        logger.error(str(e))
        print(f"\nOrder Failed: {e}")
