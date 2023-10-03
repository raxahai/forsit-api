import os

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ENV: str = "local"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    WRITER_DB_URL: str = f"pymysql://root:admin@localhost:3306/forsit"
    READER_DB_URL: str = f"pymysql://root:admin@localhost:3306/forsit"
    JWT_SECRET_KEY: str = "forsit_backend"
    JWT_ALGORITHM: str = "HS256"
    # SENTRY_SDN: str = None
    # CELERY_BROKER_URL: str = "amqp://user:bitnami@localhost:5672/"
    # CELERY_BACKEND_URL: str = "redis://:password123@localhost:6379/0"
    # REDIS_HOST: str = "localhost"
    # REDIS_PORT: int = 6379


class LocalConfig(Config):
    pass


class ProductionConfig(Config):
    DEBUG: bool = False


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "local": LocalConfig(),
    }
    return config_type[env]


config: Config = get_config()
