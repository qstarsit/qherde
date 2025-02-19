from typing import Any
import httpx
from qherde.config import Settings


class AdsbService:
    def __init__(self) -> None:
        self._base_url = "https://adsbexchange-com1.p.rapidapi.com"
        self._headers = {
            "x-rapidapi-key": Settings().rapidapi_key,
            "x-rapidapi-host": Settings().rapidapi_host,
        }

    async def get_aircrafts(
        self, lat: str = "51.5005", lon: str = "-0.1145", distance: int = 30
    ) -> Any:
        async with httpx.AsyncClient(
            base_url=self._base_url, headers=self._headers
        ) as client:
            response = await client.get(url=f"/v2/lat/{lat}/lon/{lon}/dist/{distance}/")

        return response.json()
