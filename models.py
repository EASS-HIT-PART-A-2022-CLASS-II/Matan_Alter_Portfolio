from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric

from database import Base


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    openprice = Column(Numeric(10, 2))
    lastprice = Column(Numeric(10, 2))
    lowprice = Column(Numeric(10, 2))
    highprice = Column(Numeric(10, 2))
    changeusd = Column(Numeric(10, 2))
    changeprecent = Column(Numeric(10, 2))


