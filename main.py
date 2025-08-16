from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List
import random

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

size_prices = {
    "small": 250,
    "medium": 400,
    "large": 650
}
topping_price = 160

@app.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/order", response_class=HTMLResponse)
def post_order(
    request: Request,
    size: str = Form(...),
    toppings: List[str] = Form([])
):
   
    base_price = size_prices[size]
    total_price = base_price + len(toppings) * topping_price
    delivery_time = f"{random.randint(30, 45)} minutes"

    result = {
        "pizza_size": size,
        "toppings": toppings,
        "total_price": f"₹{total_price:.2f}",
        "estimated_delivery_time": delivery_time,
        "status": " Your Pizza is being prepared! "
    }

    return templates.TemplateResponse("index.html", {"request": request, "result": result})
