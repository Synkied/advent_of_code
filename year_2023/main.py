import importlib

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Please use /days/{id} endpoint to get results."}


@app.get("/days/{day_id}")
async def read_item(day_id: int):
    solver = importlib.import_module(f"day_{day_id}.solver")
    result = solver.main()
    return {"results": result}
