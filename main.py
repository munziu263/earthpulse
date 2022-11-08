import io
from fastapi import FastAPI
from fastapi.responses import FileResponse
from PIL import Image
from img_data import attributes


path = "/Users/munziu263/src/earthpulse/S2L2A_2022-06-09.tiff"

app = FastAPI()


@app.get("/attributes")
def get_attributes():
    return attributes


@app.get("/thumbnail")
def get_thumbnail():
    return FileResponse("thumbnail.png")


@app.get("/ndvi")
def get_ndvi():
    img = Image.open("ndvi.png")
    return FileResponse("ndvi.png")
