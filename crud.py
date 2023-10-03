from sqlalchemy.orm import Session
from passlib.context import CryptContext
from schemas import *
from models import *
from sqlalchemy import asc, desc, text
from typing import List, Tuple
import urllib.parse
import json


def get_food(db: Session, food_id: int):
    food_item = db.query(Food).filter(Food.id == food_id).first()
    if not food_item:
        return None
    return food_item


def get_foods_by_name(db: Session, food_name: str, skip: int = 0, limit: int = 5):
    food_items = (
        db.query(Food)
        .filter(text("MATCH (name) AGAINST (:food_name)"))
        .params(food_name=food_name)
        .offset(skip)
        .limit(limit)
        .all()
    )

    # 총 음식 개수를 계산
    total_count = (
        db.query(Food)
        .filter(text("MATCH (name) AGAINST (:food_name)"))
        .params(food_name=food_name)
        .count()
    )

    if not food_items:
        return None, total_count
    return food_items, total_count


def get_foods(db: Session, skip: int = 0, limit: int = 100):
    foods = db.query(Food).offset(skip).limit(limit).all()
    total = db.query(Food).count()
    return foods, total


def create_food(db: Session, food: FoodCreate):
    db_food = Food(
        name=food.name,
        category_id=food.category_id,
        brand_id=food.brand_id,
        energy=food.energy,
        protein=food.protein,
        fat=food.fat,
        carbohydrate=food.carbohydrate,
        sugar=food.sugar,
        sodium=food.sodium,
        cholesterol=food.cholesterol,
        saturate_fat=food.saturate_fat,
        trans_fat=food.trans_fat,
        hydrate=food.hydrate,
        saccharose=food.saccharose,
        glucose=food.glucose,
        fructose=food.fructose,
        lactose=food.lactose,
        maltose=food.maltose,
        dietary_fiber=food.dietary_fiber,
        calcium=food.calcium,
        iron=food.iron,
        magnesium=food.magnesium,
        phosphorus=food.phosphorus,
        kalium=food.kalium,
        zinc=food.zinc,
        copper=food.copper,
        manganese=food.manganese,
        selenium=food.selenium,
        retinol=food.retinol,
        beta_carotene=food.beta_carotene,
        vitamin_D3=food.vitamin_D3,
        tocopherol=food.tocopherol,
        tocotrienols=food.tocotrienols,
        vitamin_B1=food.vitamin_B1,
        vitamin_B2=food.vitamin_B2,
        niacin=food.niacin,
        folate=food.folate,
        vitamin_B12=food.vitamin_B12,
        vitamin_C=food.vitamin_C,
        amino_acid=food.amino_acid,
        isoleucine=food.isoleucine,
        leucine=food.leucine,
        lysine=food.lysine,
        methionine=food.methionine,
        phenylalanine=food.phenylalanine,
        threonine=food.threonine,
        valine=food.valine,
        histidine=food.histidine,
        arginine=food.arginine,
        tyrosine=food.tyrosine,
        cysteine=food.cysteine,
        alanine=food.alanine,
        aspartic_acid=food.aspartic_acid,
        glutamic_acid=food.glutamic_acid,
        glycine=food.glycine,
        proline=food.proline,
        serine=food.serine,
        butyric_acid=food.butyric_acid,
        caproic_acid=food.caproic_acid,
        caprylic_acid=food.caprylic_acid,
        capric_acid=food.capric_acid,
        lauric_acid=food.lauric_acid,
        myristic_acid=food.myristic_acid,
        palmitic_acid=food.palmitic_acid,
        stearic_acid=food.stearic_acid,
        arachidic_acid=food.arachidic_acid,
        myristoleic_acid=food.myristoleic_acid,
        palmitoleic_acid=food.palmitoleic_acid,
        oleic_acid=food.oleic_acid,
        vaccenic_acid=food.vaccenic_acid,
        gadoleic_acid=food.gadoleic_acid,
        linoleic_acid=food.linoleic_acid,
        alpha_linolenic_acid=food.alpha_linolenic_acid,
        gamma_linolenic_acid=food.gamma_linolenic_acid,
        eicosadienoic_acid=food.eicosadienoic_acid,
        arachidonic_acid=food.arachidonic_acid,
        eicosatrienoic_acid=food.eicosatrienoic_acid,
        eicosapentaenoic_acid=food.eicosapentaenoic_acid,
        docosapentaenoic_acid=food.docosapentaenoic_acid,
        docosahexaenoic_acid=food.docosahexaenoic_acid,
        trans_oleic_acid=food.trans_oleic_acid,
        trans_linoleic_acid=food.trans_linoleic_acid,
        trans_linolenic_acid=food.trans_linolenic_acid,
        ash=food.ash,
        caffeine=food.caffeine,
        sugar_alcohol=food.sugar_alcohol,
        erythritol=food.erythritol,
        iodine=food.iodine,
        chloride=food.chloride,
        vitamin_D=food.vitamin_D,
        vitamin_D1=food.vitamin_D1,
        vitamin_E=food.vitamin_E,
        vitamin_K=food.vitamin_K,
        vitamin_K1=food.vitamin_K1,
        vitamin_K2=food.vitamin_K2,
        pantothenic_acid=food.pantothenic_acid,
        vitamin_B6=food.vitamin_B6,
        biotin=food.biotin,
        choline=food.choline,
        tryptophan=food.tryptophan,
        taurine=food.taurine,
        omega_3_fatty_acids=food.omega_3_fatty_acids,
        total_unsaturated_fats=food.total_unsaturated_fats,
    )
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food


