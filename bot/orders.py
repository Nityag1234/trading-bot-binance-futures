from bot.validators import validate_inputs


def execute_order(client, args, logger):
    # validate CLI inputs
    validate_inputs(args)

    # ensure leverage is set (required for futures)
    client.set_leverage(args.symbol, leverage=1)

    order_payload = {
        "symbol": args.symbol,
        "side": args.side,
        "quantity": args.quantity,
        "reduceOnly": args.reduce_only
    }

    if args.type == "MARKET":
        order_payload["type"] = "MARKET"

    elif args.type == "LIMIT":
        order_payload.update({
            "type": "LIMIT",
            "price": args.price,
            "timeInForce": "GTC"
        })

    elif args.type == "STOP_MARKET":
        order_payload.update({
            "type": "STOP_MARKET",
            "price": args.price,
            "stopPrice": args.stop_price,
            "timeInForce": "GTC"
        })

    logger.info(f"Final order payload: {order_payload}")
    response = client.place_order(**order_payload)

    print("\n===== ORDER RESULT =====")
    print(f"Order ID     : {response.get('orderId')}")
    print(f"Status       : {response.get('status')}")
    print(f"Executed Qty : {response.get('executedQty')}")
    print("========================")

    return response
