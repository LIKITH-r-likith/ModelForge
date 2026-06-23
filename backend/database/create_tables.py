from connection import engine 
from model import Base
print("Creating Tables")
Base.metadata.create_all(bind = engine)
print("Tables created successully") 
