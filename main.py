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

    shipment_number = payload.get("shipment_number")
    awb = payload.get("ext_number")

    data = payload.get("data", {})
    status_id = data.get("status_id")
    status_name = data.get("status_name")
    driver_name = data.get("driver_name")
    comments = data.get("comments")
    timestamp = data.get("timestamp")

    print("DAILY WEBHOOK RECEIVED")
    print("Shipment Number:", shipment_number)
    print("AWB:", awb)
    print("Status ID:", status_id)
    print("Status Name:", status_name)
    print("Driver:", driver_name)
    print("Comments:", comments)
    print("Timestamp:", timestamp)

    return {
        "received": True,
        "shipment_number": shipment_number,
        "awb": awb,
        "status_id": status_id,
        "comments": comments,
        "timestamp": timestamp
    }
