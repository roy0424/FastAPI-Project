from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from security import *
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session
from dependancies import get_db
import json
from urllib.parse import unquote
from pydantic import ValidationError, create_model
from typing import Any, Dict, List
from crud import *
from schemas import *
from database import *
import math

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/foods/", response_model=PaginatedFoodGet)
def get_foods_route(
    db: Session = Depends(get_db),
    sort: str = Query("", alias="sort"),
    skip: int = 0,
    limit: int = 100,
    food_name: Optional[str] = None,
):
    if food_name and sort == "":
        foods, total_items = get_foods_by_name(
            db, food_name=food_name, skip=skip, limit=limit
        )
        num_pages = math.ceil(total_items / limit)
        pagination_data = Pagination(
            skip=skip,
            limit=limit,
            total=num_pages,
            items=total_items,
        )
        response = PaginatedFoodGet(pagination=pagination_data, items=foods)
        return response

    if sort == "" and food_name is None:
        foods, total_items = get_foods(db, skip=skip, limit=limit)
        num_pages = math.ceil(total_items / limit)

        pagination_data = Pagination(
            skip=skip,
            limit=limit,
            total=num_pages,
            items=total_items,
        )
        response = PaginatedFoodGet(pagination=pagination_data, items=foods)
        return response
    sort_criteria = json.loads(sort)

    sort_criteria = SortCriteria(sort=[SortItem(**item) for item in sort_criteria])

    results, total_items = get_sorted_data(
        db,
        skip=skip,
        limit=limit,
        sort_criteria=sort_criteria,
        food_name=food_name,
    )
    num_pages = math.ceil(total_items / limit)

    pagination_data = Pagination(
        skip=skip,
        limit=limit,
        total=num_pages,
        items=total_items,
    )

    return PaginatedFoodGet(pagination=pagination_data, items=results)


@app.get("/food/{food_id}", response_model=FoodGet)
def read_food_route(food_id: int, db: Session = Depends(get_db)):
    food = get_food(db, food_id=food_id)
    if food is None:
        raise HTTPException(status_code=404, detail="Food Not Found")
    return food


