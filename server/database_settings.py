import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
load_dotenv()

SERVER_POSTGRES_CONNECTION = os.getenv("SERVER_POSTGRES_CONNECTION", False)


# SERVER_POSTGRES_CONNECTION="postgresql://postgres:postgres@postgres:5432/postgres"

engine = create_engine(SERVER_POSTGRES_CONNECTION, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
