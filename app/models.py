from sqlalchemy import Column, Integer
from database import Base


class IMSICount(Base):
    __tablename__ = 'imsi_per_account'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    account_number = Column(Integer)
    imsi_count = Column(Integer)
    
    def __init__(self, account_number: int, imsi_count: int):
        self.account_number = account_number
        self.imsi_count = imsi_count