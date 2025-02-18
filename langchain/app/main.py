from fastapi import FastAPI, HTTPException
from app.reformaTributaria.controllerRT import router as rt_router
from app.nxjAssistant.controllerNA import router as na_router

app = FastAPI(title="Syssa", version="1.0.0")

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(rt_router)
app.include_router(na_router)