@app.post("/food/create", response_model=FoodID)
def create_food_route(
    food: FoodCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return {"id": create_food(db, food=food).id}


@app.post("/food/update/{food_id}", response_model=FoodGet)
def update_food_route(
    food_id: int,
    food: FoodCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    updated_food = update_food(db, food_id, food.dict())
    if not updated_food:
        raise HTTPException(status_code=404, detail="Food Not Found")
    return updated_food


@app.post("/food/delete/{food_id}", response_model=DeleteSchema)
def delete_food_route(
    food_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    deleted_food = delete_food(db, food_id)
    if not deleted_food:
        return HTTPException(status_code=404, detail="Food not found")
    return {"message": "Food Deleted Successfully", "id": deleted_food.id}


@app.get("/categories/", response_model=List[CategoryGet])
def read_categories_route(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    categories = get_categories(db, skip=skip, limit=limit)
    return categories


@app.get("/category/{category_id}", response_model=CategoryGet)
def read_category_route(category_id: int, db: Session = Depends(get_db)):
    category = get_category(db, category_id=category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Brand Not Found")
    return category


@app.get("/category/{category_id}/foods", response_model=PaginatedGetWithFoods)
def get_category_with_foods_route(
    category_id: int,
    db: Session = Depends(get_db),
    sort: str = Query("", alias="sort"),
    skip: int = 0,
    limit: int = 100,
    food_name: Optional[str] = None,
):
    if food_name and sort == "":
        category, total_items = get_category_with_foods(
            db, category_id, skip, limit, food_name
        )
        if not category:
            return {"error": "Category not found"}
        num_pages = math.ceil(total_items / limit)

        pagination_data = Pagination(
            skip=skip,
            limit=limit,
            total=num_pages,
            items=total_items,
        )
        response = PaginatedGetWithFoods(
            pagination=pagination_data,
            id=category_id,
            name=category.name,
            foods=category.foods,
        )
        return response

    if sort == "" and food_name is None:
        category, total_items = get_category_with_foods(
            db, category_id, skip=skip, limit=limit
        )
        if not category:
            return {"error": "Category not found"}
        num_pages = math.ceil(total_items / limit)

        pagination_data = Pagination(
            skip=skip,
            limit=limit,
            total=num_pages,
            items=total_items,
        )
        response = PaginatedGetWithFoods(
            pagination=pagination_data,
            id=category_id,
            name=category.name,
            foods=category.foods,
        )
        return response
    sort_criteria = json.loads(sort)

    sort_criteria = SortCriteria(sort=[SortItem(**item) for item in sort_criteria])

    category, total_items = get_category_with_foods(
        db,
        category_id,
        skip=skip,
        limit=limit,
        sort_criteria=sort_criteria,
        food_name=food_name,
    )
    num_pages = math.ceil(total_items / limit)

    pagination_data = Pagination(
        skip=skip,
        limit=limit,
        total=num_pages,
        items=total_items,
    )
    response = PaginatedGetWithFoods(
        pagination=pagination_data,
        id=category_id,
        name=category.name,
        foods=category.foods,
    )
    return response


@app.post("/category/create", response_model=CategoryID)
def create_category_route(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return {"id": create_category(db, category=category).id}


@app.post("/category/update/{category_id}", response_model=CategoryGet)
def update_category_route(
    category_id: int,
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    updated_category = update_category(db, category_id, category.dict())
    if not updated_category:
        raise HTTPException(status_code=404, detail="Category Not Found")
    return updated_category


@app.post("/category/delete/{category_id}", response_model=DeleteSchema)
def delete_category_route(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    deleted_category = delete_category(db, category_id)
    if not deleted_category:
        return HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category Deleted Successfully", "id": deleted_category.id}


@app.get("/brands/", response_model=List[BrandGet])
def read_brands_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    brands = get_brands(db, skip=skip, limit=limit)
    return brands


@app.get("/brand/{brand_id}", response_model=BrandGet)
def read_brand_route(brand_id: int, db: Session = Depends(get_db)):
    brand = get_brand(db, brand_id=brand_id)
    if brand is None:
        raise HTTPException(status_code=404, detail="Brand Not Found")
    return brand


@app.get("/brand/{brand_id}/foods", response_model=PaginatedGetWithFoods)
def get_brand_with_foods_route(
    brand_id: int,
    db: Session = Depends(get_db),
    sort: str = Query("", alias="sort"),
    skip: int = 0,
    limit: int = 100,
    food_name: Optional[str] = None,
):
    if food_name and sort == "":
        brand, total_items = get_brand_with_foods(db, brand_id, skip, limit, food_name)
        if not brand:
            return {"error": "Brand not found"}
        num_pages = math.ceil(total_items / limit)

        pagination_data = Pagination(
            skip=skip,
            limit=limit,
            total=num_pages,
            items=total_items,
        )
        response = PaginatedGetWithFoods(
            pagination=pagination_data,
            id=brand_id,
            name=brand.name,
            foods=brand.foods,
        )
        return response

    if sort == "" and food_name is None:
        brand, total_items = get_brand_with_foods(db, brand_id, skip=skip, limit=limit)
        if not brand:
            return {"error": "Brand not found"}
        num_pages = math.ceil(total_items / limit)

        pagination_data = Pagination(
            skip=skip,
            limit=limit,
            total=num_pages,
            items=total_items,
        )
        response = PaginatedGetWithFoods(
            pagination=pagination_data,
            id=brand_id,
            name=brand.name,
            foods=brand.foods,
        )
        return response
    sort_criteria = json.loads(sort)

    sort_criteria = SortCriteria(sort=[SortItem(**item) for item in sort_criteria])

    brand, total_items = get_brand_with_foods(
        db,
        brand_id,
        skip=skip,
        limit=limit,
        sort_criteria=sort_criteria,
        food_name=food_name,
    )
    num_pages = math.ceil(total_items / limit)

    pagination_data = Pagination(
        skip=skip,
        limit=limit,
        total=num_pages,
        items=total_items,
    )

    response = PaginatedGetWithFoods(
        pagination=pagination_data,
        id=brand_id,
        name=brand.name,
        foods=brand.foods,
    )
    return response


@app.post("/brand/create", response_model=BrandID)
def create_brand_route(
    brand: BrandCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return create_brand(db, brand=brand)


@app.post("/brand/update/{brand_id}", response_model=BrandGet)
def update_brand_route(
    brand_id: int,
    brand: BrandCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    updated_brand = update_brand(db, brand_id, brand.dict())
    if not updated_brand:
        raise HTTPException(status_code=404, detail="Brand Not Found")
    return updated_brand


@app.post("/brand/delete/{brand_id}", response_model=DeleteSchema)
def delete_brand_route(
    brand_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    deleted_brand = delete_brand(db, brand_id)
    if not deleted_brand:
        return HTTPException(status_code=404, detail="Brand not found")
    return {"message": "Brand Deleted Successfully", "id": deleted_brand.id}


@app.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = get_user(db, username=form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect id or password")
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect id or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/user/me", response_model=None)
def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.post("/user/create", response_model=UserGet)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db=db, user=user)


@app.get("/users/", response_model=List[UserGet])
def read_users_route(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    users = get_users(db, skip=skip, limit=limit)
    return users


@app.get("/user/{username}", response_model=UserGet)
def read_user_route(
    username: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    db_user = get_user(db, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/user/update/{username}", response_model=UserGet)
def update_user_route(
    username: str,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    updated_user = update_user(db, username, user_data)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@app.post("/user/delete/{username}", response_model=DeleteUserSchema)
def delete_user_route(
    username: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    deleted_user = delete_user(db, username)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User Deleted Successfully", "username": deleted_user.username}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
