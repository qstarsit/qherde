from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    rapidapi_key: str = Field()
    rapidapi_host: str

