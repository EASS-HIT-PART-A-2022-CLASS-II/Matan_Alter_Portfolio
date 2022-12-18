#pip install fastapi
#pip install uvicorn
#pip install yfinance
#pip install finnhub-python


import models
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from pydantic import BaseModel
from models import Stock
import finnhub

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


class StockRequest(BaseModel):
    symbol: str


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def home(request: Request):
    #stock screen dashboard - Homepage
    return templates.TemplateResponse("home.html", {
        "request": request
    })

def fetch_stock_data(id: int):
    db = SessionLocal()
    stock = db.query(Stock).filter(Stock.id == id).first()


    finnhub_client = finnhub.Client(api_key="cea6leaad3i831op8bv0cea6leaad3i831op8bvg")
    n = stock.symbol
    X_price = (finnhub_client.quote(n))
    stock.lastprice = X_price["c"]




    db.add(stock)
    db.commit()


@app.post("/stock")
async def create_stock(stock_request: StockRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    #create stock and save it to the DB

    stock = Stock()
    stock.symbol = stock_request.symbol

    db.add(stock)
    db.commit()

    background_tasks.add_task(fetch_stock_data, stock.id)

    return{
        "code": "success",
        "message": "stock created"
    }
