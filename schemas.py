from pydantic import BaseModel;

# Pydantic Schema
class TodoBase(BaseModel):
    title:str
    description:str | None=None
    completed:bool=False

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id:int
    class config:
        orm_mode=True