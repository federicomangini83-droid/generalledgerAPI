from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
import os
import csv

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in produzione puoi specificare un dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Percorso del file JSON da esporre
CSV_FILE_PATH = r"C:\Users\federico.mangini\Downloads\Demo_Unipol\Altro\S.32.01_Disclosure_Management.csv"

@app.get("/s3201_2024sol2_dm_99_group")
def leggi_dati():
    """Espone il contenuto del file JSON come API REST"""
    if not os.path.exists(CSV_FILE_PATH):
        raise HTTPException(status_code=404, detail="File CSV non trovato")

    try:
        with open(CSV_FILE_PATH, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
        return JSONResponse(content=data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

## python -m fastapi dev Downloads\Demo_Unipol\Altro\mainweb.py
## http://127.0.0.1:8000/s3201_2024sol2_dm_99_group