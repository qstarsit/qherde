from typing import Any
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pathlib import Path

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

from qherde.services import adsb_service

BASE_DIR = Path(__file__).parent.resolve()

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR.joinpath("static").resolve()),
    name="static",
)

templates = Jinja2Templates(directory=BASE_DIR.joinpath("templates").resolve())


@app.get(path="/", response_class=HTMLResponse)
async def read_root(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"title": "Live flight near you!".title()},
    )


@app.get(path="/api/aircrafts")
async def get_aircrafts(lat: str = "51.5005", lon: str = "-0.1145") -> dict[str, Any]:
    aircrafts = await adsb_service.get_aircrafts(lat=lat, lon=lon)
    return aircrafts
