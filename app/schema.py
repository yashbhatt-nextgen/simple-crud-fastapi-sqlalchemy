from pydantic import BaseModel
from models import IMSICount

class UserIMSIData(BaseModel):
    account_number: int
    imsi_count: int
    
    
    
    

