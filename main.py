from fastapi import FastAPI, BackgroundTasks, background
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


@app.post("/api/v1/up")
async def vg_up(host: Host, background_tasks: BackgroundTasks):
    """
    Endpoint for 

    Args:
        host (Host): _description_

    Returns:
        _type_: _description_
    """
    path = "vm_Vagrantfile"
    background_tasks.add_task(vagrant_up, path)
    return {"message": "Up command start in the background"}


@app.post("/api/v1/destroy")
async def vg_down(host: Host, background_tasks: BackgroundTasks):
    path = "vm_Vagrantfile"
    background_tasks.add_task(vagrant_destroy, path)
    return {"message": "Destroy command start in the background"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
