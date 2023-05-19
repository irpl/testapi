from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/data")
async def home(request: Request):
  data = await request.json();
  print(data)

  return {"message": "got it"}