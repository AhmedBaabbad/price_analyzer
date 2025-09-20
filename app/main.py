# 📁 app/main.py

from fastapi import FastAPI
from .api import router as price_router

app = FastAPI(
    title="AI Price Analyzer",
    description="خدمة تحليل الأسعار باستخدام الذكاء الاصطناعي",
    version="1.0.0"
)

# ربط الراوتر
app.include_router(price_router, prefix="/api")
