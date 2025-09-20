def predict_price_trend(current_price: float) -> str:
    if current_price > 2800:
        return "price_may_drop"
    elif current_price < 2700:
        return "price_may_rise"
    return "stable"
