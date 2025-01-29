from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random  # ✅ Wichtiger Import

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Datenmodell für Anfragen
class TradeRequest(BaseModel):
    coin: str
    timeframe: str  # z.B. "1h", "24h"

# Beispiel-Funktion für AI-Trading-Empfehlungen
def get_trade_recommendation(coin, timeframe):
    predictions = ["Buy", "Sell", "Hold"]
    return random.choice(predictions)  # Hier könnte dein AI-Modell die Entscheidung treffen

# API-Route für Vorhersagen
@app.post("/predict")
def predict_trade(data: TradeRequest):
    recommendation = get_trade_recommendation(data.coin, data.timeframe)
    return {"coin": data.coin, "timeframe": data.timeframe, "recommendation": recommendation}

# Falls das Skript direkt ausgeführt wird
if __name__ == "__main__":
import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Port von Render lesen
    uvicorn.run(app, host="0.0.0.0", port=port)
    
