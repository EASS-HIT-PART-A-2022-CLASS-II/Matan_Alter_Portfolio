from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric

from database import Base


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    numofshares = Column(Numeric(10, 2))
    avgprice = Column(Numeric(10, 2))
    lastprice = Column(Numeric(10, 2))


