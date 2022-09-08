from fastapi import FastAPI, BackgroundTasks, background, Request
from pydantic import BaseModel
from vagrant_app import vagrant_up, vagrant_destroy

app = FastAPI()

class Host(BaseModel):
    name: str
    status: str
    port: int
    host_address: str


@app.get("/api/v1/info")
def read_item(host_id: int):
    return host_id


@app.get("/api/v1/up")
async def vg_up(background_tasks: BackgroundTasks, request: Request):
    url = request.base_url._url
    background_tasks.add_task(vagrant_up, response_url = url)
    return {"message": "Up command start in the background "}


@app.get("/api/v1/destroy")
async def vg_down(background_tasks: BackgroundTasks, request: Request):
    url = request.url.path
    background_tasks.add_task(vagrant_destroy, response_url = url)
    return {"message": "Destroy command start in the background"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
