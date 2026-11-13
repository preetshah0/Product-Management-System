import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database connection URL with fallback to local postgres
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:root@localhost:5432/product")
engine = create_engine(DATABASE_URL)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
