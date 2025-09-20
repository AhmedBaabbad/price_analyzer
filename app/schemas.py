from pydantic import BaseModel


class PriceInput(BaseModel):
    price: float


class AnalysisResult(BaseModel):
    trend: str
    score: float
    comment: str
