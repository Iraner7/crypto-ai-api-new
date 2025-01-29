from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
import os  # 🟢 os importiert

app = FastAPI()

# CORS für externe Anfragen erlauben
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🟢 Root-Route (fix 404 Fehler)
@app.get("/")
def home():
    return {"message": "API is running! Go to /docs for Swagger UI"}

# Datenmodell für Anfragen
class TradeRequest(BaseModel):
    coin: str
    timeframe: str  # z.B. "1h", "24h"

# Beispiel-Funktion für AI-Trading-Empfehlungen
def get_trade_recommendation(coin, timeframe):
    predictions = ["Buy", "Sell", "Hold"]
    return random.choice(predictions)  # Hier könnte dein AI-Modell entscheiden

# API-Route für Vorhersagen
@app.post("/predict")
def predict_trade(data: TradeRequest):
    recommendation = get_trade_recommendation(data.coin, data.timeframe)
    return {"coin": data.coin, "timeframe": data.timeframe, "recommendation": recommendation}

# Falls das Skript direkt ausgeführt wird
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Port von Render lesen
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)

