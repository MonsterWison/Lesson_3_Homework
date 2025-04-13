from sqlmodel import SQLModel, Field, create_engine
from typing import Optional
import json

class Furniture(SQLModel, table=True):
    product_id: str = Field(primary_key=True)
    category: str
    brand: str
    name: str
    color: str
    style: str
    materials: str
    length: float
    width: float
    height: float
    weight: float
    serial_no: int
    country_of_origin: str
    price: float
    warranty: int
    assembly_require: bool = Field(default=False)
    have_stock: bool
    qc: bool

class Wardrobe(SQLModel, table=True):
    product_id: str = Field(primary_key=True, foreign_key="furniture.product_id")
    category: str = Field(default="Wardrobes")
    depth_length: float
    hanging: bool
    structure: str
    function_features: str
    installation: str
    load_capacity: str
    advanced_technologies: str  # 存儲JSON字符串

class Desk(SQLModel, table=True):
    product_id: str = Field(primary_key=True, foreign_key="furniture.product_id")
    category: str = Field(default="Desk")
    design_features: str
    ergonomics: str
    additional_options: str

class TV_Cabinet(SQLModel, table=True):
    product_id: str = Field(primary_key=True, foreign_key="furniture.product_id")
    category: str = Field(default="TV_Cabinet")
    design_features: str
    compatibility: str
    additional_features: str

engine = create_engine("sqlite:///ikea_furniture.db")
SQLModel.metadata.create_all(engine)
