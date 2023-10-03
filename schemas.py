from pydantic import BaseModel, validator, Field
from typing import Optional, List


class Pagination(BaseModel):
    skip: int
    limit: int
    total: int
    items: int


class FoodID(BaseModel):
    id: int


class FoodBase(BaseModel):
    name: str
    category_id: Optional[int] = Field(None)
    brand_id: Optional[int] = Field(None)
    energy: Optional[float] = Field(None)
    protein: Optional[float] = Field(None)
    fat: Optional[float] = Field(None)
    carbohydrate: Optional[float] = Field(None)
    sugar: Optional[float] = Field(None)
    sodium: Optional[float] = Field(None)
    cholesterol: Optional[float] = Field(None)
    saturate_fat: Optional[float] = Field(None)
    trans_fat: Optional[float] = Field(None)
    hydrate: Optional[float] = Field(None)
    saccharose: Optional[float] = Field(None)
    glucose: Optional[float] = Field(None)
    fructose: Optional[float] = Field(None)
    lactose: Optional[float] = Field(None)
    maltose: Optional[float] = Field(None)
    dietary_fiber: Optional[float] = Field(None)
    calcium: Optional[float] = Field(None)
    iron: Optional[float] = Field(None)
    magnesium: Optional[float] = Field(None)
    phosphorus: Optional[float] = Field(None)
    kalium: Optional[float] = Field(None)
    zinc: Optional[float] = Field(None)
    copper: Optional[float] = Field(None)
    manganese: Optional[float] = Field(None)
    selenium: Optional[float] = Field(None)
    retinol: Optional[float] = Field(None)
    beta_carotene: Optional[float] = Field(None)
    vitamin_D3: Optional[float] = Field(None)
    tocopherol: Optional[float] = Field(None)
    tocotrienols: Optional[float] = Field(None)
    vitamin_B1: Optional[float] = Field(None)
    vitamin_B2: Optional[float] = Field(None)
    niacin: Optional[float] = Field(None)
    folate: Optional[float] = Field(None)
    vitamin_B12: Optional[float] = Field(None)
    vitamin_C: Optional[float] = Field(None)
    amino_acid: Optional[float] = Field(None)
    isoleucine: Optional[float] = Field(None)
    leucine: Optional[float] = Field(None)
    lysine: Optional[float] = Field(None)
    methionine: Optional[float] = Field(None)
    phenylalanine: Optional[float] = Field(None)
    threonine: Optional[float] = Field(None)
    valine: Optional[float] = Field(None)
    histidine: Optional[float] = Field(None)
    arginine: Optional[float] = Field(None)
    tyrosine: Optional[float] = Field(None)
    cysteine: Optional[float] = Field(None)
    alanine: Optional[float] = Field(None)
    aspartic_acid: Optional[float] = Field(None)
    glutamic_acid: Optional[float] = Field(None)
    glycine: Optional[float] = Field(None)
    proline: Optional[float] = Field(None)
    serine: Optional[float] = Field(None)
    butyric_acid: Optional[float] = Field(None)
    caproic_acid: Optional[float] = Field(None)
    caprylic_acid: Optional[float] = Field(None)
    capric_acid: Optional[float] = Field(None)
    lauric_acid: Optional[float] = Field(None)
    myristic_acid: Optional[float] = Field(None)
    palmitic_acid: Optional[float] = Field(None)
    stearic_acid: Optional[float] = Field(None)
    arachidic_acid: Optional[float] = Field(None)
    myristoleic_acid: Optional[float] = Field(None)
    palmitoleic_acid: Optional[float] = Field(None)
    oleic_acid: Optional[float] = Field(None)
    vaccenic_acid: Optional[float] = Field(None)
    gadoleic_acid: Optional[float] = Field(None)
    linoleic_acid: Optional[float] = Field(None)
    alpha_linolenic_acid: Optional[float] = Field(None)
    gamma_linolenic_acid: Optional[float] = Field(None)
    eicosadienoic_acid: Optional[float] = Field(None)
    arachidonic_acid: Optional[float] = Field(None)
    eicosatrienoic_acid: Optional[float] = Field(None)
    eicosapentaenoic_acid: Optional[float] = Field(None)
    docosapentaenoic_acid: Optional[float] = Field(None)
    docosahexaenoic_acid: Optional[float] = Field(None)
    trans_oleic_acid: Optional[float] = Field(None)
    trans_linoleic_acid: Optional[float] = Field(None)
    trans_linolenic_acid: Optional[float] = Field(None)
    ash: Optional[float] = Field(None)
    caffeine: Optional[float] = Field(None)
    sugar_alcohol: Optional[float] = Field(None)
    erythritol: Optional[float] = Field(None)
    iodine: Optional[float] = Field(None)
    chloride: Optional[float] = Field(None)
    vitamin_D: Optional[float] = Field(None)
    vitamin_D1: Optional[float] = Field(None)
    vitamin_E: Optional[float] = Field(None)
    vitamin_K: Optional[float] = Field(None)
    vitamin_K1: Optional[float] = Field(None)
    vitamin_K2: Optional[float] = Field(None)
    pantothenic_acid: Optional[float] = Field(None)
    vitamin_B6: Optional[float] = Field(None)
    biotin: Optional[float] = Field(None)
    choline: Optional[float] = Field(None)
    tryptophan: Optional[float] = Field(None)
    taurine: Optional[float] = Field(None)
    omega_3_fatty_acids: Optional[float] = Field(None)
    total_unsaturated_fats: Optional[float] = Field(None)


