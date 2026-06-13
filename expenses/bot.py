import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_CHAT_ID = os.getenv("BOT_CHAT_ID")

def send_budget_alert(category_name, spent, limit, month):
    print("SEND_BUDGET_ALERT CALLED")
    if not BOT_TOKEN or not BOT_CHAT_ID:
        print("Missing BOT_TOKEN or BOT_CHAT_ID")
        return

    message = (
        f'⚠️ Budget alert: "{category_name}" is over its monthly limit.\n'
        f"Spent {spent} / {limit} for {month}"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": BOT_CHAT_ID,
            "text": message
        }
    )
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)