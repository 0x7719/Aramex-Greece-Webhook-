from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "Aramex Greece Webhook Online"
    }


@app.post("/webhook/daily")
async def daily_webhook(request: Request):

    payload = await request.json()

    print("RECEIVED:")
    print(payload)

    return {
        "received": True,
        "payload": payload
    }