class FoodCreate(FoodBase):
    pass


class FoodGet(FoodBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True


class PaginatedFoodGet(BaseModel):
    pagination: Pagination
    items: List[FoodGet]

    class Config:
        orm_mode = True


class CategoryID(BaseModel):
    id: int


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryGet(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class PaginatedGetWithFoods(BaseModel):
    pagination: Pagination
    id: int
    name: str
    foods: List[FoodGet]

    class Config:
        orm_mode = True


class BrandID(BaseModel):
    id: int


class BrandBase(BaseModel):
    name: str


class BrandCreate(BrandBase):
    pass


class BrandGet(BrandBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserGet(UserBase):
    id: int
    is_active: bool | None = Field(None)

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    password: Optional[str]


class DeleteSchema(BaseModel):
    message: str
    id: int


class DeleteUserSchema(BaseModel):
    message: str
    username: str


class SortItem(BaseModel):
    column: str
    order: str

    @validator("column")
    def validate_column(cls, column):
        ALLOWED_COLUMNS = [
            "energy",
            "protein",
            "fat",
            "carbohydrate",
            "sugar",
            "sodium",
            "cholesterol",
            "saturate_fat",
            "trans_fat",
            "hydrate",
            "saccharose",
            "glucose",
            "fructose",
            "lactose",
            "maltose",
            "dietary_fiber",
            "calcium",
            "iron",
            "magnesium",
            "phosphorus",
            "kalium",
            "zinc",
            "copper",
            "manganese",
            "selenium",
            "retinol",
            "beta_carotene",
            "vitamin_D3",
            "tocopherol",
            "tocotrienols",
            "vitamin_B1",
            "vitamin_B2",
            "niacin",
            "folate",
            "vitamin_B12",
            "vitamin_C",
            "amino_acid",
            "isoleucine",
            "leucine",
            "lysine",
            "methionine",
            "phenylalanine",
            "threonine",
            "valine",
            "histidine",
            "arginine",
            "tyrosine",
            "cysteine",
            "alanine",
            "aspartic_acid",
            "glutamic_acid",
            "glycine",
            "proline",
            "serine",
            "butyric_acid",
            "caproic_acid",
            "caprylic_acid",
            "capric_acid",
            "lauric_acid",
            "myristic_acid",
            "palmitic_acid",
            "stearic_acid",
            "arachidic_acid",
            "myristoleic_acid",
            "palmitoleic_acid",
            "oleic_acid",
            "vaccenic_acid",
            "gadoleic_acid",
            "linoleic_acid",
            "alpha_linolenic_acid",
            "gamma_linolenic_acid",
            "eicosadienoic_acid",
            "arachidonic_acid",
            "eicosatrienoic_acid",
            "eicosapentaenoic_acid",
            "docosapentaenoic_acid",
            "docosahexaenoic_acid",
            "trans_oleic_acid",
            "trans_linoleic_acid",
            "trans_linolenic_acid",
            "ash",
            "caffeine",
            "sugar_alcohol",
            "erythritol",
            "iodine",
            "chloride",
            "vitamin_D",
            "vitamin_D1",
            "vitamin_E",
            "vitamin_K",
            "vitamin_K1",
            "vitamin_K2",
            "pantothenic_acid",
            "vitamin_B6",
            "biotin",
            "choline",
            "tryptophan",
            "taurine",
            "omega_3_fatty_acids",
            "total_unsaturated_fats",
        ]
        RESTRICTED_COLUMNS = [
            "name",
            "category_id",
            "brand_id",
        ]

        if column in RESTRICTED_COLUMNS:
            raise ValueError(f"{column} is not allowed for sorting")
        elif column not in ALLOWED_COLUMNS:
            raise ValueError(f"Invalid column: {column}")

        return column

    @validator("order")
    def validate_order(cls, order):
        ALLOWED_SORT_ORDERS = ["asc", "desc"]
        if order not in ALLOWED_SORT_ORDERS:
            raise ValueError(f"Invalid order: {order}")
        return order


class SortCriteria(BaseModel):
    sort: List[SortItem]
