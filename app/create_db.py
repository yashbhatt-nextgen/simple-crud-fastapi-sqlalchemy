from database import Base,engine
from models import UserIMSIData

print("Creating database ....")

Base.metadata.create_all(engine)