from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv(override=True)
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{os.getenv('username')}:{os.getenv('password')}@{os.getenv('server_ip')}:3306/rottentomatoes"
# SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root:banana@10.20.3.34:3306/rottentomatoes"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
