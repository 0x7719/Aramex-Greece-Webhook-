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

    daily_shipment_number = payload.get("shipment_number")
    aramex_awb = payload.get("ext_number")

    data = payload.get("data", {})
    status_id = data.get("status_id")
    status_name = data.get("status_name")
    driver_name = data.get("driver_name")
    comments = data.get("comments")
    timestamp = data.get("timestamp")

    pinumber = None
    problem_code = None
    comment1 = None

    if status_id == "17":
        pinumber = "SH033"
        problem_code = "A16"
        comment1 = "Incorrect address - Address not found"

    print("DAILY WEBHOOK RECEIVED")
    print("Daily Shipment Number:", daily_shipment_number)
    print("Aramex AWB:", aramex_awb)
    print("Status ID:", status_id)
    print("Status Name:", status_name)
    print("Driver:", driver_name)
    print("Daily Comments:", comments)
    print("Daily Timestamp:", timestamp)
    print("Mapped PINumber:", pinumber)
    print("Mapped ProblemCode:", problem_code)
    print("Mapped Comment1:", comment1)

    return {
        "received": True,
        "daily_shipment_number": daily_shipment_number,
        "aramex_awb": aramex_awb,
        "status_id": status_id,
        "status_name": status_name,
        "driver_name": driver_name,
        "daily_comments": comments,
        "daily_timestamp": timestamp,
        "pinumber": pinumber,
        "problem_code": problem_code,
        "comment1": comment1
    }
