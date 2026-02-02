def validate_inputs(args):
    if args.side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if args.type not in ["MARKET", "LIMIT", "STOP_MARKET"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_MARKET")

    if args.quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    # LIMIT order requires price
    if args.type == "LIMIT" and args.price is None:
        raise ValueError("Price is required for LIMIT orders")

    # STOP_MARKET requires stop_price (not price)
    if args.type == "STOP_MARKET" and args.stop_price is None:
        raise ValueError("stop_price is required for STOP_MARKET orders")

    # Notional check (only when price is known)
    if args.type == "LIMIT":
        if args.quantity * args.price < 100:
            raise ValueError("Order notional must be at least 100 USDT")
