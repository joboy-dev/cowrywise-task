from pydantic_settings import BaseSettings
from decouple import config
from pathlib import Path


# Use this to build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    """ Class to hold application's config values."""

    PYTHON_ENV: str = config("PYTHON_ENV")
    SECRET_KEY: str = config("SECRET_KEY")
    ALGORITHM: str = config("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = config("ACCESS_TOKEN_EXPIRE_MINUTES")
    JWT_REFRESH_EXPIRY: int = config("JWT_REFRESH_EXPIRY")

    # Database configurations
    DB_TYPE: str = config("DB_TYPE")
    
    ADMIN_DB_HOST: str = config("ADMIN_DB_HOST")
    ADMIN_DB_PORT: int = config("ADMIN_DB_PORT", cast=int)
    ADMIN_DB_USER: str = config("ADMIN_DB_USER")
    ADMIN_DB_PASSWORD: str = config("ADMIN_DB_PASSWORD")
    ADMIN_DB_NAME: str = config("ADMIN_DB_NAME")
    ADMIN_DB_URL: str = config("ADMIN_DB_URL") 

    FE_DB_HOST: str = config("FE_DB_HOST")
    FE_DB_PORT: int = config("FE_DB_PORT", cast=int)
    FE_DB_USER: str = config("FE_DB_USER")
    FE_DB_PASSWORD: str = config("FE_DB_PASSWORD")
    FE_DB_NAME: str = config("FE_DB_NAME")
    FE_DB_URL: str = config("FE_DB_URL") 

    ADMIN_APP_URL: str = config("ADMIN_APP_URL") 
    FE_APP_URL: str = config("FE_APP_URL") 


settings = Settings()
