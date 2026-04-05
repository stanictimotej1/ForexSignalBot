import os

PAIRS = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD"]
TIMEFRAMES = ["15min"]

ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")

EMA_FAST = 50
EMA_SLOW = 200
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

MIN_CONFIRMATIONS = 3
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = "forex_bot.log"

def validate_config():
    required = {
        "ALPHA_VANTAGE_API_KEY": ALPHA_VANTAGE_API_KEY,
        "SENDGRID_API_KEY": SENDGRID_API_KEY,
        "EMAIL_FROM": EMAIL_FROM,
        "EMAIL_TO": EMAIL_TO,
    }
    missing = [k for k, v in required.items() if not v]
    if missing:
        raise ValueError(f"Manjkajo spremenljivke: {', '.join(missing)}")
