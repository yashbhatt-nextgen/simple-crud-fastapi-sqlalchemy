from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy import select
from models import IMSICount
from schema import UserIMSIData
from database import SessionLocal
import traceback
from sqlalchemy.orm import Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()


@app.get('/')
async def home():
    return {"message":"APP is Running!!!!!!"}


@app.get('/get-user-data')
async def get_all_data(db: Session = Depends(get_db)):
    try:
        all_data = db.query(IMSICount).offset(0).limit(10).all()
        return {"data": all_data}
    except Exception as e:
        print(f"Exception -------> {str(e)}")
        traceback.print_exc()
        return {"message": str(e)}
        

@app.post('/add-data')
async def add_mapping_data(user_data: UserIMSIData, db: Session = Depends(get_db)):
    try:
        data_instance = IMSICount(**user_data.model_dump())
        
        db.add(data_instance)
        db.commit()
        
        return {"message": "Data Added Successfully"}
    except Exception as e:
        print(f"Exception ----------> {str(e)}")
        traceback.print_exc()
        return {"message": str(e)}
    
    
