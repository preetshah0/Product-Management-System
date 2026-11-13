import logging
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import Sessionlocal, engine
import database_model
from models import Product

logger = logging.getLogger(__name__)

# Initial default product seed catalog
products = [
    Product(id=1, name="phone", description="Apple phone", price=99.0, quantity=10),
    Product(id=2, name="HeadPhone", description="Wireless Boat Headphone", price=199.0, quantity=5),
    Product(id=3, name="Airpods", description="Apple airpods", price=89.0, quantity=15),
    Product(id=4, name="Charger", description="phone charger", price=49.0, quantity=30),
    Product(id=5, name="SIM", description="Data SIM", price=50.0, quantity=50),
]


def init_db():
    """Seed the database with initial products if the table is empty."""
    db = Sessionlocal()
    try:
        count = db.query(database_model.Product).count()
        if count == 0:
            for product in products:
                db.add(database_model.Product(**product.model_dump()))
            db.commit()
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to seed database: {e}")
    finally:
        db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle manager for startup and shutdown tasks."""
    try:
        database_model.Base.metadata.create_all(bind=engine)
        init_db()
    except Exception as e:
        logger.warning(f"Could not connect to database on startup: {e}")
    yield


app = FastAPI(title="Product Management API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def greet():
    return {"message": "Welcome to the Server"}


@app.get("/products")
@app.get("/products/")
def get_products(db: Session = Depends(get_db)):
    db_products = db.query(database_model.Product).all()
    return db_products


@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return db_product


@app.post("/products", status_code=status.HTTP_201_CREATED)
@app.post("/products/", status_code=status.HTTP_201_CREATED)
def add_product(product: Product, db: Session = Depends(get_db)):
    existing = db.query(database_model.Product).filter(database_model.Product.id == product.id).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Product with ID {product.id} already exists"
        )
    new_product = database_model.Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity
    db.commit()
    db.refresh(db_product)
    return db_product


@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    db.delete(db_product)
    db.commit()
    return {"message": "Product removed successfully"}
