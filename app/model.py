def predict_price_trend(current_price: float) -> dict:
    if current_price > 2800:
        return {
            "trend": "price_may_drop",
            "score": 0.92,
            "comment": "السعر مرتفع عن المعدل المتوقع"
        }
    elif current_price < 2700:
        return {
            "trend": "price_may_rise",
            "score": 0.87,
            "comment": "السعر منخفض عن المعدل المتوقع"
        }
    return {
        "trend": "stable",
        "score": 0.5,  # ✅ يجب إضافة score حتى لو ثابت
        "comment": "السعر مستقر قريب من المتوسط"
    }
