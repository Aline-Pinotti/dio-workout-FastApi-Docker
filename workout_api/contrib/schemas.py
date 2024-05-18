import datetime
from typing import Annotated
from pydantic import UUID4, BaseModel, Field

class BaseSchema(BaseModel):
    class Config:
        extra = "forbid" # não vai aceitar campos extras, ou seja, que não estão nos models
        from_attributes = True # antigo orm_mode --> para fazer conversões de models para schema/schema pra models
    
class OutMixin(BaseModel):
    id: Annotated[UUID4, Field(description="Identificador")]
    created_at: Annotated[datetime, Field(description="Data de criação")]