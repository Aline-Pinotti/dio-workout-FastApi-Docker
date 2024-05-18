from fastapi import FastAPI
from workout_api.routes import api_router

HOST = "0.0.0.0"
PORT = 8000

app = FastAPI(title="WorkoutApi")
app.include_router(api_router)

if __name__ == "main":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=PORT, log_level="info", reload=True) # poderia ser excluído se o make run funcionasse ¬¬'