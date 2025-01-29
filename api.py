from fastapi import FastAPI
from pydantic import BaseModel
import random  # Beispiel für eine simple AI-Logik (du kannst hier dein Modell laden)

app = FastAPI()

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
