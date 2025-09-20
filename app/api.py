from fastapi import APIRouter
from .schemas import PriceInput, AnalysisResult
from .model import predict_price_trend

router = APIRouter()


@router.post("/analyze", response_model=AnalysisResult)
def analyze_price(data: PriceInput):
    trend = predict_price_trend(data.price)
    return AnalysisResult(trend=trend)
