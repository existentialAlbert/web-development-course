from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "homework-1"

    APP_HOST: str = "localhost"
    APP_PORT: int = 8080

    DEBUG: bool = True
    LOGLEVEL: str = "DEBUG"

    class Config:
        env_file = ".env"


settings = Settings()