def update_food(db: Session, food_id: int, food_data: dict):
    food_item = db.query(Food).filter(Food.id == food_id).first()
    if not food_item:
        return None

    for key, value in food_data.items():
        setattr(food_item, key, value)

    db.commit()
    db.refresh(food_item)
    return food_item


def delete_food(db: Session, food_id: int):
    food_item = db.query(Food).filter(Food.id == food_id).first()
    if not food_item:
        return None

    db.delete(food_item)
    db.commit()
    return food_item


def get_category(db: Session, category_id: int):
    category_item = db.query(Category).filter(Category.id == category_id).first()
    if not category_item:
        return None
    return category_item


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Category).offset(skip).limit(limit).all()


def get_category_with_foods(
    db: Session,
    category_id: int,
    skip: int,
    limit: int,
    food_name: Optional[str] = None,
    sort_criteria: Optional[SortCriteria] = None,
):
    category = db.query(Category).filter(Category.id == category_id).first()

    if not category:
        return None, 0

    foods_query = db.query(Food).filter(Food.category_id == category_id)

    # Searching by food_name
    if food_name:
        foods_query = foods_query.filter(
            text("MATCH (name) AGAINST (:food_name)")
        ).params(food_name=food_name)

    # Sorting
    if sort_criteria:
        for sort_item in sort_criteria.sort:
            column = getattr(Food, sort_item.column, None)
            if column:
                if sort_item.order == "desc":
                    column = column.desc()
                foods_query = foods_query.order_by(column)

    foods = foods_query.offset(skip).limit(limit).all()
    total = foods_query.count()
    category.foods = foods

    return category, total


def create_category(db: Session, category: CategoryCreate):
    db_category = Category(
        name=category.name,
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def update_category(db: Session, category_id: int, category_data: dict):
    category_item = db.query(Category).filter(Category.id == category_id).first()
    if not category_item:
        return None

    for key, value in category_data.items():
        setattr(category_item, key, value)

    db.commit()
    db.refresh(category_item)
    return category_item


def delete_category(db: Session, category_id: int):
    category_item = db.query(Category).filter(Category.id == category_id).first()
    if not category_item:
        return None

    db.delete(category_item)
    db.commit()
    return category_item


def get_brand(db: Session, brand_id: int):
    brand_item = db.query(Brand).filter(Brand.id == brand_id).first()
    if not brand_item:
        return None
    return brand_item


def get_brands(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Brand).offset(skip).limit(limit).all()


def get_brand_with_foods(
    db: Session,
    brand_id: int,
    skip: int,
    limit: int,
    food_name: Optional[str] = None,
    sort_criteria: Optional[SortCriteria] = None,
):
    brand = db.query(Brand).filter(Brand.id == brand_id).first()

    if not brand:
        return None, 0

    foods_query = db.query(Food).filter(Food.brand_id == brand_id)

    # Searching by food_name
    if food_name:
        foods_query = foods_query.filter(
            text("MATCH (name) AGAINST (:food_name)")
        ).params(food_name=food_name)

    # Sorting
    if sort_criteria:
        for sort_item in sort_criteria.sort:
            column = getattr(Food, sort_item.column, None)
            if column:
                if sort_item.order == "desc":
                    column = column.desc()
                foods_query = foods_query.order_by(column)

    foods = foods_query.offset(skip).limit(limit).all()
    total = foods_query.count()
    brand.foods = foods

    return brand, total


def create_brand(db: Session, brand: BrandCreate):
    db_brand = Brand(
        name=brand.name,
    )
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand


def update_brand(db: Session, brand_id: int, brand_data: dict):
    brand_item = db.query(Brand).filter(Brand.id == brand_id).first()
    if not brand_item:
        return None

    for key, value in brand_data.items():
        setattr(brand_item, key, value)

    db.commit()
    db.refresh(brand_item)
    return brand_item


def delete_brand(db: Session, brand_id: int):
    brand_item = db.query(Brand).filter(Brand.id == brand_id).first()
    if not brand_item:
        return None

    db.delete(brand_item)
    db.commit()
    return brand_item


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 0):
    return db.query(User).offset(skip).limit(limit).all()


def update_user(db: Session, username: str, user_data: UserUpdate):
    user_item = db.query(User).filter(User.username == username).first()
    if not user_item:
        return None

    for key, value in user_data.dict().items():
        if key == "password":
            hashed_password = pwd_context.hash(value)
            setattr(user_item, "hashed_password", hashed_password)
        else:
            setattr(user_item, key, value)

    db.commit()
    db.refresh(user_item)
    return user_item


def delete_user(db: Session, username: str):
    user_item = db.query(User).filter(User.username == username).first()
    if not user_item:
        return None

    db.delete(user_item)
    db.commit()
    return user_item


def get_sorted_data(
    db: Session,
    skip: int,
    limit: int,
    sort_criteria: SortCriteria,
    food_name: Optional[str] = None,
):
    query = db.query(Food)

    if food_name:
        query = query.filter(text("MATCH (name) AGAINST (:food_name)")).params(
            food_name=food_name
        )

    for sort_item in sort_criteria.sort:
        column = getattr(Food, sort_item.column, None)
        if column:
            if sort_item.order == "desc":
                query = query.order_by(column.desc())
            else:
                query = query.order_by(column)

    items = query.offset(skip).limit(limit).all()
    total = query.count()

    return items, total


def next_page(skip: int, limit: int) -> int:
    return skip + limit


def filter_fields(data, fields: List[str]):
    if not fields:
        return data
    return [{field: getattr(item, field, None) for field in fields} for item in data]
