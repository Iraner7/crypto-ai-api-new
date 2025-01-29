from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
