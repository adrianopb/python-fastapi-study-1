from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/item/{item_id}")
async def read_item(item_id):
    return {"message": item_id}


@app.get("/item-only-int/{item_id}")
async def read_item_only_int(item_id: int):
    return {"message": item_id}


@app.get("/file/{file_path:path}")
async def read_file_path(file_path: str):
    return {"file_path": file_path}


@app.get("/item-path-and-query-params/{path_param}")
async def read_item_with_path_and_query_params(path_param: str, query_param: int, query_param_default: int = 5):
    return {"path_param": path_param,
            "query_param": query_param,
            "query_param_default": query_param_default}


@app.get("/items-with-annotated-and-path/{item_id}")
async def items_with_annotated_and_path(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=5)], item_id_query: str = "string default"
):
    results = {"item_id": item_id}
    if item_id_query:
        results.update({"item_id_query": item_id_query})
    return results
