from sqlalchemy import Column, ForeignKey, String, Float, Integer, Boolean
from sqlalchemy.orm import relationship

from database import Base


class Category(Base):
    __tablename__ = "Category"

    id = Column(
        Integer, primary_key=True, index=True, autoincrement=True, nullable=False
    )
    name = Column(String(100), unique=True, nullable=False)

    foods = relationship("Food", back_populates="category")


class Brand(Base):
    __tablename__ = "Brand"

    id = Column(
        Integer, primary_key=True, index=True, autoincrement=True, nullable=False
    )
    name = Column(String(100), unique=True, nullable=False)

    foods = relationship("Food", back_populates="brand")


class Food(Base):
    __tablename__ = "Food"

    id = Column(
        Integer, primary_key=True, index=True, autoincrement=True, nullable=False
    )
    name = Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=True)
    brand_id = Column(Integer, ForeignKey(Brand.id), nullable=True)

    energy = Column(Float, nullable=True)
    protein = Column(Float, nullable=True)
    fat = Column(Float, nullable=True)
    carbohydrate = Column(Float, nullable=True)
    sugar = Column(Float, nullable=True)
    sodium = Column(Float, nullable=True)
    cholesterol = Column(Float, nullable=True)
    saturate_fat = Column(Float, nullable=True)
    trans_fat = Column(Float, nullable=True)
    hydrate = Column(Float, nullable=True)
    saccharose = Column(Float, nullable=True)
    glucose = Column(Float, nullable=True)
    fructose = Column(Float, nullable=True)
    lactose = Column(Float, nullable=True)
    maltose = Column(Float, nullable=True)
    dietary_fiber = Column(Float, nullable=True)
    calcium = Column(Float, nullable=True)
    iron = Column(Float, nullable=True)
    magnesium = Column(Float, nullable=True)
    phosphorus = Column(Float, nullable=True)
    kalium = Column(Float, nullable=True)
    zinc = Column(Float, nullable=True)
    copper = Column(Float, nullable=True)
    manganese = Column(Float, nullable=True)
    selenium = Column(Float, nullable=True)
    retinol = Column(Float, nullable=True)
    beta_carotene = Column(Float, nullable=True)
    vitamin_D3 = Column(Float, nullable=True)
    tocopherol = Column(Float, nullable=True)
    tocotrienols = Column(Float, nullable=True)
    vitamin_B1 = Column(Float, nullable=True)
    vitamin_B2 = Column(Float, nullable=True)
    niacin = Column(Float, nullable=True)
    folate = Column(Float, nullable=True)
    vitamin_B12 = Column(Float, nullable=True)
    vitamin_C = Column(Float, nullable=True)
    amino_acid = Column(Float, nullable=True)
    isoleucine = Column(Float, nullable=True)
    leucine = Column(Float, nullable=True)
    lysine = Column(Float, nullable=True)
    methionine = Column(Float, nullable=True)
    phenylalanine = Column(Float, nullable=True)
    threonine = Column(Float, nullable=True)
    valine = Column(Float, nullable=True)
    histidine = Column(Float, nullable=True)
    arginine = Column(Float, nullable=True)
    tyrosine = Column(Float, nullable=True)
    cysteine = Column(Float, nullable=True)
    alanine = Column(Float, nullable=True)
    aspartic_acid = Column(Float, nullable=True)
    glutamic_acid = Column(Float, nullable=True)
    glycine = Column(Float, nullable=True)
    proline = Column(Float, nullable=True)
    serine = Column(Float, nullable=True)
    butyric_acid = Column(Float, nullable=True)
    caproic_acid = Column(Float, nullable=True)
    caprylic_acid = Column(Float, nullable=True)
    capric_acid = Column(Float, nullable=True)
    lauric_acid = Column(Float, nullable=True)
    myristic_acid = Column(Float, nullable=True)
    palmitic_acid = Column(Float, nullable=True)
    stearic_acid = Column(Float, nullable=True)
    arachidic_acid = Column(Float, nullable=True)
    myristoleic_acid = Column(Float, nullable=True)
    palmitoleic_acid = Column(Float, nullable=True)
    oleic_acid = Column(Float, nullable=True)
    vaccenic_acid = Column(Float, nullable=True)
    gadoleic_acid = Column(Float, nullable=True)
    linoleic_acid = Column(Float, nullable=True)
    alpha_linolenic_acid = Column(Float, nullable=True)
    gamma_linolenic_acid = Column(Float, nullable=True)
    eicosadienoic_acid = Column(Float, nullable=True)
    arachidonic_acid = Column(Float, nullable=True)
    eicosatrienoic_acid = Column(Float, nullable=True)
    eicosapentaenoic_acid = Column(Float, nullable=True)
    docosapentaenoic_acid = Column(Float, nullable=True)
    docosahexaenoic_acid = Column(Float, nullable=True)
    trans_oleic_acid = Column(Float, nullable=True)
    trans_linoleic_acid = Column(Float, nullable=True)
    trans_linolenic_acid = Column(Float, nullable=True)
    ash = Column(Float, nullable=True)
    caffeine = Column(Float, nullable=True)
    sugar_alcohol = Column(Float, nullable=True)
    erythritol = Column(Float, nullable=True)
    iodine = Column(Float, nullable=True)
    chloride = Column(Float, nullable=True)
    vitamin_D = Column(Float, nullable=True)
    vitamin_D1 = Column(Float, nullable=True)
    vitamin_E = Column(Float, nullable=True)
    vitamin_K = Column(Float, nullable=True)
    vitamin_K1 = Column(Float, nullable=True)
    vitamin_K2 = Column(Float, nullable=True)
    pantothenic_acid = Column(Float, nullable=True)
    vitamin_B6 = Column(Float, nullable=True)
    biotin = Column(Float, nullable=True)
    choline = Column(Float, nullable=True)
    tryptophan = Column(Float, nullable=True)
    taurine = Column(Float, nullable=True)
    omega_3_fatty_acids = Column(Float, nullable=True)
    total_unsaturated_fats = Column(Float, nullable=True)

    category = relationship("Category", back_populates="foods")
    brand = relationship("Brand", back_populates="foods")


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(500))
    is_active = Column(Boolean, default=True)
