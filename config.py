from enum import Enum
from pathlib import Path
from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    #kaggle
    KAGGLE_USERNAME: str | None = None
    KAGGLE_KEY: SecretStr | None = None

settings = Settings()
